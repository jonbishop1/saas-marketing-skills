# Contributing

Keep this collection useful for people marketing developer tools and data products. A contribution should change a decision or improve a concrete deliverable, not merely replace “SaaS” with “developer.”

## Scope and structure

- Keep canonical source in `.agents/skills/<name>/SKILL.md`, using the [Agent Skills specification](https://agentskills.io/specification).
- Keep the original `saas-*` names unless a separately planned migration justifies breaking compatibility.
- Each skill must work when copied alone with its references and assets. Shared context is optional. Use relative links; no absolute personal paths or required sibling dependencies.
- Keep the entrypoint concise. Load task-specific templates and examples from references or assets. Do not add required connectors or vendor accounts to a markdown-only workflow.
- Use factual, task-specific descriptions so hosts can distinguish adjacent skills. Explain when another skill owns the task rather than triggering on every marketing term.
- Preserve the MIT license and source attribution. External material retains its own license; do not copy substantial vendor or third-party content into the repo.

## Quality bar

State inputs, a decision-changing workflow, developer-tool and data-product differences, the deliverable, and verification limits. Do not require a full intake before answering a narrow request. Carry forward supplied context and ask only for missing facts that matter.

Separate facts, observations, hypotheses, and unknowns. Sample success is not real-data success; documentation is not executed proof; attribution is not causation. No invented metrics, quotes, customers, tests, screenshots, or benchmark results. Fictional examples must be labeled.

Planning and writing do not authorize external messages, publishing, spending, or production changes. Respect authorization already present; do not add redundant approval gates. Protect credentials, private records, and confidential audience results.

## Local checks

Install [requirements-dev.txt](requirements-dev.txt) into an isolated environment, then run:

```sh
python scripts/validate.py
python -m unittest discover -s tests
```

The repository validator checks the chosen ASCII naming subset, metadata, local file links, standalone package boundaries, plugin discovery, version consistency, README inventory, and scenario coverage. It is not an official certification or a full Markdown linter.

For official format validation, use the [Agent Skills reference library](https://github.com/agentskills/agentskills/tree/main/skills-ref) in an isolated environment and run `skills-ref validate .agents/skills/<name>` for each changed skill. Pin the reviewed upstream commit when installing from source and record it in review notes. The reference tool requires Python 3.11 or later. It is not a runtime dependency of these skills.

If you have a compatible Claude Code CLI, run both `claude plugin validate .claude-plugin/plugin.json` and `claude plugin validate .claude-plugin/marketplace.json`. The [official plugin reference](https://code.claude.com/docs/en/plugins-reference) documents the custom `skills` path. Host validation and skill-format validation answer different questions.

## Behavioral review

Use [evals/scenarios.json](evals/scenarios.json). For each changed skill:

1. Start a fresh host context with only the relevant skill and its bundled files. Supply the scenario prompt and any fixture described by the scenario.
2. Capture which skill was selected, the output, tool actions, and unavailable capabilities. Do not give the model the expected criteria as hidden extra instructions.
3. Judge every positive criterion and every prohibited behavior. Mark a criterion pass, fail, or not observable with a short reason.
4. Include a neighboring task to check over-triggering, a sparse-context request, and an evidence-gap or permission boundary. Repeat for both product classes where the task spans both.
5. Report structural checks, manual inspection, and actual host runs separately. Do not describe a written scenario or static coverage check as a completed model test.

Add cases for regressions and meaningful new behavior. Avoid tests that only assert that a particular sentence appears in a prompt. Useful failures include a public-only audit pretending it executed a task, a sample counted as real activation, and a draft campaign spending money.

## Pull requests

Explain the task and before/after behavior, affected skills, evidence or example provenance, validation performed, actual behavioral runs if any, and remaining limitations. Update the README inventory and changelog for new skills. Keep plugin and skill versions consistent for a release. Do not commit local settings, credentials, user outputs, or private research.
