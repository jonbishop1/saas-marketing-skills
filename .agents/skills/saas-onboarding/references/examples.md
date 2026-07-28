# Worked Examples

Two complete examples showing how the onboarding skill works end-to-end: from intake through situation assessment, onboarding design, and implementation plan. These demonstrate how recommendations change based on product type, complexity, and the founder's resources.

---

## Table of Contents

1. [Example 1: API Monitoring Product (PLG, Low Complexity, Solo Founder)](#example-1-api-monitoring-product)
2. [Example 2: SEO Keyword Research Tool (PLG + Sales-Assist, Medium Complexity, Small Team)](#example-2-seo-keyword-research-tool)

---

## Example 1: API Monitoring Product

### Scenario: PingForge

**The founder:** Solo technical founder. Full-stack engineer. Built the entire product. Has never designed onboarding beyond a "Welcome!" flash message that disappears after 2 seconds. "People sign up and I think most of them never actually set up monitoring."

**The product:** API uptime and latency monitoring. Users paste an endpoint URL, set a check interval, and get alerts. The core action takes 30 seconds. 5 months post-launch, ~80 paying customers, growing slowly.

**Current onboarding state:**
- Signup flow: email + password → lands on empty dashboard
- No welcome screen (the flash message doesn't count)
- Empty dashboard shows column headers for monitors, latency, and alerts — all empty
- No checklist, no tooltips, no guidance
- One welcome email that says "Welcome to PingForge! Get started by logging in." with a login link
- No trial expiry emails
- Free plan + paid plans. Freemium model with 5 free endpoints.

**Metrics (rough):**
- ~200 signups/month
- ~25% add their first endpoint (signup-to-first-action)
- ~15% configure an alert (signup-to-activation — the founder's guess)
- ~3% convert to paid within 30 days
- No formal activation metric defined

**Tools:** No onboarding tool. No email automation (welcome email is sent via SendGrid API, hand-coded). PostHog for basic analytics. React frontend.

**Time/budget:** 1–2 days of dev time available now. No tool budget currently, but would pay $100/mo if convinced it helps.

**Competitors:** "Better Uptime has a nice onboarding — they walk you through adding your first monitor and setting up a status page. Uptime Robot is basically zero onboarding but their product is simple enough it doesn't matter."

---

### Situation Assessment

**Product complexity:** Low. Value in 30 seconds (paste URL → monitoring starts). This is the easiest onboarding to fix because the core action is so simple. The problem isn't product complexity — it's that users arrive at an empty screen and don't know what to do.

**Launch stage:** Post-launch, 200 signups/month, ~80 paying customers. Enough data to see the problem but early enough that simple fixes will have outsized impact.

**GTM motion:** PLG, self-serve. No human involvement in onboarding. The product must teach itself.

**Founder's UX experience:** Minimal. Needs specific, implementable patterns, not abstract principles.

**Resources:** Solo, 1–2 days of dev time, no tool budget initially. → Tier 1 execution. Everything must be custom-coded and simple.

**Current onboarding diagnosis:**
The pipeline leak is massive and obvious:
```
Signup (200/mo) → First endpoint added (50, 25%) → Alert configured (30, 15%) → Paid (6, 3%)
```

75% of users never add their first endpoint. This is almost certainly an empty state problem — they land on a blank dashboard and don't know what to do. The "Welcome!" flash message provides no guidance and disappears before they can read it.

The single highest-leverage fix: replace the empty dashboard with a clear empty state that drives the user to add their first endpoint.

---

### Recommended Tier: Tier 1 (1–2 days of custom code)

This is a Tier 1 situation where Tier 1 will have outsized impact because the current state is so poor. Going from "no onboarding" to "basic onboarding" is the biggest single improvement possible.

### The Design

**Step 1: Replace the empty dashboard with an actionable empty state**

Current: Empty table with headers "Endpoint | Status | Latency | Last Check" and no rows.

New:
```
┌─────────────────────────────────────────────────┐
│                                                   │
│  👋 Let's monitor your first API endpoint         │
│                                                   │
│  Paste your endpoint URL below and PingForge       │
│  will start checking it every 5 minutes.           │
│  You'll get an alert if it goes down.              │
│                                                   │
│  ┌─────────────────────────────────────┐          │
│  │  https://                           │          │
│  └─────────────────────────────────────┘          │
│  ┌──────────────────┐                             │
│  │  Start monitoring  │                            │
│  └──────────────────┘                             │
│                                                   │
│  Or try with a sample endpoint →                   │
│                                                   │
│  ─────────────────────────────────────────────    │
│  💡 What you'll see:                               │
│  [Screenshot of a populated dashboard with         │
│   uptime chart, latency graph, and status]         │
└─────────────────────────────────────────────────┘
```

The "try with a sample endpoint" link pre-fills a demo URL and creates a monitor with pre-loaded historical data. The user sees an active dashboard immediately, understands the product, then adds their own endpoints.

**Why this works:** The URL input is right there — no navigation needed. The user understands what will happen. The sample endpoint option removes all friction for evaluation.

**Step 2: Post-activation success state**

After the first endpoint is added and the first check completes:

```
┌─────────────────────────────────────────────────┐
│  ✅ Your first monitor is live!                    │
│                                                   │
│  PingForge is now checking [endpoint URL]          │
│  every 5 minutes. You'll get an email if it        │
│  goes down.                                        │
│                                                   │
│  Want faster alerts? Set up Slack notifications →   │
│                                                   │
│  [Dashboard now shows real data for the endpoint]  │
└─────────────────────────────────────────────────┘
```

The nudge to Slack notifications is the next engagement step. Slack alerts are stickier than email alerts and correlate with retention.

**Step 3: Fix the welcome email**

Current: "Welcome to PingForge! Get started by logging in."

New (reference `saas-copywriting` for polish, but the structure is):

```
Subject: Your API monitoring is ready — add your first endpoint

Body:
Welcome to PingForge!

The fastest way to get started:

1. Log in → [button: Open PingForge]
2. Paste any API endpoint URL
3. You'll have monitoring running in 30 seconds

That's it. You'll get an alert if your endpoint goes down.

If you want to see how it looks first, try our sample endpoint
when you log in — it's pre-loaded with 24 hours of monitoring data.

— [Founder name]
```

**Step 4: Add a trial expiry email (freemium conversion nudge)**

Since PingForge is freemium, there's no trial expiry. Instead, add a usage-milestone email triggered when the user is approaching the free tier limit:

```
Trigger: User has 4 of 5 free endpoints

Subject: You're monitoring 4 endpoints — your 5th is free too

Body:
You're getting real value from PingForge — your 4 endpoints have had
[X]% average uptime this week.

You've got room for one more endpoint on the free plan. After that,
the Starter plan ($29/mo) gives you up to 25 endpoints with 1-minute
check intervals and Slack alerts.

[button: Add your 5th endpoint]

Or if you're ready for faster checks and Slack alerts:
[button: See pricing]
```

### Implementation plan

| Task | Effort | Priority |
|---|---|---|
| Empty state redesign on dashboard | 4–6 hours | P0 — do this first |
| Sample endpoint functionality | 2–3 hours | P0 — part of empty state |
| Post-activation success banner | 1–2 hours | P1 |
| Fix welcome email copy | 30 minutes | P1 |
| Usage milestone email (4/5 endpoints) | 2–3 hours (need event tracking) | P2 |

**Total: ~1.5 days of focused work.**

### Expected results

Conservative estimates based on the changes:
- Signup-to-first-endpoint: 25% → 40–50% (the empty state with inline form is the biggest lever)
- Signup-to-activation: 15% → 25–35% (success state nudges toward alert configuration)
- Paid conversion: 3% → 4–6% (usage milestone email catches users approaching limits)

These improvements compound. Going from 6 to 10+ new paying customers per month from the same 200 signups is a meaningful acceleration.

### What to do next (after Tier 1 is live)

1. **Instrument the funnel.** Track: signup → dashboard_visited → first_endpoint_added → first_check_completed → first_alert_configured → paid_conversion. Use PostHog.
2. **Watch session recordings.** PostHog records sessions — watch 20 new user sessions to see where people get confused.
3. **After 30 days with data:** Consider adding a 3-item checklist if the data shows users complete the first endpoint but don't configure alerts. The checklist creates a visible path from "endpoint added" to "fully set up."
4. **After 60 days:** If signups > 300/month, evaluate adding Userflow or Product Fruits for a checklist + tooltips.

---

## Example 2: SEO Keyword Research Tool

### Scenario: KeyScope

**The founders:** Two-person team — technical co-founder and growth co-founder. Growth co-founder owns onboarding strategy. Technical co-founder implements.

**The product:** Keyword research tool focused on gap analysis and opportunity scoring. Medium complexity: user adds their domain, adds competitors, runs gap analysis, reviews results. Core value moment is seeing the gap analysis results with opportunity scores.

**Current onboarding state:**
- Signup: email + password + "What's your primary use case?" (content marketing / SEO audits / competitive analysis)
- After signup: welcome modal with 3-step instruction ("1. Add your domain, 2. Add a competitor, 3. Run gap analysis")
- Dashboard shows recent analyses (empty for new users — shows "No analyses yet")
- Onboarding checklist: exists but buried in a sidebar and only 2 of 4 items have clear CTAs
- 5-email onboarding sequence (time-based, not behavioral)
- 14-day free trial, no CC

**Metrics:**
- 450 signups/month
- 55% add their domain (step 1)
- 40% run their first gap analysis (step 2)
- 28% view and interact with results (activation metric — "viewed gap analysis results and clicked on at least one keyword")
- 8% convert to paid within 14 days
- Day 1 return rate: 35%
- Day 7 return rate: 18%

**Tools:** Intercom (in-app messages + email), Amplitude for analytics, React frontend.

**Time/budget:** Growth co-founder can dedicate 8–10 hours/week to onboarding. Budget for tools already covered (Intercom). Technical co-founder available for 1–2 days of implementation per month.

**Competitors:** "Ahrefs has no onboarding — they assume you know what you're doing. Mangools has a nice guided setup that helps you configure your first project. SE Ranking has tooltips everywhere but it feels overwhelming."

---

### Situation Assessment

**Product complexity:** Medium. 3–4 steps to value (add domain → add competitor → run analysis → view results). Not trivial but not complex.

**Launch stage:** Growth stage, 450 signups/month, 340 customers. Enough data for meaningful optimization. This is a tuning problem, not a "build from scratch" problem.

**GTM motion:** Primarily PLG. But some enterprise leads need sales-assist (agencies evaluating for team use, companies with 10+ users).

**Resources:** Dedicated growth person + some dev time + existing tools. → Tier 2 moving to Tier 3. Can execute segmented, behavioral onboarding.

**Current onboarding diagnosis:**

```
Signup (450) → Domain added (248, 55%) → Gap analysis run (180, 40%) → Results viewed (126, 28%) → Paid (36, 8%)
```

The funnel has two significant leaks:
1. **Domain added → Gap analysis run (55% → 40%, losing 68 users/month):** Users add their domain but don't complete the analysis. This is likely a friction or motivation problem at the "add competitor" step.
2. **Gap analysis run → Results viewed and activated (40% → 28%, losing 54 users/month):** Users run the analysis but don't engage with results. This might be a results comprehension problem — the data comes back and users don't know what to do with it.

The smaller but also important leak: 45% of signups don't even add their domain. The welcome modal tells them to but doesn't make it easy enough.

**Day 1 return rate of 35% is below benchmark (40–60%).** The first session isn't creating enough hook to bring users back. This connects to the results engagement problem — if users don't understand or get excited by the results, they don't return.

---

### Recommended Tier: Tier 2 → Tier 3 over 8 weeks

Week 1–2: Fix the two biggest leaks with targeted interventions.
Week 3–4: Upgrade email to behavioral triggers.
Week 5–8: Add segmentation and progressive disclosure.

### Week 1–2: Fix the leaks

**Fix 1: Replace the empty analysis view with a sample analysis**

Currently, new users see "No analyses yet" with a button to start. Instead:

Show a pre-loaded sample gap analysis for "example.com vs competitor.com" with real-looking data. The user can explore the interface, understand what they'll get, and see opportunity scores in action — before entering their own domain.

Above the sample data, a persistent banner:
```
📊 This is sample data. Run your first real analysis:
[Your domain: ________] vs [Competitor: ________]  [Run analysis →]
```

**Why:** This solves both leaks simultaneously. Users who see sample data understand what the product does (reducing the 55% → 40% drop) AND understand how to interpret results (reducing the 40% → 28% drop). The sample data is the product's best sales pitch.

**Fix 2: Inline competitor suggestions**

When the user adds their domain, automatically suggest 2–3 competitors based on the domain. "Based on your domain, your likely competitors are: [competitor1.com], [competitor2.com], [competitor3.com]. Select one to run your first analysis."

**Why:** The "add a competitor" step is friction because users have to think about and type a competitor domain. Suggestions reduce this to a single click.

**Fix 3: Results onboarding within the gap analysis**

When the first gap analysis results load, add an inline results guide:

```
┌─────────────────────────────────────────────┐
│ 🎯 Your keyword gap analysis found 147       │
│ keywords your competitors rank for that you   │
│ don't.                                        │
│                                               │
│ Here's how to read your results:              │
│ • Green = High opportunity (you can likely     │
│   rank with one good piece of content)         │
│ • Yellow = Medium opportunity (competitive,    │
│   but achievable in 3-6 months)               │
│ • Red = Hard (dominated by high-authority      │
│   sites — save these for later)               │
│                                               │
│ Start with green keywords. Click any keyword   │
│ to see the full SERP analysis.                │
│                                               │
│ [Got it, show me my results →]                │
└─────────────────────────────────────────────┘
```

**Why:** Users who run the analysis but don't engage with results likely don't understand what they're looking at. This in-context explanation turns data into actionable insight.

### Week 3–4: Behavioral email upgrade

**Current:** 5 time-based emails over 14 days, same for every user.

**New:** Behavioral branching based on product actions.

```
Signup
 ├─ [No domain added after 24h] → Email: "Add your domain to find keyword gaps"
 │    └─ Include 2 competitor suggestions to reduce friction
 │
 ├─ [Domain added, no analysis run after 24h] → Email: "You're one click away"
 │    └─ Show the competitor suggestion + one-click analysis CTA
 │
 ├─ [Analysis run, results not viewed] → Email: "Your gap analysis is ready"
 │    └─ Include a teaser: "We found 147 keywords — here are your top 3 opportunities"
 │
 ├─ [Activated — results viewed] → Email: "Nice work! Here's what to do next"
 │    └─ Guide toward second analysis, export features, or sharing
 │
 └─ [Trial expiry sequence]
      ├─ Day 10: Value summary ("You found 324 keyword opportunities across 3 analyses")
      ├─ Day 12: Social proof ("See how [customer] increased organic traffic 40% using KeyScope")
      └─ Day 14: Final nudge ("Your trial ends today — plans start at $49/mo")
```

**Implementation:** Intercom supports event-triggered email workflows. The growth co-founder sends product events (domain_added, analysis_run, results_viewed) from the frontend to Intercom via the JavaScript SDK. The technical co-founder implements the event firing (2–4 hours).

### Week 5–8: Segmentation and progressive disclosure

**Segmentation based on signup survey:**

The existing "What's your primary use case?" question now drives the experience:

| Use case | Onboarding emphasis | First-run experience |
|---|---|---|
| Content marketing | "Find topics your competitors write about that you don't" | Sample analysis filtered to show content-relevant keywords |
| SEO audits | "See where your client's organic strategy has gaps" | Multi-competitor comparison highlighted |
| Competitive analysis | "Track what your competitors rank for over time" | Competitor tracking features surfaced early |

**Progressive disclosure:**

- **Day 1:** Core features only (gap analysis, opportunity scores)
- **After first analysis:** Reveal keyword tracking ("Want to monitor these keywords over time?")
- **After 3 analyses:** Reveal bulk import and API access
- **After team invite:** Reveal shared workspaces and team reporting

**Sales-assist triggers:**

Flag for human outreach when:
- Agency email domain signs up (custom domain check against known agency domains)
- User runs 5+ analyses in first 3 days (power evaluator)
- User invites 3+ team members (team purchase signal)
- Enterprise domain signup (company size data from clearbit or similar enrichment)

The growth co-founder reaches out personally to flagged users: "I saw you're evaluating KeyScope for [agency name]. Want me to set up a custom demo for your team?"

### Expected results after 8 weeks

| Metric | Current | Expected (week 2) | Expected (week 8) |
|---|---|---|---|
| Domain added | 55% | 65% | 70% |
| Gap analysis run | 40% | 52% | 58% |
| Results activated | 28% | 38% | 45% |
| Trial-to-paid | 8% | 10% | 13–15% |
| Day 1 return | 35% | 45% | 50% |

Conservative estimates. The sample data and inline results guide (week 1–2 fixes) will have the most immediate impact. Behavioral email and segmentation (week 3–8) compound over time.

At 450 signups/month, improving trial-to-paid from 8% to 13% means going from 36 to 58 new customers per month — a 60% increase in customer acquisition from the same traffic.
