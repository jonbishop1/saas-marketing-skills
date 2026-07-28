# Marketing Planning Frameworks

Templates, phasing frameworks, and coordination systems for building and executing a marketing plan. Referenced when building an actual plan or reviewing quarterly strategy.

---

## Table of Contents

1. [Planning Templates by Tier](#planning-templates-by-tier)
2. [Projections — Working Backward from Goals](#projections--working-backward-from-goals)
3. [Phasing Frameworks](#phasing-frameworks)
4. [Multi-Channel Coordination](#multi-channel-coordination)
5. [Review and Adjustment Cadence](#review-and-adjustment-cadence)

---

## Planning Templates by Tier

### One-Page Marketing Plan (Tier 1)

For founders with one channel and minimal time. Fill this out once, revisit monthly.

```
WHO: [1-sentence ICP description]
PROBLEM: [in their words, from audience research]
CHANNEL: [the ONE channel you're focusing on]
MESSAGE: [1-sentence value prop in the audience's language]
GOAL: [specific metric — e.g., 20 signups this month]
WEEKLY ACTIONS:
  1. [specific repeatable activity — e.g., "publish 1 blog post"]
  2. [specific repeatable activity — e.g., "answer 5 questions on Reddit"]
  3. [specific repeatable activity — e.g., "share post in 2 communities"]
MEASUREMENT: [how you'll know if it's working — what metric, checked when]
REVIEW DATE: [when you'll evaluate and decide to continue or pivot]
```

**Example — API monitoring product, Tier 1:**
```
WHO: Backend developers at 10-50 person startups
PROBLEM: "I need to know when my API is slow before customers notice"
CHANNEL: Reddit + Hacker News (community)
MESSAGE: Simple API monitoring with alerts that don't drown you in noise
GOAL: 30 signups this month
WEEKLY ACTIONS:
  1. Answer 5 monitoring/DevOps questions on r/devops and r/sre
  2. Write 1 technical post for our blog (share in communities)
  3. Engage in 2 relevant HN threads
MEASUREMENT: Weekly signups from community referral traffic (GA4)
REVIEW DATE: End of month — if < 10 signups, reassess messaging before switching channels
```

**Example — SEO keyword research tool, Tier 1:**
```
WHO: Freelance SEO consultants and small agency owners
PROBLEM: "I need to find low-competition keywords without paying $99/month"
CHANNEL: Content / SEO
MESSAGE: Keyword research that's simple, accurate, and affordable
GOAL: 20 signups this month
WEEKLY ACTIONS:
  1. Publish 1 SEO-focused blog post targeting a long-tail keyword
  2. Share in r/SEO and 1 Facebook SEO group
  3. Answer 3 keyword-related questions on Reddit or forums
MEASUREMENT: Organic traffic growth + signups attributed to blog (GA4)
REVIEW DATE: End of month 3 — SEO needs 3 months to evaluate fairly
```

### Quarterly Marketing Plan (Tier 2)

For founders with 1–2 channels producing results and modest resources. Built at the start of each quarter, reviewed monthly.

```
QUARTER: [Q1/Q2/Q3/Q4 YYYY]

SITUATION SUMMARY:
  Current MRR: $
  Current signups/month: [number] from [channels]
  Current CAC: $ (or "unmeasured" — that's an action item)
  Biggest growth bottleneck: [one sentence]

GOALS:
  Primary: [e.g., 100 new signups at < $200 CAC]
  Secondary: [e.g., grow email list to 500 subscribers]
  Experiment: [e.g., test YouTube with 4 videos]

CHANNEL PLAN:
  Primary channel: [name]
    Budget: $ / Time: hrs/week / Owner: [person]
    Goal: [specific target — e.g., 70 signups]
    Key activities: [2-3 specific recurring activities]

  Supporting channel: [name]
    Budget: $ / Time: hrs/week / Owner: [person]
    Goal: [specific target — e.g., 20 signups]
    Key activities: [2-3 specific recurring activities]

  Experiment: [name]
    Budget: $ / Time: hrs/week / Owner: [person]
    Goal: [what you're trying to learn, not a signup target]
    Success criteria: [what would make you continue this next quarter]

METRICS (tracked weekly):
  - Signups by channel
  - Activation rate by channel (route to saas-data-analysis if not set up)
  - CAC by channel
  - MRR

MONTHLY MILESTONES:
  Month 1: [specific deliverables and targets]
  Month 2: [specific deliverables and targets]
  Month 3: [specific deliverables and targets]

DECISION RULES:
  Continue channel if: [e.g., CAC < $200 and activation rate > 25%]
  Scale channel if: [e.g., CAC < $150 and we haven't hit audience ceiling]
  Kill channel if: [e.g., 3 months with < 5 signups despite consistent execution]
```

### 6-Month Marketing Plan (Tier 3)

For growth-stage companies with multiple channels, budget, and team members. Built every 6 months, adjusted quarterly. Six months is long enough to see compounding effects from organic channels and short enough to stay responsive to market changes.

```
6-MONTH GOALS:
  Revenue target: [MRR by end of period]
  Customer target: [new customers needed to hit revenue target]
  Required blended CAC: [total marketing budget / target customers]
  Required LTV:CAC ratio: [target — minimum 3:1]

CHANNEL PORTFOLIO:
  [For each active channel:]
  Channel: [name]
    Role: [acquisition / nurture / retention / brand]
    6-month budget: $
    Target new customers: [number]
    Target CAC: $
    Owner: [person or team]
    Key initiatives: [2-3 major projects for the period]

QUARTERLY THEMES:
  First quarter: [e.g., "scale Google Ads past $10K/mo, launch content program, hire writer"]
  Second quarter: [e.g., "evaluate second paid channel, optimize conversion, build partnerships"]

INFRASTRUCTURE INVESTMENTS:
  Analytics: [what to set up or upgrade — route to saas-data-analysis]
  Content: [hire writer? build editorial calendar? launch programmatic SEO?]
  Tools: [what to add — email platform, social scheduler, BI tool?]
  Team: [hire? contractor? agency? what roles?]

PROJECTIONS:
  Use the funnel projection model (see Projections section below) to validate
  that your channel portfolio can realistically produce the customer target.
  Attach the projection spreadsheet as a companion to this plan.

RISKS AND CONTINGENCIES:
  If primary paid channel CPA rises > 50%: [contingency — shift budget to X]
  If organic growth stalls: [contingency — invest in link building / paid promotion]
  If key hire doesn't work out: [contingency — contractor coverage]
```

---

## Projections — Working Backward from Goals

Most founders set goals ("I want 30 new customers this month") without calculating what that requires at the top of the funnel. Funnel math turns a customer goal into specific activity targets — how many impressions, clicks, signups, and activations each channel needs to produce.

This is where marketing planning meets reality. If you want 30 customers/month and your funnel converts at typical SaaS rates, you may need 30,000–100,000 impressions depending on the channel. Knowing this before you commit to a channel prevents the surprise of "we're doing everything right but only getting 3 customers."

### How Funnel Math Works

Every channel has a funnel with conversion rates at each step. Working backward from your customer goal reveals the required top-of-funnel volume.

```
Desired customers/month: 30
  ÷ Trial-to-paid conversion rate: 8%
= Required trial signups: 375
  ÷ Visitor-to-signup conversion rate: 3%
= Required website visitors: 12,500
  ÷ Click-through rate (from channel): 2%
= Required impressions: 625,000
```

If 625,000 impressions is unrealistic for your channel and budget, you either need a different channel, a higher conversion rate, or a lower customer target. Better to know this now than 3 months in.

### Build a Projection Spreadsheet

Use `saas-data-analysis` to build a spreadsheet that models your funnel for each channel. The spreadsheet should have:

**Input columns (one row per channel):**
- Channel name
- Monthly budget (for paid) or hours/week (for organic)
- Estimated impressions per month
- Estimated CTR (click-through rate)
- Estimated visitor-to-signup rate
- Estimated signup-to-activation rate
- Estimated activation-to-paid rate

**Calculated columns:**
- Clicks = impressions × CTR
- Signups = clicks × visitor-to-signup rate
- Activated users = signups × activation rate
- Customers = activated users × conversion rate
- CAC = budget / customers (for paid channels)

**Summary row:**
- Total customers across all channels
- Blended CAC
- Gap vs. customer target

Ask Claude to use `saas-data-analysis` to create this spreadsheet with your specific data. If you don't have your own conversion data yet, use the industry ranges below as starting estimates — then replace them with actuals as you collect data.

### Typical Conversion Ranges by Channel

These are ranges observed across SaaS products. Your numbers will vary based on product, audience, and execution quality. Use the midpoint as a starting estimate, then update with your actual data.

**Google Search Ads:**

| Funnel step | Low | Typical | High |
|---|---|---|---|
| Impressions → Clicks (CTR) | 2% | 4–6% | 10%+ |
| Clicks → Landing page visit | 90% | 95% | 98% |
| Landing page → Signup | 2% | 4–8% | 15% |
| Signup → Activation | 20% | 30–50% | 60%+ |
| Activation → Paid | 3% | 8–15% | 25% |

Example: 50,000 impressions → 2,500 clicks → 2,375 landing page visits → 120 signups → 48 activated → 6 customers. At $3 CPC, that's $7,500 spend for 6 customers = $1,250 CAC.

**Meta Ads (Facebook/Instagram):**

| Funnel step | Low | Typical | High |
|---|---|---|---|
| Impressions → Clicks (CTR) | 0.5% | 1–2% | 3%+ |
| Clicks → Landing page visit | 80% | 90% | 95% |
| Landing page → Signup | 1% | 3–5% | 10% |
| Signup → Activation | 15% | 25–40% | 50%+ |
| Activation → Paid | 2% | 5–10% | 20% |

Note: Meta CTR is lower than Search because you're interrupting, not capturing intent. Activation rates are typically lower because the audience is less qualified.

**Content / SEO (Organic):**

| Funnel step | Low | Typical | High |
|---|---|---|---|
| Impressions (in search results) → Clicks | 1% | 3–5% | 10%+ (position 1) |
| Clicks → Meaningful page engagement | 40% | 60–70% | 80%+ |
| Engaged visitors → Signup | 0.5% | 1–3% | 5% |
| Signup → Activation | 25% | 35–50% | 65%+ |
| Activation → Paid | 3% | 8–15% | 25% |

Note: SEO visitors often have higher activation and conversion rates than paid because they arrived with intent. But the impression-to-click rate depends heavily on ranking position.

**Reddit / Community (Organic):**

| Funnel step | Low | Typical | High |
|---|---|---|---|
| Post/comment views → Profile/link clicks | 0.5% | 1–3% | 5%+ |
| Link clicks → Signup | 2% | 5–10% | 15% |
| Signup → Activation | 20% | 30–45% | 60%+ |
| Activation → Paid | 3% | 5–12% | 20% |

Note: Community traffic is spiky and hard to project consistently. Use for directional planning, not precise forecasting.

**Email Marketing (to owned list):**

| Funnel step | Low | Typical | High |
|---|---|---|---|
| Emails sent → Opened | 15% | 25–35% | 50%+ |
| Opened → Clicked | 2% | 4–7% | 12%+ |
| Clicked → Signup/action | 5% | 10–20% | 30% |

Note: Email conversion depends entirely on list quality and relevance. A 500-person list of highly engaged users will outperform a 10,000-person list of cold subscribers.

**Product Hunt (one-off launch):**

| Funnel step | Low | Typical | High |
|---|---|---|---|
| PH page views | 500 | 2,000–5,000 | 10,000+ |
| Page views → Your site visit | 20% | 30–40% | 50%+ |
| Site visits → Signup | 3% | 5–10% | 15% |
| Signup → Activation | 10% | 20–30% | 40%+ |
| Activation → Paid | 2% | 3–8% | 15% |

Note: Product Hunt is a spike, not a sustained channel. Don't include it in monthly projections — model it as a one-time event.

### Running the Projection

**Step 1:** Set your monthly customer target. Be specific: "30 new paying customers per month."

**Step 2:** For each channel you're considering, fill in the spreadsheet using:
- Your actual conversion data (best) 
- Industry ranges above with the "Typical" column (good enough to start)
- The "Low" column if you're being conservative or your product is new

**Step 3:** Work backward from 30 customers. How many impressions does each channel need to produce? Is that realistic given your budget and effort level?

**Step 4:** Identify the bottleneck. Usually it's one of:
- Not enough top-of-funnel volume (need more impressions — more budget or more content)
- Poor landing page conversion (need better messaging or page design)
- Low activation rate (need better onboarding — route to `saas-data-analysis`)
- Low trial-to-paid (need better product-market fit or pricing)

**Step 5:** Update the spreadsheet monthly with actual data. Replace estimated ranges with your real conversion rates. The model gets more accurate over time.

**Example — API monitoring product, goal: 30 customers/month:**

| Channel | Budget | Impressions | Clicks | Signups | Activated | Customers |
|---|---|---|---|---|---|---|
| Google Ads | $5,000 | 40,000 | 2,000 | 100 | 40 | 5 |
| Content/SEO | $0 (time) | 80,000 | 3,200 | 64 | 26 | 3 |
| Community | $0 (time) | 20,000 | 400 | 28 | 11 | 1 |
| **Total** | **$5,000** | **140,000** | **5,600** | **192** | **77** | **9** |

This projection shows 9 customers — well short of the 30 target. Options: increase Google Ads budget (but check if CPA stays viable at higher spend), invest in content for 3–6 months to grow organic traffic, or improve activation rate (the biggest leverage point — going from 40% to 60% activation gets you from 9 to 13 customers with the same traffic).

**Example — SEO keyword research tool, goal: 30 customers/month:**

| Channel | Budget | Impressions | Clicks | Signups | Activated | Customers |
|---|---|---|---|---|---|---|
| Google Ads | $3,000 | 30,000 | 1,500 | 90 | 45 | 5 |
| Content/SEO | $0 (time) | 150,000 | 6,000 | 90 | 45 | 5 |
| Email nurture | $0 | — | — | 20 (from list) | 12 | 2 |
| **Total** | **$3,000** | **180,000** | **7,500** | **200** | **102** | **12** |

Again short. But the projection reveals that content/SEO at 150K impressions is producing the same number of customers as $3K in ads — and it'll grow. The 6-month plan should invest heavily in content while maintaining ads for immediate volume.

---

## Phasing Frameworks

### Pre-Launch (1–4 Weeks)

The plan is: launch. Marketing supports launch, it doesn't delay it.

```
Week 1–2:
  - Landing page with clear value prop + email capture
  - Set up GA4 (10 minutes — route to saas-data-analysis)
  - Identify 3–5 communities where audience gathers

Week 3–4:
  - Launch. Share simultaneously across:
    * Product Hunt (if applicable)
    * Hacker News ("Show HN" post)
    * 2–3 relevant communities (Reddit, Slack, Discord, forums)
    * Your social accounts
    * Email to anyone who signed up for the waitlist
  - Respond to every comment and message. Be present.
  - Capture feedback voraciously — this informs all future marketing.
```

**What NOT to do pre-launch:**
- Build a content strategy or editorial calendar
- Set up email nurture sequences
- Run paid ads
- Obsess over branding or design perfection
- Spend more than 2 weeks on the landing page

### First 90 Days Post-Launch

```
MONTH 1 — Find one channel

  Week 1: Pick one channel based on your strengths, audience, and product type
           (use the Channel Selection Framework in SKILL.md)
  Week 2: Start executing — 2-3 activities per week minimum
  Week 3: Continue executing. Don't judge results yet.
  Week 4: First evaluation:
           - Any signal? (signups, engagement, conversations — not revenue yet)
           - If yes: continue into month 2
           - If zero signal: check messaging first, then channel fit

MONTH 2 — Double down or pivot

  If signal exists:
    - Increase effort on the channel
    - Start measuring quality: are signups activating? (route to saas-data-analysis)
    - Talk to 5 users who came through this channel — what resonated?
    - Refine messaging based on what you learn

  If no signal after messaging check:
    - Try a different channel
    - Don't try three channels — try ONE different channel
    - Give it 3-4 weeks before judging

MONTH 3 — Add measurement + second channel

  - Set up proper analytics if you haven't (route to saas-data-analysis)
  - Add one supporting channel that compounds the primary
  - Start monthly review cadence (see below)
  - By end of month 3 you should be able to answer:
    "Which channel produces signups, and do those signups activate?"
```

### Growth Phase: Quarterly Cycles

Once you have a working channel, marketing shifts from exploration to optimization.

```
QUARTERLY CYCLE:

  Review (week 1):
    - Pull data: signups, activation, CAC, revenue by channel
    - What worked? What didn't? What surprised you?
    - Where are you spending time/money vs. where results come from?
    - Is each channel trending in the right direction?

  Plan (week 2):
    - Fill in the Quarterly Marketing Plan template
    - Set channel-level goals proportional to performance
    - Pick ONE experiment for the quarter (new channel or new approach)
    - Identify one thing to stop doing (this is as important as what you start)

  Execute (weeks 3–12):
    - Follow the plan
    - Monthly check-ins: on track or need adjustment?
    - Don't change strategy mid-quarter unless data is dramatically different from expectations
    - Document learnings as you go — they feed the next quarterly review
```

---

## Multi-Channel Coordination

### Channel Roles

At Tier 3, channels work together as a system. Each channel has a role.

| Role | Purpose | Example channels |
|---|---|---|
| **Acquisition** | Bring new users into the funnel | SEO, Google Ads, Meta Ads, social, community, partnerships |
| **Nurture** | Warm up leads who aren't ready to buy | Email sequences, retargeting ads, educational content |
| **Conversion** | Turn warm leads into customers | Landing pages, demos, trials, bottom-funnel content, sales |
| **Retention** | Keep customers and expand revenue | Email, in-app messaging, community, product updates |
| **Brand** | Build long-term awareness and trust | Social media, content, PR, events, thought leadership |

**Tier 1:** Everything is Acquisition. That's fine.
**Tier 2:** Add Nurture (email) alongside Acquisition.
**Tier 3:** All five roles should have at least one channel.

Most early-stage founders try to fill all five roles too early. If you have < 1,000 users, Acquisition is what matters. Nurture and Conversion start mattering around 1,000 users. Retention matters when churn threatens growth. Brand is a luxury — invest only after product-market fit is solid.

### Content Repurposing Loop

One source piece can feed every channel. This is the highest-leverage content strategy for a time-constrained founder.

```
Source: Blog post (primary content investment)

Derivatives:
  → Twitter/X thread (extract the 5 sharpest insights, post as numbered thread)
  → LinkedIn post (professional angle, add 1-2 paragraphs of context and opinion)
  → Newsletter email (send to subscribers with personal commentary)
  → Reddit comment (save the URL — when someone asks the question your post answers, share it)
  → YouTube video (record yourself walking through the post's content with screen share)
  → Podcast talking point (reference the post's data or conclusions in your next guest appearance)
  → Social proof snippet (if the post includes customer data, extract as a standalone graphic)
```

This isn't blasting the same thing everywhere — each platform has different format expectations. A 2,000-word blog post becomes a 280-character tweet by extracting the sharpest single insight. It becomes a 10-minute video by adding visual demonstration. It becomes a LinkedIn post by framing it as a professional lesson learned.

**Practical schedule for repurposing one blog post:**

| Day | Activity | Time |
|---|---|---|
| Monday | Publish blog post | (writing done prior) |
| Monday | Post Twitter thread + LinkedIn post | 30 min |
| Tuesday | Send newsletter with post link + commentary | 20 min |
| Wednesday | Share in 1–2 relevant communities where post answers a real question | 15 min |
| Thursday | Record quick video walkthrough (optional) | 1–2 hrs |
| Ongoing | Reference post in community answers and podcast appearances | 0 min (part of normal activity) |

### Cross-Channel Attribution

When running multiple channels, you need to know which channels produce results. This is harder than it sounds because users interact with multiple channels before converting.

**Minimum viable attribution (Tier 2):**
UTM parameters on every link + first-touch and last-touch capture on signup. Route to `saas-data-analysis` for implementation.

**What you'll discover:** Most channels contribute to conversion but few are the final step. A user might discover you on Reddit, read your blog a week later via Google, and sign up after clicking a retargeting ad. Which channel gets credit? At Tier 2, use first-touch attribution (credit the channel that introduced them). It's imperfect but simple and directionally useful.

**Full attribution (Tier 3):** Multi-touch attribution models in your data warehouse. This requires significant analytics infrastructure. Don't build this until you're spending $10K+/month on marketing and need to optimize allocation across 4+ channels.

---

## Review and Adjustment Cadence

### Weekly (15 minutes)

Glance at the numbers. Don't analyze deeply — just check for anomalies.

- Signups this week vs. last week (up, down, flat?)
- Any channel producing zero results? (might indicate a broken link, paused ad, or platform issue)
- Any channel producing unusual results? (viral post? algorithm change? ad overspend?)

### Monthly (1 hour)

Proper review of channel performance.

- Signups by channel — which channels grew, shrank, or stayed flat?
- Activation rate by channel — is channel quality holding steady?
- CAC by channel (if running paid) — trending up or down?
- MRR change — net growth?
- One thing to adjust for next month

### Quarterly (half day)

Full strategic review. Use the Quarterly Plan template above.

- Channel-level performance vs. goals
- Budget reallocation based on performance
- Experiment results — promote to regular channel, extend experiment, or kill?
- Updated plan for next quarter

### Semi-Annually (half day)

Step back from tactics and evaluate the marketing strategy holistically. This is when you build the next 6-month plan.

- Which channels are producing the best customers (not just the most)?
- What's the LTV:CAC ratio by channel?
- Are we investing proportionally to results?
- Do projections still hold? Update the funnel model with actual data.
- What should we start, stop, and continue in the next 6 months?
- What infrastructure or team investments would unlock the next level?
