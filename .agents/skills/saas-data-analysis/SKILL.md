---
name: saas-data-analysis
description: >
  Comprehensive product and marketing analytics guide for developers and technical founders building SaaS products, developer tools/APIs, and enterprise software. Use this skill for any question about analytics setup, event tracking, conversion tracking, GA4, Google Tag Manager, Mixpanel, Amplitude, PostHog, Heap, Pendo, product metrics, marketing attribution, funnel analysis, cohort analysis, retention analysis, activation metrics, pirate metrics (AARRR), defining KPIs, building dashboards, connecting marketing data to product data, understanding which acquisition channels produce the best customers, or figuring out what to measure and how. Trigger whenever a user asks about setting up analytics, choosing analytics tools, understanding their metrics, tracking user behavior, measuring product-market fit, analyzing funnels, or any data-driven decision-making for a SaaS product — even if they just say "I don't know what to track" or "my analytics are a mess."
---

# SaaS Product & Marketing Analytics

Audience: developers and technical founders. Explain things in engineering terms. Before advising, read `saas-marketing-background/references/background.md` and gather missing background. Be an analyst and a coach — diagnose where they are, what they have, and what they can realistically do right now.

---

## Table of Contents

1. [Why This Matters](#why-analytics-matter)
2. [Situation Assessment](#situation-assessment)
3. [Three Tiers of Analytics](#three-tiers-of-analytics)
4. [Marketing Analytics](#marketing-analytics)
5. [Product Analytics](#product-analytics)
6. [Connecting Marketing to Product](#connecting-marketing-to-product)
7. [Key Metrics Framework](#key-metrics-framework)
8. [Session Recording — Light Touch](#session-recording--light-touch)
9. [Analytics by Product Stage](#analytics-by-product-stage)
10. [Reference Files](#reference-files)

---

## Why Analytics Matter

Most technical founders either track nothing or track everything. Both fail.

Tracking nothing means you're guessing — about which channels produce real customers, about where users drop off, about what features actually drive retention. Tracking everything means you drown in dashboards, spend time maintaining instrumentation instead of shipping product, and still can't answer the one question that matters: "Is what I'm doing working?"

Good analytics answer specific questions. The system exists to make decisions, not to produce charts.

**The marketing-to-product connection most founders miss:** Marketing analytics (GA4, UTMs, ad platforms) tell you where users come from. Product analytics (Mixpanel, Amplitude, PostHog) tell you what users do after they arrive. Most founders set these up as separate systems and never connect them. This means marketing optimizes for signups while product optimizes for engagement, and nobody knows which acquisition channels produce customers who actually stick around and pay. Connecting these two systems is one of the highest-leverage analytics investments you can make.

**Example — API monitoring product:**
GA4 shows strong signup rates from Hacker News posts. Mixpanel shows those users have 15% day-7 retention vs. 45% from Google Search. Without connecting these systems, you'd double down on HN content. With the connection, you'd realize HN drives tire-kickers while Search drives serious buyers, and reallocate accordingly.

**Example — SEO keyword research tool:**
GA4 shows paid ads convert at 4% to trial. Amplitude shows paid ad users activate (run their first keyword search) at 60%, while organic users activate at 85%. The paid funnel looks fine on the marketing side but underperforms on the product side — those users need different onboarding, or the ad copy is attracting the wrong people.

---

## Situation Assessment

Before recommending any analytics setup, assess where the founder actually is. Don't prescribe Amplitude with custom event taxonomies to someone with 12 users. Don't tell someone with 5,000 users they only need GA4.

### Questions to Evaluate

**Current analytics state:**
- What's installed today? (GA4, any product analytics, any tag manager?)
- Is anything actually tracked beyond pageviews?
- Do you have a defined set of key events? Or are you relying on auto-tracked/default data?
- Can you currently answer: "Which acquisition channel produces my best customers?"

**Technical context:**
- What's your stack? (SPA, server-rendered, mobile, API-only)
- Single domain or multi-subdomain? (app.product.com, docs.product.com, etc.)
- Do you have a backend that can send server-side events?
- Any privacy/compliance requirements? (GDPR, SOC2, HIPAA)

**Resources:**
- Time: How many hours/week can you spend on analytics? (1–2 hours is fine at Tier 1)
- Budget: Any budget for tools? ($0 is fine — PostHog and GA4 are free to start)
- Team: Just you, or is someone else looking at this data too?

**Product stage:**
- Pre-launch with no users
- Launched with < 100 users
- 100–1,000 users
- 1,000–10,000 users
- 10,000+ users

**What decisions are blocked right now?**
This is the most important question. Analytics exist to unblock decisions. If you can't name a specific decision you need data for, you're not ready for more instrumentation — you're ready to ship product and see what happens.

### Stage-Based Routing

| Stage | Analytics priority | Tool recommendation | Skip for now |
|---|---|---|---|
| Pre-launch | Don't set up analytics. Ship. | GA4 basic install only — 15 minutes | Product analytics, dashboards, funnels |
| < 100 users | Core event tracking, basic funnel | GA4 + PostHog free (or Mixpanel free) | Custom dashboards, cohort analysis, attribution modeling |
| 100–1,000 users | Activation + retention metrics, basic acquisition quality | GA4 + one product analytics tool, connect user IDs | Data warehouse, BI tools, advanced attribution |
| 1,000–10,000 | Full funnel instrumentation, marketing-to-product connection | GA4 + GTM + dedicated product analytics (Amplitude/Mixpanel/PostHog) | CDP, data warehouse (unless data volume requires it) |
| 10,000+ | Everything above + data infrastructure | Add Segment/Rudderstack, warehouse, BI layer | Nothing — you need the full stack |

---

## Three Tiers of Analytics

Tiers are cumulative. Tier 2 includes Tier 1. Start where you are.

### Tier 1 — Minimum Viable Analytics (Pre-launch to early, $0 budget, 1–2 hrs/week)

You have few or no users. Your priority is shipping product and getting signal on whether anyone cares. Don't build a data platform.

**What you set up:**
- GA4 on your marketing site and app (one property, basic install)
- 5–10 key events defined and tracked (see Key Metrics Framework below)
- UTM parameters on every link you share (social posts, emails, paid ads)
- One product analytics tool on the free tier (PostHog, Mixpanel, or Amplitude — see tool comparison in `references/guide.md`)

**What you can answer:**
- How many people visit, sign up, and come back
- Which traffic sources drive signups (at a basic level via UTMs)
- Where users drop out of your signup/onboarding flow
- Whether users are doing the core action your product exists for

**What you can't answer (and that's fine for now):**
- Which channels produce the highest-LTV customers
- Detailed cohort retention curves
- Statistical significance on anything
- Attribution beyond last-click

**Performance note:** Tier 1 gives you directionally useful signal. GA4's event data and a free product analytics tool are enough to catch major problems — a broken signup flow, a feature nobody uses, a traffic source that produces zero activations. You'll miss nuance (multi-touch attribution, segment-level retention differences), but nuance doesn't matter when you have 50 users.

**Example — API monitoring product at Tier 1:**
Track: `signed_up`, `api_key_created`, `first_alert_configured`, `first_alert_fired`, `upgraded_to_paid`. Put UTM tags on your Show HN post, your documentation links, and your Twitter bio link. That's it. You can now see your full funnel from visit → value delivered.

**Example — SEO keyword research tool at Tier 1:**
Track: `signed_up`, `first_keyword_search`, `saved_keyword_list`, `exported_report`, `upgraded_to_paid`. UTM tag your blog posts, Product Hunt listing, and any outreach links. You can now see which content drives users who actually use the product.

### Tier 2 — Connected Analytics (Launched, growing, small budget, 3–5 hrs/week)

You have users. You need to understand which are good customers and why, and connect acquisition data to product behavior.

**What you add to Tier 1:**
- Google Tag Manager for event management (stop hardcoding tracking calls)
- User identity stitching — connect the anonymous marketing visitor to the authenticated product user
- Property/trait enrichment on users (plan type, company size, signup source)
- Activation metric defined and tracked formally
- Basic retention analysis (weekly or monthly cohorts)
- Marketing-to-product connection (which UTM source → which activation rate → which retention rate)
- 15–25 key events with properties

**What you can answer:**
- Which acquisition channels produce users who activate and retain (not just sign up)
- Where in onboarding users get stuck, segmented by source or plan
- Whether your activation metric actually predicts retention
- Basic cohort retention — is it improving over time?

**What you can't answer:**
- Multi-touch attribution across long sales cycles
- Predictive analytics or propensity scoring
- Real-time operational dashboards
- Cross-platform journey stitching (web + mobile + API)

**Performance note:** Tier 2 is where analytics starts paying for itself. Connecting marketing and product data lets you cut wasted ad spend, fix onboarding for specific segments, and prove (or disprove) that a channel is working. The investment is moderate — a few hours setting up GTM and enriching your event stream — and the return is disproportionate.

### Tier 3 — Systematic Analytics (Growth stage, budget available, dedicated effort)

You have enough users and data that analysis becomes an ongoing function, not a periodic check-in.

**What you add to Tier 2:**
- Customer Data Platform (Segment or Rudderstack) for event routing
- Data warehouse (BigQuery, Snowflake, or Redshift) as the single source of truth
- BI layer (Metabase, Looker Studio, or Tableau) for self-serve dashboards
- Server-side event tracking for reliable data (not just client-side JS)
- Advanced segmentation and cohort analysis
- Revenue attribution across the full funnel
- Custom metrics and computed properties (LTV predictions, health scores)
- Automated alerting on metric changes

**Performance note:** Tier 3 is expensive — both in tools and in time to maintain. Most SaaS companies under $3M ARR don't need all of this. Build only the parts that answer questions blocking your growth. A data warehouse with no one querying it is a cost center, not an asset.

See `references/guide.md` → Data Infrastructure for implementation details on Tier 3 tools.

---

## Marketing Analytics

Marketing analytics answers: where do users come from, and how efficiently?

### GA4 — The Foundation

GA4 is free, required for Google Ads integration, and provides baseline web analytics. It is not a product analytics tool — don't try to make it one.

**What GA4 is good at:** Traffic analysis, acquisition channel attribution, marketing campaign measurement, ecommerce/conversion tracking, audience building for Google Ads, basic event tracking.

**What GA4 is bad at:** In-product user journey analysis, retention cohorts, real-time event debugging, individual user inspection, anything requiring user-level data exploration. Use a product analytics tool for these.

**Tier 1 GA4 setup (15 minutes):**
Install the GA4 tag. Set up 3–5 conversion events. Add UTM parameters to your links. Done. See `references/guide.md` → GA4 Setup for step-by-step.

**Tier 2 GA4 setup (1–2 hours):**
Move event management to GTM. Set up cross-domain tracking if you have multiple subdomains. Connect GA4 to Google Ads. Build 2–3 custom audiences. Configure data retention to 14 months.

**Tier 3 GA4 setup:**
BigQuery export for raw event data. Custom channel groupings. Offline conversion import from CRM. Attribution model comparison.

### Google Tag Manager (GTM)

GTM is a container that sits between your site and your analytics tools. Instead of hardcoding tracking calls in your codebase, you configure them in GTM's UI. This matters because:
- Marketing can add tracking without engineering deploys
- You can add/modify events without code changes
- One data layer feeds multiple tools (GA4, Mixpanel, ad pixels)
- You can test and debug events before publishing

**When to add GTM:** Tier 2 — when you have more than 5–10 events to manage, or when you're running paid ads that need conversion tracking. Don't bother with GTM for a basic Tier 1 setup — it's overhead that doesn't help yet.

See `references/guide.md` → GTM Setup for implementation patterns.

---

## Product Analytics

Product analytics answers: what do users do inside your product, and does it predict retention and revenue?

### Choosing a Tool

| Tool | Free tier | Best for | Hosted/Self-hosted | Key strength |
|---|---|---|---|---|
| **PostHog** | 1M events/mo | Startups wanting all-in-one, privacy-conscious | Both | Open source, self-hostable, includes session recording |
| **Mixpanel** | 20M events/mo | Event-driven products, SaaS with clear user flows | Hosted | Best-in-class funnel and retention analysis |
| **Amplitude** | 50K MTUs | Products needing behavioral cohorts, larger teams | Hosted | Strong for segmentation and behavioral analysis |
| **Heap** | 10K sessions/mo | Teams that want auto-capture without manual instrumentation | Hosted | Captures everything retroactively; low setup effort |
| **Pendo** | Free for < 500 MAUs | Product-led growth, in-app guides alongside analytics | Hosted | Combines analytics with in-app messaging |

**Tier 1 recommendation:** Pick one. PostHog if you value open source and want session recording included. Mixpanel if you want the strongest free tier for event analytics. Don't agonize — you can switch later when you're small.

**Tier 2 recommendation:** Commit to one tool. Invest in a proper event taxonomy (see `references/guide.md` → Event Taxonomy Design). Set up user identity and properties.

**Tier 3 recommendation:** Your product analytics tool becomes one node in a larger data stack, fed by a CDP and drained to a warehouse. The tool choice matters less because the warehouse becomes the source of truth.

**Performance note on "good enough":** Heap's auto-capture means you track everything with zero instrumentation effort. The tradeoff is messier data — auto-captured click events on "Button 3" aren't as useful as a deliberately defined `api_key_created` event. Heap is the fastest to set up (Tier 1 speed) but produces Tier 1 quality data even at scale. Manual instrumentation takes longer but produces cleaner signal. For most founders, 10 well-defined events beat 10,000 auto-captured ones.

---

## Connecting Marketing to Product

This is the section most analytics setups miss entirely. Marketing tools and product tools exist in separate universes unless you deliberately connect them. The connection is how you learn which channels produce good customers — not just customers.

### How the Connection Works

```
Anonymous visitor (GA4 client ID, UTM params)
        ↓ signs up
Authenticated user (your user ID)
        ↓ you stitch these identities
Product analytics links: user_123 came from utm_source=google, utm_medium=cpc
        ↓ now you can ask
"What's the activation rate of users from Google Ads vs. organic search?"
"What's the 30-day retention of users from Hacker News vs. Product Hunt?"
"What's the average revenue per user by acquisition channel?"
```

### Implementation by Tier

**Tier 1 — Manual, good enough:**
On signup, capture UTM parameters from the URL (or from a cookie you set on landing) and store them as user properties in your product analytics tool. Most product analytics tools have a `set` or `identify` call that lets you attach properties to a user.

```javascript
// On signup, after creating the user
analytics.identify(userId, {
  signup_source: getUtmSource(),      // from URL or cookie
  signup_medium: getUtmMedium(),
  signup_campaign: getUtmCampaign(),
  signup_landing_page: getLandingPage()
});
```

This is imperfect — you'll lose UTM data if the user visits multiple times before signing up, and you're only capturing last-touch. But it works and takes 30 minutes to implement.

**Tier 2 — First-touch + last-touch:**
Set a persistent cookie on first visit that captures UTM parameters. On signup, send both first-touch (the cookie) and last-touch (the current URL) as user properties. This gives you two attribution perspectives for free.

Also enrich user profiles with product data that marketing needs: plan type, activation status, MRR, account age. This lets you build segments like "users from Google Ads who activated and are on a paid plan" — the gold standard for acquisition quality analysis.

**Tier 3 — Full attribution via CDP:**
Route all events through Segment or Rudderstack. The CDP maintains identity resolution across touchpoints and can send enriched user profiles to both marketing tools (GA4, ad platforms) and product analytics tools. Server-side tracking ensures you don't lose events to ad blockers.

See `references/guide.md` → Marketing-Product Connection for implementation details.

**Example — API monitoring product:**
After connecting, you discover that users from DevOps-focused Reddit posts have 2x the activation rate of users from generic "monitoring" Google Ads. You shift ad spend to DevOps-specific keywords and write more Reddit content. Cost per activated user drops 40%.

**Example — SEO keyword research tool:**
After connecting, you find that users who arrive via blog posts about "long-tail keywords" have the highest 90-day retention. Users from "best SEO tools" comparison pages sign up at high rates but churn after the trial. You stop optimizing for the comparison traffic and double down on educational content.

---

## Key Metrics Framework

Don't track metrics because a blog post said to. Track metrics because they answer questions that drive decisions.

### The AARRR Framework Applied to SaaS

| Stage | What it measures | Key metric | Example (API product) | Example (SEO tool) |
|---|---|---|---|---|
| **Acquisition** | Are people finding you? | Visitors by channel | 2,000 monthly visitors, 40% from search | 5,000 monthly visitors, 60% from blog |
| **Activation** | Do they experience core value? | Activation rate | % who configure first alert within 7 days | % who run first keyword search within 3 days |
| **Retention** | Do they come back? | Week-1, Week-4 retention | 45% return in week 2 | 35% return in week 2 |
| **Revenue** | Do they pay? | Trial-to-paid conversion, MRR | 8% trial → paid at $49/mo | 5% trial → paid at $29/mo |
| **Referral** | Do they bring others? | Referral rate, viral coefficient | Team invites per account | Shared report links |

### Defining Your Activation Metric

The activation metric is the single most important product metric for early-stage SaaS. It's the action that predicts whether a new user will retain.

**How to find it:**
1. List the 3–5 actions a user must take to get value from your product
2. For each action, calculate retention rate for users who did it vs. didn't within the first 7 days
3. The action with the largest retention gap is your activation metric

**Tiered approach to finding activation:**

| Level | Method | Accuracy |
|---|---|---|
| Good | Intuition + basic data: pick the action that logically represents "got value," check if users who do it retain better | Directionally correct, good enough to start |
| Better | Correlation analysis: calculate retention rate by each candidate action, pick the strongest predictor | Statistically grounded |
| Best | Regression analysis: multivariate model to find which combination of actions best predicts 30/60/90-day retention | Precise, but needs 1,000+ users |

**Example — API monitoring product:**
Candidate activation events: `api_key_created`, `first_monitor_configured`, `first_alert_fired`. Analysis shows users who configure their first monitor within 3 days retain at 55% (week 4), vs. 12% for those who don't. Activation metric: first monitor configured within 3 days.

**Example — SEO keyword research tool:**
Candidates: `first_keyword_search`, `saved_keyword_list`, `exported_report`. Users who save a keyword list within 7 days retain at 40% vs. 10%. Activation metric: saved first keyword list within 7 days.

### Metrics to Track by Tier

**Tier 1 (5–10 events):**
- `page_viewed` (marketing site key pages: homepage, pricing, docs)
- `signed_up`
- `onboarding_step_completed` (with step property)
- `[activation_event]` — your core value moment
- `upgraded_to_paid`
- `invited_team_member` (if applicable)

**Tier 2 (15–25 events):**
Everything from Tier 1, plus:
- `feature_used` (with feature name property — covers multiple features in one event)
- `search_performed` / `query_executed` / `[core_action]` (with properties)
- `settings_changed` (with setting name)
- `billing_page_viewed`
- `plan_changed` (with old/new plan)
- `churned` / `subscription_cancelled`
- `support_ticket_created`

**Tier 3 (25+ events with rich properties):**
Everything from Tier 2, plus: granular feature usage, team/organization-level events, API usage events, integration events, computed properties (health score, engagement score), and server-side events for reliability.

See `references/guide.md` → Event Taxonomy Design for naming conventions and property standards.

---

## Session Recording — Light Touch

Session recording tools (Hotjar, PostHog, Microsoft Clarity, FullStory) capture video replays of user sessions. They answer "what is the user actually doing?" in a way event data can't.

**When session recording is worth it:**
- Users aren't activating and you don't know why
- A specific funnel step has high drop-off and events don't explain it
- You're redesigning onboarding and need to see current behavior
- Support tickets describe confusion you can't reproduce

**When it's not worth the effort:**
- You have < 50 users (just watch over their shoulder on a call)
- You don't have a specific question to answer
- You're already doing customer interviews that cover the same ground

**Tool recommendation:** PostHog includes session recording in the free tier — if you're already using PostHog for product analytics, turn it on and filter to specific flows. If not, Microsoft Clarity is free and lightweight. Don't add Hotjar or FullStory until you've outgrown the free options.

---

## Analytics by Product Stage

### Pre-Launch: Don't Set Up Analytics. Ship.

If you haven't launched, the only analytics you need are GA4 on your landing page (10 minutes) to see if anyone shows up. Everything else waits until you have real users producing real data. Don't instrument an app nobody is using yet.

The one exception: if you have a waitlist or beta signup page, track the conversion event. That's one event, one page, five minutes of work.

### Post-Launch, First 100 Users: Tier 1, Fast

```
Week 1: Install GA4 + one product analytics tool (PostHog/Mixpanel free)
Week 1: Define and track 5–10 key events
Week 2: Add UTM parameters to all shared links
Week 2: Look at your signup → activation funnel for the first time
Week 3–4: Watch for patterns. Don't optimize yet — you don't have enough data.
```

At this stage, qualitative data (customer interviews, support conversations) is more valuable than quantitative data. You don't have statistical power. Use analytics to spot gross problems (broken funnels, zero activation), not to optimize.

### 100–1,000 Users: Tier 2, Connect the Systems

This is where analytics starts earning its keep. You have enough data to see patterns.

```
Month 1: Add GTM, expand to 15–25 events, implement identity stitching
Month 1: Define your activation metric (even a hypothesis is fine)
Month 2: Connect marketing → product (UTM params as user properties)
Month 2: Run your first acquisition quality analysis: which channel → best activation?
Month 3: Set up basic retention cohorts (weekly or monthly)
Month 3: Build your first dashboard (3–5 charts, not 30)
```

### 1,000+ Users: Tier 2 → Tier 3 Transition

You now have enough data for statistical confidence. Analytics becomes a continuous function.

- Validate or refine your activation metric with real correlation data
- Build segment-level retention analysis (by channel, plan, company size)
- Consider data infrastructure (Segment/Rudderstack, warehouse) if tool limits or data reliability become problems
- Build dashboards for team members, not just yourself

---

## Reference Files

- `saas-marketing-background/references/background.md` — shared intake questions; read before advising
- `references/guide.md` — complete reference: GA4 setup, GTM patterns, tool-specific implementation (Mixpanel, Amplitude, PostHog, Heap, Pendo), event taxonomy design, marketing-product connection code, metric definitions, dashboard templates, data infrastructure (Segment, Rudderstack, warehouses, BI tools)
