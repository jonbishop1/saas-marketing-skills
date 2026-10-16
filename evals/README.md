# Evaluation status

Scenario coverage and package validity are static checks, not behavioral pass rates.

## Behavioral repair candidate

The revised instructions were exercised in actual Claude Code CLI sessions using fictional products and Read/Skill tools only, with no browser, messaging, spending, or production tools. The configured model reported `claude-sonnet-5` in Claude Code 2.1.222. Global host context was still visible, so these were fresh conversations rather than clean-room evaluations. No cross-model performance claim is made.

Several candidate revisions improved cohort arithmetic, synthetic-first evaluation, and conditional launch decisions. Later runs still produced unsupported copy, mixed separate pricing workloads, and sometimes changed evidence status. A model-written Skill invocation summary was observed changing the original brief before the skill loaded; the candidate now explicitly addresses that evidence boundary. These are unresolved behavior defects, not package-validation failures.

The latest behavioral batch stopped after the existing Claude subscription reached its session limit. Ten of its first twelve attempts returned model answers; two were limit errors. The remaining scenarios were not executed for that snapshot. Transport success is not a quality pass. Earlier iterations and different snapshots must not be pooled as a final-release pass rate.

Raw traces and detailed judgments remain private because they include host context. The candidate is held for further validation; this file does not certify it for publication or live execution.

## Reproduce selected cases

With an authenticated Claude Code CLI, choose explicit IDs from `scenarios.json` and a new private output directory outside this repository:

```sh
python scripts/run_behavior.py --help
```

Pass the chosen IDs with `--ids` and a new directory with `--output`. The runner uses the configured model/account, read-only tool access, an empty MCP configuration, fresh conversations, per-run time/cost-equivalent bounds, and stops on host failure. Keep results outside the publishable checkout. Review each output against its original prompt and criteria; inspect the actual loaded entrypoint and invocation arguments when diagnosing errors. The runner deliberately records quality as unreviewed.

Installing through a different host or directly loading a skill requires its own evaluation. Authored scenarios are reusable test inputs, not promises that every supported host produces a correct answer.
