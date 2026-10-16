# Evaluation charter

Decision / roles and owner / baseline / dataset provenance and permission / workload / environment / versions / success criteria / tolerances / cost cap / stop conditions / cleanup.

## Example correctness plan

For a fictional incremental ingestion product, compare expected keys and values after an initial load, insert, update, delete if supported, and a late arrival. Define what happens when the schema changes or a run is interrupted. State unsupported semantics rather than silently omitting them.

## Results table

Criterion / agreed or proposed threshold / method / baseline result / product result / uncertainty / status / evidence. If execution has not happened, leave results blank and label the artifact a plan.

## Decision memo

Summarize demonstrated value, untested production requirements, owner effort, expected cost at the observed workload, and the smallest next step. Include a no-go option when correctness, permissions, or economics do not fit.
