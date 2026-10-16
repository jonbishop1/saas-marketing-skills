#!/usr/bin/env python3
"""Repository checks, complementing (not replacing) official skills-ref validation."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate YAML keys rather than silently keeping the last value."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError('duplicate frontmatter key: ' + str(key))
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
FIELDS = {'name', 'description', 'license', 'metadata', 'compatibility', 'allowed-tools'}
LINK = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')


def inside(path, parent):
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def local_links(path, boundary):
    errors = []
    for target in LINK.findall(path.read_text()):
        target = target.strip().strip('<>')
        parsed = urlsplit(target)
        if parsed.scheme or not parsed.path:
            continue
        resolved = path.parent / unquote(parsed.path)
        if not inside(resolved, boundary):
            errors.append(f'{path.name}: local link escapes package: {target}')
        elif not resolved.exists():
            errors.append(f'{path.name}: missing local link: {target}')
    return errors


def validate_skill(directory):
    errors = []
    path = directory / 'SKILL.md'
    if not path.is_file():
        return ['missing SKILL.md']
    content = path.read_text()
    match = re.match(r'\A---\n(.*?)\n---\n(.+)\Z', content, re.S)
    if not match:
        return ['missing frontmatter or body']
    try:
        meta = yaml.load(match.group(1), Loader=UniqueLoader)
    except (yaml.YAMLError, ValueError, TypeError) as exc:
        return [f'invalid frontmatter: {exc}']
    if not isinstance(meta, dict):
        return ['frontmatter must be a mapping']
    if set(meta) - FIELDS:
        errors.append('unknown frontmatter fields')
    name = meta.get('name')
    if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
        errors.append('invalid name (repository uses the ASCII subset of Agent Skills names)')
    if name != directory.name:
        errors.append('name does not match directory')
    desc = meta.get('description')
    if not isinstance(desc, str) or not 1 <= len(desc.strip()) <= 1024:
        errors.append('description must contain 1–1024 characters')
    if meta.get('license') != 'MIT':
        errors.append('repository skills must declare MIT')
    metadata = meta.get('metadata')
    if not isinstance(metadata, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in metadata.items()):
        errors.append('metadata must contain string keys and values')
    if 'compatibility' in meta and (not isinstance(meta['compatibility'], str) or not 1 <= len(meta['compatibility']) <= 500):
        errors.append('invalid compatibility field')
    if 'allowed-tools' in meta and not isinstance(meta['allowed-tools'], str):
        errors.append('allowed-tools must be a string')
    if len(content.splitlines()) >= 500:
        errors.append('keep SKILL.md under 500 lines; move detail to references')
    if re.search(r'\[TODO:|\bTBD\b', content):
        errors.append('unfinished placeholder in instructions')
    # No runtime dependencies on sibling skills: a selected folder is portable.
    for file in directory.rglob('*.md'):
        if not inside(file, directory):
            errors.append('skill contains a symlink outside its package')
        else:
            errors.extend(local_links(file, directory))
    return errors


def validate_repository(root):
    errors = []
    directories = sorted(p for p in (root/'.agents/skills').iterdir() if p.is_dir())
    if not directories:
        return ['no skills found']
    for directory in directories:
        errors.extend(f'{directory.name}: {e}' for e in validate_skill(directory))
    try:
        manifest = json.loads((root/'.claude-plugin/plugin.json').read_text())
        marketplace = json.loads((root/'.claude-plugin/marketplace.json').read_text())
        if manifest['skills'] != ['./.agents/skills/']:
            errors.append('plugin must discover the canonical skill directory')
        if manifest['name'] != 'saas-marketing-skills' or marketplace['name'] != 'saas-growth-pros':
            errors.append('legacy plugin and marketplace identifiers must remain compatible')
        if marketplace['plugins'][0]['name'] != manifest['name'] or marketplace['plugins'][0]['source'] != './':
            errors.append('marketplace must resolve to this plugin')
        for directory in directories:
            fm = (directory/'SKILL.md').read_text().split('---\n', 2)[1]
            metadata = yaml.load(fm, Loader=UniqueLoader).get('metadata', {})
            if metadata.get('version') != manifest['version']:
                errors.append(f'{directory.name}: skill and plugin versions differ')
    except (OSError, KeyError, IndexError, ValueError, TypeError, yaml.YAMLError) as exc:
        errors.append(f'packaging: {exc}')
    for filename in ('README.md', 'CONTRIBUTING.md'):
        path = root/filename
        if path.exists():
            errors.extend(local_links(path, root))
    if not (root/'LICENSE').is_file() or 'MIT License' not in (root/'LICENSE').read_text():
        errors.append('missing MIT license')
    try:
        cases = json.loads((root/'evals/scenarios.json').read_text())
        names = {p.name for p in directories}
        ids = set()
        covered = set()
        for case in cases:
            if case['id'] in ids:
                errors.append('duplicate evaluation id: ' + case['id'])
            ids.add(case['id'])
            if not case['expected_skills'] or not set(case['expected_skills']) <= names:
                errors.append('evaluation references unknown or missing skills: ' + case['id'])
            covered.update(case['expected_skills'])
            if not case['prompt'].strip() or not case['must_include'] or not case['must_avoid']:
                errors.append('evaluation needs a prompt and positive/negative criteria: ' + case['id'])
        if names - covered:
            errors.append('skills missing evaluation scenarios: ' + ', '.join(sorted(names - covered)))
    except (OSError, KeyError, TypeError, ValueError) as exc:
        errors.append(f'evaluation suite: {exc}')
    readme = (root/'README.md').read_text()
    for directory in directories:
        if f'.agents/skills/{directory.name}/SKILL.md' not in readme:
            errors.append('skill missing from README: ' + directory.name)
    count_match = re.search(r'^(\d+) open-source', readme, re.M)
    if not count_match or int(count_match.group(1)) != len(directories):
        errors.append('README skill count is incorrect')
    return errors


if __name__ == '__main__':
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    failures = validate_repository(root)
    if failures:
        print('\n'.join(f'ERROR: {message}' for message in failures))
        sys.exit(1)
    print(f'PASS: {len(list((root/".agents/skills").glob("*/SKILL.md")))} skills; metadata, local links, packaging, and scenario coverage')
