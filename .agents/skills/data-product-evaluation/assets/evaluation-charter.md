# Data-product evaluation charter

Status: proposed plan / agreed plan / executed evaluation. Choose the actual state.

## Decision and people

- Decision this evaluation supports:
- Business task and current alternative:
- Evaluator, technical owner, approver, and reviewer:
- Proposed or agreed scope and criteria:

## Authorized environment

- Data provenance, permission, and sensitivity:
- Source, destination, schema, volume, skew, and update patterns:
- Deployment, versions, configuration, and baseline:
- Credential scope and owner; never include secret values:
- Cost ceiling, stop conditions, retention, cleanup owner:
- What this sample cannot establish:

## Criteria and result ledger

| Criterion | Method and expected invariant | Threshold and who agreed it | Baseline | Product result | Evidence | Status and limitation |
| --- | --- | --- | --- | --- | --- | --- |
| Initial correctness | Reconcile approved keys and values | | | | | |
| Incremental changes | Inserts, updates, deletes if supported | | | | | |
| Late arrivals | Defined arrival and event-time cases | | | | | |
| Recovery | Interrupted run and safe resumption | | | | | |
| Performance | Stated freshness/latency/throughput method | | | | | |
| Cost and operation | Actual resources, effort, and limits | | | | | |

Use pass / partial / fail / unknown only with a reason. Mark not-applicable criteria explicitly. Empty result cells mean no result, not a pass.

## Decision memo

- Demonstrated value and conditions:
- Failures, deviations, and untested requirements:
- Operating and migration effort:
- Next bounded step, owner, and approval needed:
- Conditions for stopping or declining adoption:
