# Marketing skills for developer tools and data products

> Behavioral repair candidate: packaging checks pass, but output-quality regressions remain. See [evaluation status](evals/README.md). Hold this branch for validation before release.

26 open-source [Agent Skills](https://agentskills.io/specification) by [Jon Bishop](https://jonbishop.co): practical workflows for helping technical users discover, evaluate, adopt, and buy a product. Covers developer tools, APIs, SDKs, open-source projects, data platforms, connectors, analytics products, and related technical software.

The collection keeps the repository and original `saas-*` names for compatibility. Version 2 redesigns those 16 skills for technical products and adds 10 focused workflows. This is not a general-purpose prompt pack: each skill defines its task, product-specific decisions, evidence requirements, output, and a linked playbook.

## Choose your product type

- [Developer-tool marketing skills](https://github.com/jonbishop1/devtool-marketing-skills): 25 skills for APIs, SDKs, CLIs, packages, open-source projects, and engineering workflows.
- [Data-product marketing skills](https://github.com/jonbishop1/data-product-marketing-skills): 25 skills for connectors, pipelines, databases, analytics platforms, and data workflows.

Each focused repository has product-specific skill names, decision criteria, examples, and installation instructions. Most marketing tasks have a version in both. README is developer-specific; workload evaluation is data-specific. This repository remains the shared authoring source and retains the original names for existing users.

To reproduce both distributions from this source, install the development requirements and run:

```sh
python scripts/export_collections.py --output /tmp/jon-bishop-marketing-collections
```

Each output is standalone: it contains its own license, skill folders, references, applicable templates, plugin manifests, checks, and evaluation scenarios. Generated files do not require this repository at runtime. Shared fixes and the product-specific overlays are maintained here.

## What is different

- Developer and data workflows change the recommendation: local versus hosted use, approved data access, correctness, maintenance ownership, production fit, and purchasing roles.
- Sample success, meaningful value, recurring use, and paid adoption are separate milestones.
- Factual claims need sources or observations. Hypotheses, unknowns, fictional examples, and untested code stay labeled.
- Work proceeds with available context. A full intake is optional, not a gate before every small task.
- Drafts and plans do not grant permission to post, message, spend, or change production systems.

## Skills

| Skill | Main job |
| --- | --- |
| [`saas-marketing-background`](.agents/skills/saas-marketing-background/SKILL.md) | Technical product marketing context |
| [`saas-audience-research`](.agents/skills/saas-audience-research/SKILL.md) | Audience research for developer and data products |
| [`saas-competitive-research`](.agents/skills/saas-competitive-research/SKILL.md) | Competitive evaluation for technical products |
| [`saas-customer-psychology`](.agents/skills/saas-customer-psychology/SKILL.md) | Technical adoption and buying decisions |
| [`saas-marketing-plan`](.agents/skills/saas-marketing-plan/SKILL.md) | Go-to-market planning for technical products |
| [`saas-content-strategy`](.agents/skills/saas-content-strategy/SKILL.md) | Content strategy for technical evaluation |
| [`saas-content-production`](.agents/skills/saas-content-production/SKILL.md) | Produce credible technical marketing content |
| [`saas-copywriting`](.agents/skills/saas-copywriting/SKILL.md) | Messaging and copy for technical products |
| [`saas-landing-pages`](.agents/skills/saas-landing-pages/SKILL.md) | Landing pages for technical evaluation |
| [`saas-seo-research`](.agents/skills/saas-seo-research/SKILL.md) | Search research for developer and data products |
| [`saas-seo-audit`](.agents/skills/saas-seo-audit/SKILL.md) | Audit technical product discoverability |
| [`saas-google-ads`](.agents/skills/saas-google-ads/SKILL.md) | Paid search for technical product demand |
| [`saas-meta-ads`](.agents/skills/saas-meta-ads/SKILL.md) | Paid social for developer and data products |
| [`saas-onboarding`](.agents/skills/saas-onboarding/SKILL.md) | Onboarding to meaningful technical value |
| [`saas-product-launches`](.agents/skills/saas-product-launches/SKILL.md) | Launch technical products and features |
| [`saas-data-analysis`](.agents/skills/saas-data-analysis/SKILL.md) | Analyze technical product adoption and economics |
| [`devtool-readme`](.agents/skills/devtool-readme/SKILL.md) | README as a developer evaluation path |
| [`devtool-quickstart`](.agents/skills/devtool-quickstart/SKILL.md) | Quickstarts that prove a useful task |
| [`devtool-agent-readiness`](.agents/skills/devtool-agent-readiness/SKILL.md) | Evidence-based agent readiness evaluation |
| [`devtool-community-distribution`](.agents/skills/devtool-community-distribution/SKILL.md) | Useful distribution in technical communities |
| [`data-product-evaluation`](.agents/skills/data-product-evaluation/SKILL.md) | Design a credible data-product evaluation |
| [`technical-pricing`](.agents/skills/technical-pricing/SKILL.md) | Pricing and packaging for technical workloads |
| [`technical-proof`](.agents/skills/technical-proof/SKILL.md) | Technical proof, benchmarks, and case studies |
| [`technical-sales-enablement`](.agents/skills/technical-sales-enablement/SKILL.md) | Help technical champions reach a decision |
| [`technical-conference-pipeline`](.agents/skills/technical-conference-pipeline/SKILL.md) | Conference conversations to qualified evaluations |
| [`technical-integration-marketing`](.agents/skills/technical-integration-marketing/SKILL.md) | Market a verified integration workflow |

## Choose a starting point

- “Help us pick an audience and a plan.” → `saas-audience-research`, then `saas-marketing-plan`.
- “Developers find us but cannot evaluate us.” → `devtool-readme`, `devtool-quickstart`, or `saas-onboarding`, depending on the barrier.
- “Can agents use our product?” → `devtool-agent-readiness`; specify a task and whether execution is allowed.
- “Our warehouse trial needs to prove value.” → `data-product-evaluation`.
- “Can we substantiate this performance claim?” → `technical-proof`.
- “Help us get useful conference conversations.” → `technical-conference-pipeline`.

Related skills are optional. Each folder is self-contained; you can copy one skill with its `references/` folder without installing the entire collection. A shared brief from `saas-marketing-background` can reduce repeated context when using several skills.

## Use with an Agent Skills-compatible tool

Canonical source: `.agents/skills/<skill-name>/SKILL.md`. Each folder has standard YAML frontmatter and a relative-linked reference playbook. There are no required external services, runtime hooks, or paid tools. Live research and execution depend on the capabilities and permissions of your host.

Clone this repository, then place the desired skill folders in the skill location documented by your host, preserving the folder names and references. This repository's format validation does not certify every host's discovery or runtime behavior.

For project-local tools that discover `.agents/skills`, copying these folders into that directory is the direct layout. Avoid installing the same skills by multiple discovery paths in one host.

## Codex usage

Copy the desired skill folders with their references/assets into your project’s `.agents/skills/`, then invoke a skill such as `$saas-copywriting`. See the [Codex evaluation notes](evals/README.md#codex-follow-up) for tested scope and limits.

## Claude Code plugin

The plugin manifest explicitly scans `./.agents/skills/`; it does not depend on local `.claude/skills` symlinks.

```text
/plugin marketplace add jonbishop1/saas-marketing-skills
/plugin install saas-marketing-skills@saas-growth-pros
```

`saas-growth-pros` is the legacy marketplace identifier, retained so the installation name remains compatible. The display name is Developer & Data Product Marketing Skills. Follow the host's reload prompt if it requires one.

To validate a local plugin checkout using a compatible Claude Code CLI:

```sh
claude plugin validate .
```

The focused collections are published separately. The commands above retain the original combined collection's installation name for existing users. Local validation is separate from a live host behavior test.

## Open format and open source

“Agent Skills” here refers to the [open format specification](https://agentskills.io/specification), not MCP and not a certification. Frontmatter has a directory-matching `name`, a task-specific `description`, an SPDX `license`, and string-valued metadata. The core instructions stay short and load details from references when needed.

The code and authored skill content are MIT-licensed; see [LICENSE](LICENSE). This license does not relicense external sources, vendor documentation, logos, datasets, or private customer material. Respect their licenses and permissions.

## Validation and contributions

```sh
python3 -m venv /tmp/technical-marketing-skills-venv
/tmp/technical-marketing-skills-venv/bin/pip install -r requirements-dev.txt
/tmp/technical-marketing-skills-venv/bin/python scripts/validate.py
/tmp/technical-marketing-skills-venv/bin/python -m unittest discover -s tests
```

CI runs structural, packaging, link, and validator regression checks. The [evaluation scenarios](evals/scenarios.json) cover task routing, domain decisions, evidence limits, and action boundaries; they are a behavioral review suite, not a claim of automated model evaluation. See [CONTRIBUTING.md](CONTRIBUTING.md) for the review procedure and optional official `skills-ref` validation.

Structural checks cannot prove a skill makes good decisions. Review realistic developer and data-product requests before distributing changes.
