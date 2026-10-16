#!/usr/bin/env python3
"""Build two standalone, product-specific distributions from shared authored source."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'.agents/skills'
TARGETS = {
    'devtool': dict(repo='devtool-marketing-skills', label='Developer-tool marketing',
                    product='developer tools', exclude='data-product-evaluation',
                    fixture='TraceNest is a fictional local HTTP replay tool. An engineer can replay a sanitized fixture locally, but service integration needs a platform owner. Sample replay is not proof of recurring project value. Do not invent hosted behavior, speed improvements, or customer results.'),
    'data-product': dict(repo='data-product-marketing-skills', label='Data-product marketing',
                         product='data products', exclude='devtool-readme',
                         fixture='FlowLake is a fictional incremental ingestion product. A synthetic source-to-warehouse sample works, but real data needs approved credentials and reconciliation. Sample completion is not production approval. Update, delete, late-arrival, freshness, and recovery behavior must be verified rather than assumed.'),
}

# Each pair changes the task decision and its evidence requirements. These are
# authored domain overlays, not substitutions of product names in generic prose.
DECISIONS = {
    'saas-marketing-background': (
        'Record language/runtime, local or hosted execution, package or repository access, current debugging/integration workflow, and who maintains a new dependency. Define first useful task success and repeated project use separately.',
        'Record source and destination, data sensitivity, update patterns, schema, freshness/correctness requirements, access owner, and workload economics. Define reconciled real-data output and approved recurring operation separately.'),
    'saas-audience-research': (
        'Compare segments by stack, recurring engineering task, deployment policy, integration authority, and dependency ownership. Separate tutorial learners from teams with a production problem; include maintainers and internal-build alternatives.',
        'Compare segments by source-to-consumer workflow, correctness/freshness need, access authority, and operational ownership. Distinguish analyst interest, engineering evaluation, platform review, and budget authority.'),
    'saas-competitive-research': (
        'Compare the tool with scripts, framework features, existing platform tooling, and open-source packages on the exact engineering task. Inspect installability, maintenance, licensing, integration effort, and reversibility before claiming a reason to switch.',
        'Compare the workload against SQL jobs, open-source connectors, and managed platforms. Require equivalent update/delete semantics, reconciliation, freshness, failure recovery, access model, and cost conditions before claiming superiority.'),
    'saas-customer-psychology': (
        'Investigate whether hesitation concerns owning another dependency, exposing payloads, debugging integration failure, or persuading a platform owner. Offer a reversible local proof and a clear maintenance boundary; do not attribute every stall to developer skepticism.',
        'Investigate concern about silent corruption, credential scope, data movement, migration, or operating a failed workload. Offer reconciliation evidence and an approved bounded evaluation; retain governance controls rather than treating them as persuasion problems.'),
    'saas-marketing-plan': (
        'Sequence task-specific discovery, a runnable example, own-project success, and team adoption. If setup fails, prioritize evaluation reliability before additional distribution. Measure qualified projects and recurring useful tasks instead of stars or package downloads.',
        'Sequence workload-specific demand, access approval, representative correctness evaluation, and operating ownership. If credentials or reconciliation block progress, resolve that path before increasing demos. Measure approved real-data evaluations separately from sample runs.'),
    'saas-content-strategy': (
        'Build around supported stacks, debugging and integration tasks, migration decisions, and production tradeoffs. Choose a canonical docs path and a distinct editorial purpose; avoid duplicating reference documentation to fill a calendar.',
        'Build around source/destination behavior, schema changes, late arrivals, reconciliation, freshness, governance, and workload cost. Require a verified example or defensible evidence for each proposed connector or performance topic.'),
    'saas-content-production': (
        'For tutorials state supported runtime, installation, sanitized input, expected result, failure recovery, and integration boundary. Test only in the authorized environment, label untested commands, and show a process diagram when it explains execution.',
        'For guides state data provenance, shape, transformations, expected invariants, access scope, reconciliation, and operating limits. Label synthetic records and illustrative charts; do not publish a performance conclusion without equivalent, reproducible workloads.'),
    'saas-copywriting': (
        'Anchor copy in the engineering task, supported environment, input/output, and evidence of reduced effort or risk. Distinguish local/open-source use from paid hosted behavior; select a runnable example or docs CTA when that fits readiness.',
        'Anchor copy in the data workflow and the output users can validate. Qualify freshness, correctness, scale, and cost claims; distinguish connectivity from correct recurring operation. Offer a sample or approved workload evaluation with clear prerequisites.'),
    'saas-landing-pages': (
        'Organize the page around task, supported stack, input/output, runnable path, integration limits, proof, and adoption requirements. Provide an evaluator route and a platform/buyer route where they need different evidence.',
        'Organize the page around workload, source-to-destination flow, supported semantics, reconciliation evidence, permissions, cost, and evaluation. Separate credential-free sample access from approved real-data setup instead of promising instant production access.'),
    'saas-seo-research': (
        'Separate programming education, package support, jobs, debugging, integration, and tool-selection intent. Favor tasks the product can actually complete and check whether official framework docs already answer the query better.',
        'Separate conceptual education from operational source/destination, schema, recovery, freshness, and cost queries. A connector page needs verified behavior and a distinct task; do not map every possible product pair to an indexable page.'),
    'saas-seo-audit': (
        'Inspect docs versioning, repository/package links, supported framework examples, rendered task instructions, canonical paths, and useful transitions into a runnable evaluation. Diagnose the observed rendering issue before proposing a stack rewrite.',
        'Inspect connector and workload pages for distinct supported semantics, source evidence, evaluation instructions, and appropriate canonical structure. Check whether thin integration permutations obscure the useful documentation and proof.'),
    'saas-google-ads': (
        'Classify learner, job, support, free-package, commercial-tool, and production-task queries before excluding or bidding. Define qualified own-project evaluation and recurring use; do not optimize a campaign solely for low-cost signups.',
        'Tie query groups to supported source/destination workloads and buying context. Qualify access, platform fit, correctness needs, and an evaluation owner; account for delayed enterprise qualification and distinguish students from deployable accounts.'),
    'saas-meta-ads': (
        'Judge whether a verified task demonstration can reach relevant engineers in an interruption channel. Broad interests do not establish a developer role or deployment authority. Connect engagement to useful task evaluation, with a capped hypothesis test.',
        'Judge whether a synthetic workflow explanation or proof asset reaches a credible evaluator. A content download does not establish platform authority or approved data access. Preserve data privacy and evaluate downstream workload fit.'),
    'saas-onboarding': (
        'Map installation, environment compatibility, credentials if needed, sample task, own-project task, repeat use, and team integration. Provide recovery and a maintenance owner; distinguish automation/retries from independent successful use.',
        'Map approved access, source connection, initial output, reconciliation, incremental changes, recurring runs, and production approval. Keep sample success and real-data success separate; show the next useful step while an administrator reviews access.'),
    'saas-product-launches': (
        'Verify package/repository access, license, supported runtime, install commands, a reproducible demo, limitations, and maintainer support before choosing launch scope. Measure task success and repeated project adoption alongside attention.',
        'Verify connector behavior, approved evaluation data, reconciliation, access scope, cost limits, operating ownership, and recovery before choosing launch scope. A sample-only test can support a scoped beta claim, not unqualified production availability.'),
    'saas-data-analysis': (
        'Choose person/project/workspace/account identities deliberately. Separate downloads, automated API activity, sample success, own-project useful tasks, repeat project use, and paid team adoption. Cohort by eligibility and complete observation windows.',
        'Choose workload/workspace/account identities deliberately. Separate sample runs, valid real-data output, reconciliation, recurring approved operation, and paid adoption. Include empty/failed runs, freshness, operating cost, and complete observation windows.'),
    'devtool-readme': (
        'Expose task, local/hosted boundary, supported runtime, minimal verified command, expected output, license, maintenance, and support. Make the route from a sample to own-project adoption clear without inventing traction badges.',
        'Not included in the data-product collection.'),
    'devtool-quickstart': (
        'Use one supported engineering task with sanitized input, exact prerequisites, expected output, deterministic success assertion, recovery, and cleanup. Disclose credentials or hosted costs before commands and distinguish verified execution from plausible instructions.',
        'Use synthetic or authorized records with explicit schema, expected keys/values, reconciliation checks, connector permissions, resource caps, and cleanup. A green connection or sample dashboard alone is not the success assertion.'),
    'devtool-agent-readiness': (
        'Assess a defined engineering task through available docs/API/SDK/CLI/MCP/skills paths. Separate discoverability, documented setup, authorized execution, result verification, and recovery; no particular interface file is sufficient or mandatory.',
        'Assess a defined data task through documented interfaces, scoped access, schema discovery, query/workload cost, correctness, freshness, and partial-failure recovery. Public-only evidence cannot prove authenticated execution or production data readiness.'),
    'devtool-community-distribution': (
        'Choose stack-specific communities, maintainers, or package ecosystems where the task is relevant. Offer a reproducible answer and disclose affiliation. Respect project governance and maintain the example rather than turning issue trackers into promotion channels.',
        'Choose source/warehouse ecosystems and practitioner communities where the workload is relevant. Contribute a synthetic reconciliation example, operational lesson, or transparent methodology; never expose private customer queries or records.'),
    'data-product-evaluation': (
        'Not included in the developer-tool collection.',
        'Agree on the decision, baseline, representative authorized workload, correctness invariants, updates/deletes/late arrivals, recovery, freshness, cost cap, ownership, and cleanup before results. Keep proposed criteria and measured outcomes distinct.'),
    'technical-pricing': (
        'Select the developer workload only when a brief also labels a separate data workload. Do not price unrelated source-row activity as CLI usage. Compare human seats, automation and team licensing; local software can be commercial without a hosted service.',
        'Select the data workload only when a brief labels a separate developer workload. Do not import that other product\'s human/CI identities or requests into this offer. If this data product has no supplied user count, a numeric seat scenario is unavailable. Compare data volume, scan/compute, refresh, retention and egress; billed resource use and change counts are distinct.'),
    'technical-proof': (
        'Define the actual task and baseline before making productivity or speed claims. A faster local demonstration does not prove team productivity. Record versions, equivalent setup, correctness, failures, repeated runs, and reproducibility.',
        'Prove equivalent output and semantics before comparing workload speed or cost. Record dataset shape and skew, updates, cache state, concurrency, freshness, failures, resources, repeated runs, and uncertainty. Include unfavorable conditions and limitations.'),
    'technical-sales-enablement': (
        'Turn an individual successful task into an honest team-evaluation memo: dependency and maintenance owner, integration effort, deployment and security review, commercial fit, reversibility, and an owned next test. Do not call a local demo production adoption.',
        'Turn a reconciled evaluation slice into an honest decision memo: source/destination fit, approved data boundary, recovery, recurring operation, procurement, cost predictability, and owner. State remaining production tests and a no-go option.'),
    'technical-conference-pipeline': (
        'Use a reproducible engineering demo with a safe offline fallback. Qualify stack, recurring task, and team-integration ownership. Capture only permitted notes and an agreed next step; badge scans are not qualified pipeline or blanket outreach consent.',
        'Use synthetic records and a workload-evaluation worksheet. Qualify source/destination, correctness/freshness need, access owner, and platform approval without collecting sensitive data. Track agreed evaluations separately from scans and conversations.'),
    'technical-integration-marketing': (
        'Verify the SDK/CLI/plugin/CI/API workflow, versions, permissions, expected result, artifact storage, secrets handling, maintenance, and support ownership. Distinguish a custom example from an officially supported partner integration.',
        'Verify source, transformation, destination, schema/update semantics, credentials, reconciliation, freshness, partial failures, and recovery. Connectivity alone does not prove correct operation; distinguish a tested supported connector from a custom example.'),
}


def exported_name(name, prefix):
    for start in ('saas-', 'technical-', 'devtool-', 'data-product-'):
        if name.startswith(start):
            return prefix+'-'+name[len(start):]
    raise ValueError(name)


def parse(path):
    _, fm, body = path.read_text().split('---', 2)
    return yaml.safe_load(fm), body.strip()


def section(body, heading):
    return body.split('## '+heading+'\n\n', 1)[1].split('\n## ', 1)[0].strip()


def export(destination):
    all_exports = {}
    for index, (prefix, config) in enumerate(TARGETS.items()):
        folder = destination/config['repo']
        folder.mkdir(parents=True, exist_ok=True)
        if (folder/'.agents').exists():
            shutil.rmtree(folder/'.agents')
        mapping = {}
        rows = []
        for source in sorted(SOURCE.iterdir()):
            if not source.is_dir() or source.name == config['exclude']:
                continue
            name = exported_name(source.name, prefix)
            mapping[source.name] = name
            target = folder/'.agents/skills'/name
            shutil.copytree(source, target)
            meta, original = parse(source/'SKILL.md')
            meta.update(name=name)
            original_desc = meta['description']
            meta['description'] = original_desc.replace('developer tools and data products', config['product']).replace('developer tools or data products', config['product'])
            meta['metadata'].update(version='1.0.1', audience=config['product'].replace(' ', '-'), source_skill=source.name)
            title = name[len(prefix)+1:].replace('-', ' ').capitalize()
            focus = section(original, 'Product-specific decisions')
            developer, data = focus.removeprefix('**Developer tools:** ').split('\n\n**Data products:** ',1)
            workflow = section(original, 'Workflow')
            if (source/'references'/f'{prefix}-example.md').exists():
                workflow = workflow+'\n\n### Decision example (fictional; use the user\'s facts for the deliverable)\n\n'+(source/'references'/f'{prefix}-example.md').read_text().split('\n\n',1)[1]
            workflow += '\n\n## '+config['label']+' decisions\n\n'+DECISIONS[source.name][index]
            workflow += '\n\n'+(developer if prefix=='devtool' else data)
            body = f'# {title} for {config["product"]}\n\n'
            body += section(original,'Working rules')+'\n\n'
            body += '## Product scope\n\n'+('APIs, SDKs, CLIs, packages, open-source projects, and other products used in engineering workflows.' if prefix=='devtool' else 'Connectors, pipelines, databases, warehouses, analytics, and other products that move, transform, query, or operationalize data.')+'\n\n'
            body += '## Inputs\n\n'+section(original,'Inputs')+'\n\n## Workflow\n\n'+workflow+'\n\n'
            body += '## Deliverable\n\n'+section(original,'Deliverable')+'\n\n## Quality checks\n\n'+section(original,'Quality checks')+'\n\n'
            body += '## Reference\n\nUse the [task playbook](references/playbook.md) for a worked domain scenario and acceptance criteria. All example companies are fictional.\n'
            if (target/'assets').exists():
                for asset in sorted((target/'assets').glob('*.md')):
                    body += '\nFill the ['+asset.stem.replace('-',' ')+'](assets/'+asset.name+') only with supported facts; unknown results stay unfilled.\n'
            (target/'SKILL.md').write_text('---\n'+yaml.safe_dump(meta,sort_keys=False,width=96)+'---\n\n'+body)
            playbook = '# '+title+' playbook\n\n## Fictional product context\n\n'+config['fixture']+'\n\n'
            playbook += '## Decision to resolve\n\n'+DECISIONS[source.name][index]+'\n\n'
            playbook += '## Task-specific method\n\n'+(developer if prefix=='devtool' else data)+'\n\n'
            playbook += '## Output worksheet\n\n| Field | Record |\n| --- | --- |\n| Requested decision and task | |\n| User, evaluator, buyer, and owner | |\n| Supported behavior and environment | |\n| Evidence, source, and limits | |\n| Proposed action or finished artifact | |\n| Meaningful result and verification | |\n| Unknowns, failure, and stop condition | |\n\n'
            example = source/'references'/f'{prefix}-example.md'
            if example.exists():
                playbook += '## Completed example\n\n'+example.read_text().split('\n\n',1)[1]+'\n'
            else:
                playbook += '## Application brief\n\nDeliver: '+section(original,'Deliverable')+'\n\n'
            for example_file in (target/'references').glob('*-example.md'):
                example_file.unlink()
            playbook += 'Do not assume missing capabilities or report proposed tests as completed. A useful answer identifies what is known, finishes the requested artifact within that scope, and names the next bounded verification when needed.\n\n'
            playbook += '## Review criteria\n\n'+section(original,'Quality checks')+'\n\n'
            # Preserve the richer original reference as an optional methods file;
            # the entrypoint and primary playbook remain product-specific.
            shutil.copy2(source/'references/playbook.md',target/'references/shared-methods.md')
            playbook += 'The [shared method examples](shared-methods.md) provide additional templates and cross-product examples; apply only those that fit the product scope.\n'
            (target/'references/playbook.md').write_text(playbook)
            rows.append(dict(source=source.name,name=name,title=title,description=meta['description'],focus=DECISIONS[source.name][index],repository=config['repo']))
        for filename in ('LICENSE','.gitignore','requirements-dev.txt'):
            shutil.copy2(ROOT/filename, folder/filename)
        (folder/'.claude-plugin').mkdir(exist_ok=True)
        plugin=dict(name=config['repo'],version='1.0.1',description=f"{len(rows)} open-source marketing skills for {config['product']}: research, content, acquisition, technical evaluation, activation, proof, pricing, and sales.",author=dict(name='Jon Bishop',url='https://jonbishop.co'),homepage=f'https://jonbishop.co/directories/ai-marketing-skills/{"developer-tools" if prefix=="devtool" else "data-products"}/',repository='https://github.com/jonbishop1/'+config['repo'],license='MIT',skills=['./.agents/skills/'])
        (folder/'.claude-plugin/plugin.json').write_text(json.dumps(plugin,indent=2)+'\n')
        marketplace=dict(name='jon-bishop-'+prefix,description=config['label']+' skills by Jon Bishop.',owner=dict(name='Jon Bishop',url='https://jonbishop.co'),plugins=[dict(name=config['repo'],source='./',description=plugin['description'])])
        (folder/'.claude-plugin/marketplace.json').write_text(json.dumps(marketplace,indent=2)+'\n')
        (folder/'scripts').mkdir(exist_ok=True)
        (folder/'tests').mkdir(exist_ok=True)
        # Reuse the format/link validator, with collection-aware packaging rules.
        validator=(ROOT/'scripts/validate.py').read_text()
        validator=validator.replace("manifest['name'] != 'saas-marketing-skills' or marketplace['name'] != 'saas-growth-pros'",f"manifest['name'] != '{config['repo']}' or marketplace['name'] != 'jon-bishop-{prefix}'")
        validator=validator.replace("legacy plugin and marketplace identifiers must remain compatible","collection plugin and marketplace identifiers must match")
        (folder/'scripts/validate.py').write_text(validator)
        shutil.copy2(ROOT/'scripts/run_behavior.py',folder/'scripts/run_behavior.py')
        test=(ROOT/'tests/test_validation.py').read_text()
        test=test.replace('devtool-agent-readiness',prefix+'-agent-readiness').replace('name: another-skill','name: another-skill')
        test=test.replace('version: 2.0.1','version: 1.0.1')
        test=test.replace('../saas-copywriting/SKILL.md','../'+prefix+'-copywriting/SKILL.md')
        (folder/'tests/test_validation.py').write_text(test)
        shutil.copy2(ROOT/'tests/test_behavior_runner.py',folder/'tests/test_behavior_runner.py')
        scenarios=[]
        for case in json.loads((ROOT/'evals/scenarios.json').read_text()):
            if case.get('product_scope') and case['product_scope'] != prefix:
                continue
            if config['exclude'] in case['expected_skills']:
                continue
            if prefix == 'devtool' and re.search(r'warehouse|data connector|ingestion|data platform|data product|late.arrival|reconcil|incremental', case['prompt'], re.I):
                continue
            if prefix == 'data-product' and re.search(r'local replay|replay tool|HTTP|webhook|backend|CLI|repository visits|developer tool', case['prompt'], re.I):
                continue
            case['expected_skills']=[mapping[name] for name in case['expected_skills']]
            scenarios.append(case)
        # A product-specific scenario for every package, in addition to shared
        # boundary regressions. Authored scenarios are not reported model runs.
        for row in rows:
            scenarios.append(dict(id=prefix+'-'+row['name'],expected_skills=[row['name']],prompt=f"For this fictional product, complete the {row['title']} task. {config['fixture']} Work with available facts and mark evidence gaps.",must_include=[row['focus'],'Concrete deliverable with evidence limits'],must_avoid=['Invented product capabilities or results','Unauthorized external actions']))
        (folder/'evals').mkdir(exist_ok=True)
        (folder/'evals/scenarios.json').write_text(json.dumps(scenarios,indent=2)+'\n')
        (folder/'evals/README.md').write_text((ROOT/'evals/README.md').read_text())
        table='\n'.join(f"| [`{r['name']}`](.agents/skills/{r['name']}/SKILL.md) | {r['title']} |" for r in rows)
        readme=f'''# {config['label']} skills

> Behavioral repair candidate: output-quality regressions remain. See [evaluation status](evals/README.md). Hold this branch for validation before release.

{len(rows)} open-source [Agent Skills](https://agentskills.io/specification) by [Jon Bishop](https://jonbishop.co) for marketing {config['product']}. Each skill includes a bounded workflow, domain-specific decisions, an evidence standard, a deliverable, and a linked playbook. There are no required paid services or runtime hooks.

## Built for this product type

{('Engineering adoption runs from a useful local or sandbox task to real-project integration, repeated use, and team ownership. These skills account for supported stacks, packages and SDKs, open-source licensing, deployment policy, maintainers, and platform approval. Downloads and stars are not activation.' if prefix=='devtool' else 'Data adoption runs from an approved sample to correct real-data output, reconciliation, recurring workloads, and production approval. These skills account for source/destination semantics, schema changes, freshness, permissions, recovery, governance, and workload economics. A green connector is not proof of value.')}

This collection has its own skill names, product-specific guidance, and examples. For the other product type, see [{TARGETS['data-product' if prefix=='devtool' else 'devtool']['label']} skills](https://github.com/jonbishop1/{TARGETS['data-product' if prefix=='devtool' else 'devtool']['repo']}).

## Install

Clone this repository and copy the desired `.agents/skills/<name>/` folders into the skill location documented by your Agent Skills-compatible host. Keep each folder's references and assets. Each skill is standalone; shared context is optional. Avoid installing duplicate copies through several discovery paths.

For Claude Code:

```text
/plugin marketplace add jonbishop1/{config['repo']}
/plugin install {config['repo']}@jon-bishop-{prefix}
```

The manifest explicitly discovers `./.agents/skills/`. Format and manifest validation do not establish that every host can load or execute every task. Live research and execution depend on your host's tools and your authorization.

## Skills

| Skill | Task |
| --- | --- |
{table}

## Evidence and actions

Facts, observations, hypotheses, and unknowns stay distinct. Examples are fictional unless explicitly described as measured evidence. Sample success does not establish production readiness. Plans and drafts do not authorize publishing, messaging, spending, or production changes; existing user authorization governs execution.

## Validate and contribute

Use Python 3.9 or later for the repository checks, in an isolated environment:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

The final two commands require a compatible Claude Code CLI. The [official reference validator](https://github.com/agentskills/agentskills/tree/main/skills-ref) requires Python 3.11 or later and can validate each skill folder. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [evaluation scenarios](evals/scenarios.json). Authored scenarios are not completed model runs.

## Source and license

This is a standalone distribution generated from [shared authored source](https://github.com/jonbishop1/saas-marketing-skills), with domain overlays maintained there. Prefer contributing shared fixes upstream so both collections receive them. No sibling repo is required at runtime.

MIT — see [LICENSE](LICENSE). External documentation, logos, datasets, and customer material retain their own rights and permissions.
'''
        (folder/'README.md').write_text(readme)
        contribution=(ROOT/'CONTRIBUTING.md').read_text().replace('Keep the original `saas-*` names unless a separately planned migration justifies breaking compatibility.','Keep the published product-specific names stable; propose any migration explicitly.')
        (folder/'CONTRIBUTING.md').write_text(contribution)
        (folder/'CHANGELOG.md').write_text('# Changelog\n\n## 1.0.1\n\nImprove evidence boundaries, pricing economics, analytics cohorts, synthetic evaluation and readiness decisions. Add completed task examples and targeted behavioral regressions.\n\n## 1.0.0\n\nInitial focused collection with 25 domain-specific marketing skills, linked playbooks, standalone assets where applicable, format validation, regression tests, and authored behavioral scenarios.\n')
        if (ROOT/'.github').exists():
            shutil.copytree(ROOT/'.github',folder/'.github',dirs_exist_ok=True)
        files={str(p.relative_to(folder)):hashlib.sha256(p.read_bytes()).hexdigest() for p in folder.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts}
        all_exports[prefix]=dict(**config,skills=rows,files=files)
    return all_exports


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    result=export(args.output)
    (args.output/'collections.json').write_text(json.dumps(result,indent=2)+'\n')
    print(', '.join(f'{cfg["repo"]}: {len(cfg["skills"])} skills' for cfg in result.values()))
