# Completed fictional example

Facts: local CLI; pricing/license unknown; five humans, three CI identities; 50,000 manual and 700,000 automated requests/month. Vendor cost and willingness to pay unknown.

| Proposed meter | Illustrative quantity | Main tradeoff |
| --- | --- | --- |
| Human seats | 5, if CI identities excluded | Predictable; identify who needs a license |
| All identities | 8, if all billable | Could penalize automation identities; terms unvalidated |
| Requests | 750,000/month | Scales with CI activity; needs spend predictability |
| Team license | 1 team, proposed boundary | Predictable automation access; test team/value definition |

Automation is 700,000/750,000 = 93.3% of requests. Doubling CI requests leaves five human seats and raises requests to 1.45 million. Local customer CPU is not evidence of vendor compute cost. Recommendation: research a team license with an explicit proposed CI entitlement versus human seats; interview budget owners before choosing price. A hosted service is unnecessary for either proposal. This does not assert current packages or license rights.
