---
name: saas-google-ads
description: >
  Comprehensive Google Ads guide for developers and technical founders running paid search for web-first software products: SaaS, developer tools/APIs, and enterprise software. Use this skill for any question about Google Ads, paid search, PPC, search campaigns, conversion tracking, Google Tag Manager, keyword research, Quality Score, bidding strategy, ROAS, CAC, attribution, campaign structure, ad copy, landing pages, or scaling paid acquisition. Trigger whenever a user asks about acquiring users or customers through Google, setting up or troubleshooting campaigns, or measuring ad performance for a software product.
---
 
# Google Ads for Software Products
 
Audience: developers and technical founders. Explain things in engineering terms. Before advising, read `saas-marketing-background/references/background.md` and gather missing background.
 
---
 
## Google Ads — Additional Intake Questions
 
After gathering shared background, also ask these channel-specific questions:
 
**Keywords**
- High-intent terms they're confident about?
- Competitors users might also be evaluating?
- Terms that look relevant but attract the wrong audience?
- What would they search for? (symptoms, tools they use today, category terms)
 
**Google Ads current state**
- Ran Google Search Ads before? What worked/didn't?
- Conversion tracking set up and verified?
 
**Google Ads safe defaults (don't ask, just apply):**
 
| Parameter | Default |
|---|---|
| Device | All; -20–30% mobile for B2B |
| Ad schedule | All hours; business hours only for sales-led |
| Budget sizing | Target CPA × 3 minimum daily per campaign |
| Target CPA | Unknown — run Maximize Conversions until baseline established |
| Match types | Phrase + Exact to start; no Broad until 30+ conv/month |
 
**Channel-specific routing:**
 
| Situation | Where to go |
|---|---|
| No tracking set up | Set up tracking in `guide.md` → Conversion Tracking before anything else |
| Tracking set up, no campaigns | Account setup below → keywords/ads/bidding in `guide.md` |
| Campaigns running, underperforming | Verify tracking first (guide.md → Tracking) then Optimization section |
| Campaigns profitable, want to scale | guide.md → Scaling |
 
---
 
## How Google Search Ads Work
 
A keyword is not just a search term — it's a signal of buyer intent. The same concept ("api monitoring") searched different ways signals different stages of the buying journey. Your job is to match your spend to the highest-intent signals first.
 
The auction pipeline:
```
User query → Auction → Ad Rank → Click → Landing page → Conversion
     ↑                                                        |
     └──────────── Feedback loop (conversion signal) ─────────┘
```
 
**Ad Rank** = bid × Quality Score × expected impact of assets. You don't win by bidding highest — you win by having the highest Ad Rank, which means Quality Score is a cost multiplier. Improving QS lowers CPC without touching your bid.
 
**What Google doesn't tell you:** Google's revenue comes partly from inefficiency. Their automated suggestions (broad match expansion, Performance Max, auto-applied recommendations) often increase spend before they improve results. Treat account suggestions as hypotheses to test, not instructions to follow. The default campaign settings are not optimized for your goals — they're optimized for Google's revenue.
 
**Why search works for software:** Search captures demand that already exists. A user searching "rest api rate limiting library" has identified their problem and is actively looking for a solution. That query may have 200 searches/month globally, but the buyer intent is extremely high. This is fundamentally different from social ads, which interrupt people who weren't looking.
 
**When search doesn't work:** If your product category doesn't exist yet (common in AI), there may be no search volume for what you sell. In that case, you're educating the market — which search ads do poorly. Problem-aware keywords ("how to reduce api latency") can work, but expect lower conversion rates and higher CPAs.
 
---
 
## Is It Worth the Budget? Minimum Testing Formula
 
Before starting, determine if you have enough budget to get meaningful data:
 
```
Minimum monthly test budget = Target CPA × 50
 
Why 50: Smart bidding needs ~30 conversions/month to stabilize.
50 gives you headroom for learning period waste.
 
If you don't know your Target CPA yet:
  Estimate = LTV × acceptable CAC/LTV ratio
  Example: LTV $1,200, willing to spend 20% → Target CPA = $240
  Minimum budget = $240 × 50 = $12,000/month
 
Minimum daily budget per campaign = Target CPA × 3
Below this, smart bidding has too little signal per day to work.
```
 
If your budget is below this threshold, use Manual CPC and accept slower optimization — don't use smart bidding without the data to support it.
 
---
 
## Account Structure
 
```
Account
└── Campaign  (budget, network, bidding strategy, goal)
    └── Ad Group  (keyword theme + bid modifier)
        ├── Keywords
        └── Ads
```
 
**Campaign types for software (in order of when to add them):**
 
| Type | When to use |
|---|---|
| Search | Always — start here exclusively |
| Display | Retargeting only, once you have converters to exclude/target |
| Demand Gen | Top-of-funnel awareness once Search is profitable |
| Performance Max | Only after 50+ conversions/month and solid tracking |
 
**Campaign structure by intent — not by internal org or budget cycle:**
 
```
Brand           → your product name + brand + pricing
Competitor      → named competitors users are evaluating
Category        → solution-aware ("api monitoring tool")
Problem-aware   → symptom-aware ("api keeps going down")
Feature-specific → exact feature searches ("webhook retry logic")
```
 
Keep Brand separate always — brand terms have low CPA and will consume budget from non-brand if mixed.
 
---
 
## Goals and Conversion Hierarchy
 
Set one primary conversion per campaign. Multiple primary conversions give the bidding algorithm conflicting signals.
 
```
Primary (bid on — pick ONE):
  PLG/SaaS:       free trial signup OR account creation
  Sales-led:      demo request OR contact sales form
  Dev tools:      API key created OR SDK first call
  Enterprise:     qualified demo booked OR MQL form
 
Secondary (track, don't bid on):
  - Demo video played
  - Pricing page visit > 30s
  - Docs page visit
  - Chatbot started
 
Micro (track for funnel visibility):
  - Blog post read > 60s
  - Newsletter signup
  - Any page view
```
 
---
 
## Campaign Settings — What to Change from Defaults
 
**Networks:** Uncheck Search Partners and Display Network. These are separate products bundled into Search by default. They dilute data and are harder to audit.
 
**Location:** Set explicitly. Default is "Presence or interest" — change to "Presence" only, or you'll show ads to people researching your target location from elsewhere.
 
**Ad rotation:** Set to "Do not optimize" while testing copy. Switch to "Optimize" once you have a winning variant.
 
**Ad schedule:** For B2B/enterprise, restrict to business hours. For PLG/dev tools with global self-serve buyers, leave all hours.
 
**Device bid adjustments:** For enterprise B2B, apply -20–30% on mobile — mobile rarely converts for high-consideration software purchases.
 
---
 
## Naming Conventions
 
Consistent naming makes filtering, reporting, and auditing faster at scale.
 
```
Campaigns:  [Type]_[Intent/Audience]_[Offer]_[YYYY-MM]
            Search_Competitor_FreeTrial_2024-03
            Search_Brand_Demo_2024-03
 
Ad Groups:  [Theme]_[MatchType]
            APIMonitoring_Exact
            ChurnReduction_Phrase
 
Ads:        [Angle]_[CTA]_v[N]
            ProblemHook_StartTrial_v1
            SocialProof_BookDemo_v2
```
 
---
 
## Pre-Launch Checklist
 
**Tracking (do not skip)**
- [ ] Conversion tracking configured and verified with a real test event
- [ ] Auto-tagging enabled
- [ ] GA4 linked; audiences available in Google Ads
- [ ] Cross-domain tracking set up if funnel spans subdomains
- [ ] UTM tracking template set at account level
 
**Audiences**
- [ ] Remarketing audiences created: all visitors (180d), pricing/demo page visitors, converters
- [ ] Converters excluded from prospecting campaigns
- [ ] Customer Match list uploaded if available
 
**Campaigns**
- [ ] Negative keyword list created and applied
- [ ] Location targeting explicitly set
- [ ] Language matches landing page language
- [ ] Brand campaign live (even low-budget — protects brand terms)
- [ ] Brand terms in negatives on all non-brand campaigns
- [ ] Ad schedule configured for audience type
- [ ] Daily budget = Target CPA × 3 minimum
 
**Creative**
- [ ] Landing pages < 3s load (check PageSpeed Insights)
- [ ] Landing pages mobile-responsive
- [ ] Single CTA above the fold matching the ad's promise
- [ ] All asset types added (sitelinks, callouts, structured snippets)
 
**Team**
- [ ] Reporting view configured
- [ ] Relevant team notified (paid traffic spikes inbound volume)
 
---
 
## Key Metrics Reference
 
| Metric | Formula | Alert threshold |
|---|---|---|
| CTR | clicks / impressions | < 2% brand, < 1% non-brand |
| CPC | spend / clicks | Rising without CVR improvement |
| CVR | conversions / clicks | Drop > 20% week-over-week |
| CPA | spend / conversions | Exceeds target × 1.5 for 2+ weeks |
| ROAS | revenue / spend | Below target for 2+ weeks |
| Quality Score | Google's 1–10 rating | Any keyword < 6 needs investigation |
| Impression Share | your impressions / available impressions | < 50% on core terms with budget headroom |
 
**SaaS-specific KPIs:**
 
| Product type | Primary KPI | Typical range |
|---|---|---|
| PLG / SaaS trial | Cost per trial | $50–$300 |
| Sales-led / demo | Cost per demo | $200–$2,000 |
| Dev tools / API | Cost per signup | $30–$150 |
| Enterprise | Cost per MQL | $300–$3,000 |
 
---
 
## Reference Files
 
- `saas-marketing-background/references/background.md` — shared intake questions; read before advising
- `references/guide.md` — complete reference: keywords, ads, tracking, bidding, audiences, optimization, scaling
 
