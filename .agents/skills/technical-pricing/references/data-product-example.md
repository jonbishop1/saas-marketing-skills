# Completed fictional example

Facts: one million source rows, 5% change daily; scanned bytes, compute, retries and egress unknown.

50,000 changed rows/day is an illustrative daily activity estimate if the percentage means distinct changed rows per day. Over 30 days this is 1.5 million change occurrences, not necessarily 1.5 million distinct source rows. It does not establish billed bytes, repeated writes, or cost.

Compare a workspace base plus explicit workload allowance, changed-record meter, and measured compute/scan meter. Recommend testing the base-plus-allowance hypothesis for predictability; define retries, failed jobs, alerts and hard caps as proposed terms. First measure actual billed resources and customer budget fit. Do not mix a separate developer workload's CI identities into this product or invent a validated price.
