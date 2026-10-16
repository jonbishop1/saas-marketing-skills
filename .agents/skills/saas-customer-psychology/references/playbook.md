# Barrier-to-proof worksheet

| Observed behavior | Hypothesis | Useful proof | Disconfirming signal |
| --- | --- | --- | --- |
| Engineers run locally but do not connect a service | Deployment ownership is unclear | Integration boundary, rollback steps, owner checklist | Users report no recurring need |
| Data team completes a demo but will not connect a warehouse | Credentials or data scope is unacceptable | Least-privilege setup and approved evaluation slice | Authorized users still cannot reconcile results |

## Decision handoff

Write a short memo: task / demonstrated result / unresolved risk / responsible owner / reversible next step / expected cost / stop condition.

## Ethical copy example

Prefer “Test with a local sample before connecting a service; this path does not establish production readiness” over “Your competitors are already ahead.” The former answers a real evaluation question and states its limits.
