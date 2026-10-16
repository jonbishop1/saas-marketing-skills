#!/usr/bin/env python3
"""Run selected fictional scenarios through Claude Code; preserve evidence for review.

This invokes the user's configured Claude model/account. Successful execution is
not a content-quality verdict. Review the outputs against each scenario's criteria.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time


def run_case(case, plugin, output, timeout):
    directory = output / case['id']
    directory.mkdir(parents=True, exist_ok=False)
    manifest = json.loads((plugin/'.claude-plugin/plugin.json').read_text())
    name = case['expected_skills'][0]
    prompt = f"Use /{manifest['name']}:{name}.\n\n{case['prompt']}\n\nReturn the requested artifact. Do not browse, change files, contact anyone or take external actions."
    (directory/'prompt.txt').write_text(prompt)
    config = directory/'empty-mcp.json'
    config.write_text('{"mcpServers":{}}\n')
    command = ['claude', '-p', '--output-format', 'stream-json', '--verbose',
               '--no-session-persistence', '--no-chrome', '--setting-sources', '',
               '--strict-mcp-config', '--mcp-config', str(config),
               '--permission-mode', 'dontAsk', '--max-budget-usd', '0.70',
               '--plugin-dir', str(plugin), '--tools', 'Read,Skill',
               '--allowedTools', 'Read', 'Skill']
    started = time.monotonic()
    with (directory/'trace.jsonl').open('w') as out, (directory/'stderr.txt').open('w') as err:
        try:
            process = subprocess.run(command, input=prompt, text=True, cwd=directory,
                                     stdout=out, stderr=err, timeout=timeout)
            code = process.returncode
        except subprocess.TimeoutExpired:
            code = -1
    rows = []
    for line in (directory/'trace.jsonl').read_text().splitlines():
        try:
            rows.append(json.loads(line))
        except ValueError:
            pass
    result = next((row for row in reversed(rows) if row.get('type') == 'result'), {})
    init = next((row for row in rows if row.get('type') == 'system' and row.get('subtype') == 'init'), {})
    calls = [block for row in rows if row.get('type') == 'assistant'
             for block in row.get('message', {}).get('content', []) if block.get('type') == 'tool_use']
    entry = plugin/'.agents/skills'/name/'SKILL.md'
    record = dict(id=case['id'], expected_skill=name, model=init.get('model'),
                  entrypoint_sha256=hashlib.sha256(entry.read_bytes()).hexdigest(),
                  exit_code=code, host_success=code == 0 and not result.get('is_error', True),
                  duration_seconds=round(time.monotonic()-started, 2),
                  invoked_skills=[c['input'].get('skill') for c in calls if c['name'] == 'Skill'],
                  tool_names=[c['name'] for c in calls],
                  permission_denials=result.get('permission_denials', []),
                  estimated_api_equivalent_usd=result.get('total_cost_usd'),
                  criteria=dict(must_include=case['must_include'], must_avoid=case['must_avoid']),
                  output=result.get('result', ''), quality_verdict='unreviewed')
    (directory/'result.json').write_text(json.dumps(record, indent=2)+'\n')
    (directory/'output.txt').write_text(record['output'])
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plugin-root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--ids', nargs='+', required=True, help='Explicit scenario IDs; no implicit full-suite run')
    parser.add_argument('--output', type=Path, required=True, help='New private output directory, outside the plugin')
    parser.add_argument('--timeout', type=int, default=150)
    args = parser.parse_args()
    plugin, output = args.plugin_root.resolve(), args.output.resolve()
    if plugin == output or plugin in output.parents:
        parser.error('Keep raw host traces outside the publishable plugin checkout.')
    scenarios = json.loads((plugin/'evals/scenarios.json').read_text())
    selected = [c for c in scenarios if c['id'] in args.ids]
    if {c['id'] for c in selected} != set(args.ids):
        parser.error('Unknown scenario ID; inspect evals/scenarios.json.')
    if any(len(c['expected_skills']) != 1 for c in selected):
        parser.error('This runner handles single-skill cases; use a routing-specific test for multi-skill cases.')
    output.mkdir(parents=True, exist_ok=False)
    # Sequential runs bound host/account pressure and make an interrupted batch resumable
    # by choosing only remaining IDs in a new output directory.
    results = []
    for case in selected:
        result = run_case(case, plugin, output, args.timeout)
        results.append(result)
        (output/'results.json').write_text(json.dumps(results, indent=2)+'\n')
        print(json.dumps({k:result[k] for k in ('id', 'host_success', 'invoked_skills')}), flush=True)
        if not result['host_success']:
            raise SystemExit('Stopped after host failure; inspect evidence before retrying.')


if __name__ == '__main__':
    main()
