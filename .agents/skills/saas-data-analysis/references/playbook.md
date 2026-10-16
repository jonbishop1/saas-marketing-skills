# Metric contract

Name / entity / numerator / eligible denominator / cohort start / observation window / success event / deduplication / exclusions / sample or real / assisted or independent / missing-data rule.

## Worked arithmetic: illustrative data

Of 40 eligible workspaces with a full observation window, 12 completed a real-data reconciliation: 30%. Another 8 completed only a sample. Report sample success separately; combining them would describe a different metric. These counts are illustrative, not a benchmark.

## Event record

event_name, occurred_at, anonymous_or_user_id where permitted, project_id, workspace_id, account_id if known, environment, task, outcome, sample_flag, assistance_flag, source, schema_version. Collect only what the actual decision requires and is permitted.

## Interpretation

If paid traffic has lower activation but includes more early cohorts with incomplete windows, compare eligible cohorts first. If sales-assisted accounts activate more often, account selection and support effort may explain the difference; do not attribute it entirely to the channel.
