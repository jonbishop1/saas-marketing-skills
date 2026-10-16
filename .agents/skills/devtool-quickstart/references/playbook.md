# Quickstart contract

Task / product version / runtime / permissions / data / cost envelope / commands / expected result / success assertion / recovery / cleanup / next task.

## Failure table

| Symptom | Check | Recovery |
| --- | --- | --- |
| Authentication rejected | Credential source, scope, endpoint | Correct approved scope; never paste secret into report |
| Empty result | Sample loaded, filter, expected input | Compare with documented fixture and invariants |
| Unexpected spend | Resources, run count, usage limits | Stop the authorized test and inspect cost before retrying |

## Fictional examples

A replay quickstart passes when the expected local response is reproduced from a sanitized fixture. An ingestion quickstart passes when the destination matches the expected keys and values, including one documented update case. Both need a cleanup path; neither result alone establishes real-workload readiness.
