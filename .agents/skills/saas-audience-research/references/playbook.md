# Research worksheet

Record one row per observation: source / task / environment / trigger / workaround / consequence / user role / buying authority / limitation / confidence.

## Interview prompts

- Tell me about the last time this happened. What were you trying to deliver?
- Show or describe the workaround. Who maintained it and what failed?
- What have you tried? Why did you stop or keep using it?
- What would prevent you from testing another option this week?
- Who approves the data, deployment, or purchase? What evidence do they need?

## Segment comparison

| Candidate | Repeated task | Trigger | Can evaluate? | Blocking constraint | Evidence against fit |
| --- | --- | --- | --- | --- | --- |
| Backend platform team | Reproduce service failures | Incident review | Local sanitized trace | No external payload upload | Existing internal tooling may suffice |
| Analytics engineering team | Reconcile late-arriving records | Broken downstream report | Approved historical slice | Connector and warehouse access | Infrequent changes may not justify migration |

These are fictional hypotheses. Validate them against the product's actual users and supported environments. Choose one research method because it resolves a decision, not because a fixed number of interviews or comments has been reached.
