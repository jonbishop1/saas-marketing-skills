# SaaS Copywriting: Complete Reference Guide

Detailed frameworks, formulas, templates, and examples for each copy type. This file is the deep-dive companion to SKILL.md. Read the relevant section when you need implementation detail.

Throughout this guide, two example products are used to show how frameworks apply to different SaaS types:
- **APIWatch** — an API monitoring and alerting product (developer tool, PLG, technical buyer)
- **RankGap** — an SEO keyword research and gap analysis product (marketing tool, PLG/sales-assist, mixed technical/non-technical buyer)

---

## Table of Contents

1. [Headline Formulas](#headline-formulas)
2. [Value Proposition Frameworks](#value-proposition-frameworks)
3. [Website Pages](#website-pages)
   - [Homepage Framework](#homepage-framework)
   - [Pricing Page Frameworks](#pricing-page-frameworks)
   - [Feature Page Framework](#feature-page-framework)
4. [Landing Pages](#landing-pages)
   - [Landing Page Formulas](#landing-page-formulas)
   - [Message Match Examples](#message-match-examples)
   - [Landing Page Copy by Tier](#landing-page-copy-by-tier)
5. [Email Sequences](#email-sequences)
   - [Onboarding Sequence Blueprint](#onboarding-sequence-blueprint)
   - [Trial Expiry Sequence](#trial-expiry-sequence)
   - [Nurture Sequence](#nurture-sequence)
   - [Subject Line Formulas](#subject-line-formulas)
6. [Ad Copy](#ad-copy)
   - [Search Ad Frameworks](#search-ad-frameworks)
   - [Social Ad Hook Formulas](#social-ad-hook-formulas)
   - [Ad Copy by Intent Level](#ad-copy-by-intent-level)
7. [Sales Collateral](#sales-collateral)
   - [One-Pager Template](#one-pager-template)
   - [Case Study Structure](#case-study-structure)
   - [Competitive Comparison Sheet](#competitive-comparison-sheet)
8. [Copy Principles Reference](#copy-principles-reference)
   - [Clarity Checklist](#clarity-checklist)
   - [Specificity Patterns](#specificity-patterns)
   - [Social Proof Hierarchy](#social-proof-hierarchy)
   - [CTA Best Practices](#cta-best-practices)

---

## Headline Formulas

Headlines do the most work in any piece of copy. A strong headline earns attention; a weak one makes everything below it invisible. These formulas are starting points — adapt them, don't fill in blanks robotically.

### Formula 1: [Outcome] + [Qualifier]

States the benefit and scopes it to the audience or method.

```
APIWatch:   "API monitoring that pages you before your customers notice."
RankGap:    "Find the keywords your competitors rank for and you don't."
```

Why it works: outcome-first, specific enough to self-select the right audience.

### Formula 2: [Do X] without [undesirable thing]

Pairs a desired outcome with the removal of a known pain.

```
APIWatch:   "Monitor every endpoint without per-host pricing."
RankGap:    "Run keyword gap analysis without exporting spreadsheets."
```

Why it works: addresses a specific objection or frustration with existing solutions.

### Formula 3: [Specific metric] + [in timeframe]

Uses numbers and time to create concreteness.

```
APIWatch:   "Detect API errors in under 30 seconds."
RankGap:    "Find 100+ keyword gaps in 2 minutes."
```

Why it works: specificity builds credibility. Vague claims ("fast," "powerful") are noise.

### Formula 4: [Action verb] + [what they actually want]

Starts with the user's action, ends with their desired outcome.

```
APIWatch:   "Ship faster. Break less."
RankGap:    "Stop guessing which keywords to target."
```

Why it works: short, punchy, speaks to the emotional state. Good for hero sections and ads.

### Formula 5: [Who it's for] + [what changes for them]

Explicitly names the audience and the transformation.

```
APIWatch:   "For engineering teams that refuse to find out about downtime from Twitter."
RankGap:    "For SEOs tired of keyword tools that hide the data that matters."
```

Why it works: self-selection. The right reader thinks "that's me." Everyone else moves on. That's the point.

### Anti-patterns to flag

- **"The all-in-one platform for..."** — vague, overused, says nothing specific
- **"Powerful, flexible, scalable"** — adjectives without evidence are noise
- **"Revolutionize your workflow"** — hyperbolic and meaningless
- **"Next-generation [category]"** — what generation? What changed?
- **"[Product name]: [Category] reimagined"** — reimagined how? This headline does no work.

---

## Value Proposition Frameworks

A value proposition is the core argument for why someone should choose your product. It's not a tagline — it's the strategic foundation that every piece of copy is built on.

### Framework: The Positioning Statement

```
For [target audience]
who [situation or need],
[product name] is a [category]
that [key benefit].
Unlike [alternatives],
we [primary differentiator].
```

**APIWatch example:**
```
For backend engineering teams
who need to know about API issues before their users do,
APIWatch is an API monitoring tool
that detects latency spikes and errors with 30-second resolution.
Unlike Datadog and New Relic,
we charge per endpoint, not per host — so monitoring scales with your API, not your infrastructure bill.
```

**RankGap example:**
```
For SEO professionals and content teams
who need to find keyword opportunities they're missing,
RankGap is a keyword research tool
that shows the exact queries competitors rank for and you don't.
Unlike Ahrefs and SEMrush,
we focus entirely on gap analysis — no feature bloat, just the keywords you're leaving on the table.
```

This positioning statement isn't copy that goes on the website. It's the reference document that keeps all copy consistent. When writing any piece of copy, check it against this.

### The "So What" Test

For every claim in your copy, ask "so what?" until you reach the outcome the buyer actually cares about:

```
APIWatch:
  "We use WebSocket connections." → So what?
  "You get real-time monitoring." → So what?
  "You see errors the second they happen." → So what?
  "You fix issues before customers are affected." → That's the headline.

RankGap:
  "We analyze SERP data." → So what?
  "You see keyword gaps." → So what?
  "You find pages competitors rank for that you don't." → So what?
  "You stop writing content that nobody searches for." → That's the headline.
```

Most engineer-written copy stops at level 1 or 2. Push to level 3 or 4 — that's where the persuasive copy lives.

---

## Website Pages

### Homepage Framework

The homepage serves multiple audiences at once: first-time visitors, returning evaluators, existing customers looking for docs. Organize it as a progressive disclosure of value.

**Section-by-section structure:**

#### Above the fold (0-1 seconds)

| Element | Purpose | Guidance |
|---|---|---|
| Headline | What is this, who is it for | Use headline formulas above. Pass the bar test. |
| Subhead | How it works or primary proof | One sentence. Add specificity the headline lacks. |
| CTA | Next step | One primary CTA. "Start free trial" > "Get started" > "Learn more" |
| Visual | Show the product | Screenshot, demo GIF, or short video. Not a stock photo. |

**APIWatch above the fold:**
```
Headline: "API monitoring that pages you before your customers notice."
Subhead: "Track latency, errors, and uptime across every endpoint. Alerts in 30 seconds. Free up to 10 endpoints."
CTA: [Start Free Trial]
Visual: Dashboard screenshot showing an alert firing on a latency spike
```

**RankGap above the fold:**
```
Headline: "Find keywords your competitors rank for and you don't."
Subhead: "Keyword gap analysis in minutes. Difficulty scores based on real SERP data, not estimates."
CTA: [Try Free for 14 Days]
Visual: Screenshot of a gap analysis report with highlighted opportunities
```

#### Social proof bar (2-3 seconds)

Logos, user count, or one short testimonial. This doesn't need to be elaborate.

**Tier 1 (no logos yet):** Use a metric. "Monitoring 50,000+ API calls daily" or "Analyzing 2M+ keywords." If you don't have a metric, skip this section entirely — don't fabricate.

**Tier 2-3:** Logo bar of recognizable customers. 5-8 logos is ideal. Add "Trusted by teams at..." above the logos.

#### Benefits section (5-15 seconds)

Three key benefits, each structured as:
```
[Benefit headline — outcome-focused]
[2-3 sentences explaining how the product delivers this outcome]
[Optional: specific metric or proof point]
```

Common mistake: listing features here. "WebSocket-based monitoring" is a feature. "See errors in real time — not 5 minutes later" is a benefit. Lead with the outcome, then explain the mechanism only if the buyer cares about it (technical buyers often do).

#### How it works (15-30 seconds)

Three steps, simplified. This isn't documentation — it's a confidence builder.

```
APIWatch:
  1. Add one line to your config → "Point APIWatch at your endpoints"
  2. See your dashboard populate → "Latency, errors, and uptime in real time"
  3. Get paged when something breaks → "Slack, PagerDuty, or webhook — your choice"

RankGap:
  1. Enter your domain and a competitor → "We crawl both sites and compare rankings"
  2. See every keyword gap → "Sorted by traffic potential and difficulty"
  3. Export to your content plan → "CSV, Sheets, or direct to your project board"
```

#### Secondary proof (30-60 seconds)

For visitors still scrolling, add:
- Detailed testimonial with name, title, company
- Case study summary with a specific metric ("Reduced MTTD from 12 minutes to 30 seconds")
- Integration logos (if relevant — "Works with your existing stack")
- Security badges (SOC 2, GDPR, etc. — especially for enterprise-facing products)

#### FAQ / objection handling

Address the top 3-5 reasons someone wouldn't sign up. Get these from:
- Sales calls (what objections come up?)
- Support tickets (what confuses people?)
- Competitor comparison (what do people worry about when switching?)

Common SaaS objections to address:
- "How long does setup take?"
- "What happens when my trial ends?"
- "Can I export my data?"
- "Do you integrate with [tool they already use]?"
- "What's the pricing?" (link to pricing page if not on this page)

#### Final CTA

Repeat the primary CTA. Same button, same copy. Adding a secondary CTA here ("Talk to sales" alongside "Start free trial") is acceptable for products that serve both self-serve and enterprise buyers.

### Pricing Page Frameworks

Pricing pages have the highest buyer intent of any page on your site. Someone visiting pricing is actively evaluating. The copy job here is to make the decision easy.

**Structure:**
1. Headline — not "Pricing" (boring). Try: "Simple pricing that scales with you" or "Start free. Pay when you're ready." or just clearly state the model.
2. Plan cards — feature comparison with the recommended plan highlighted
3. Plan names — should signal who each plan is for (not clever internal names)
4. CTA per plan — "Start free trial" for self-serve, "Contact sales" for enterprise
5. FAQ — pricing-specific objections (billing cycle, overages, cancellation, discounts)

**Tier 1 pricing page:** Can be a section on the homepage. Just list the plans, what's included, and the CTA.

**Tier 2-3 pricing page:** Dedicated page with feature comparison table, calculator (for usage-based pricing), and FAQ.

**APIWatch pricing copy example:**
```
Headline: "Free up to 10 endpoints. No credit card."
Plans: Starter (free), Team ($49/mo), Enterprise (custom)
CTA: [Start Free] | [Start Free Trial] | [Contact Sales]
Clarity detail: "All plans include 30-second resolution, Slack alerts, and API access."
```

**RankGap pricing copy example:**
```
Headline: "14-day free trial on every plan. Cancel anytime."
Plans: Solo ($29/mo), Team ($79/mo), Agency ($199/mo)
CTA: [Start Free Trial] on all self-serve plans
Clarity detail: "Every plan includes unlimited keyword gap reports. Plans differ by tracked domains and competitor slots."
```

### Feature Page Framework

Feature pages serve buyers evaluating specific capabilities and SEO traffic for feature-related queries.

**Structure:**
1. Headline — the outcome this feature enables (not the feature name)
2. Subhead — how it works in one sentence
3. Visual — screenshot or GIF of the feature in action
4. Benefits — 3-4 outcomes this feature creates
5. Technical detail — for technical buyers, how it works under the hood
6. Use case — a specific scenario showing the feature solving a real problem
7. CTA — back to the primary conversion action

**Write for the buyer first, then optimize for SEO.** Feature pages rank for long-tail queries, but keyword-stuffing kills readability.

---

## Landing Pages

### Landing Page Formulas

#### PAS (Problem → Agitation → Solution)

Best for: audiences aware of their problem but not your product.

```
Problem: State the pain clearly.
Agitation: Describe the consequences of not solving it — make the pain vivid.
Solution: Introduce your product as the resolution.
```

**APIWatch PAS example:**
```
Problem: "Your API goes down. You find out when a customer tweets about it."
Agitation: "Every minute of downtime costs revenue and trust. And the longer it takes
           to detect, the longer it takes to fix. Your monitoring tool checks every
           5 minutes. That's 5 minutes of users hitting errors."
Solution: "APIWatch checks every 30 seconds and pages you instantly.
           Detect issues before your customers do."
CTA: [Start Free Trial — 30 Second Setup]
```

**RankGap PAS example:**
```
Problem: "You're publishing content every week, but organic traffic isn't growing."
Agitation: "The problem isn't your content — it's your targeting. You're writing about
           topics your competitors already own, and missing the keywords where you
           could actually win. Every article targeting the wrong keyword is time
           and money you don't get back."
Solution: "RankGap shows you exactly which keywords competitors rank for and you don't —
           sorted by difficulty and traffic potential."
CTA: [Find Your Keyword Gaps — Free for 14 Days]
```

#### AIDA (Attention → Interest → Desire → Action)

Best for: audiences with low awareness. Good for social ad landing pages.

```
Attention: Hook with a surprising fact, question, or bold claim.
Interest: Explain what makes this worth their time.
Desire: Show the outcome — what life looks like with this product.
Action: Clear, specific CTA.
```

#### BAB (Before → After → Bridge)

Best for: audiences who know the problem and want the transformation.

```
Before: Current painful state.
After: Life with the problem solved.
Bridge: Your product is how they get there.
```

### Message Match Examples

The #1 landing page conversion killer is message mismatch. The headline on the landing page must reflect the promise that brought the visitor there.

| Source | Source copy | Landing page headline | Match? |
|---|---|---|---|
| Google Ad | "API monitoring — 30 second alerts" | "Detect API issues in 30 seconds" | Yes |
| Google Ad | "API monitoring — 30 second alerts" | "The Complete Observability Platform" | No — too broad |
| Meta Ad | "Stop publishing content nobody searches for" | "Find keyword gaps in 2 minutes" | Yes |
| Meta Ad | "Stop publishing content nobody searches for" | "The #1 SEO Research Tool" | No — different promise |
| Email | "3 keywords your competitors rank for (and you don't)" | "See your full keyword gap report" | Yes |
| Email | "3 keywords your competitors rank for (and you don't)" | "Try RankGap free" | Weak — no content echo |

### Landing Page Copy by Tier

**Tier 1 (solo founder, one page):**
- Use PAS formula — it's the most forgiving structure
- Headline + subhead + 3 bullets + CTA + one testimonial (if available)
- Total copy: 150-300 words. Don't overthink it.
- No A/B testing — get one page live and measure conversion rate before optimizing

**Tier 2 (some help, 2-3 pages):**
- One page per primary acquisition channel or audience
- Different headline angle per page, same core value proposition
- Add a FAQ section to handle top 3 objections
- Total copy: 300-500 words per page

**Tier 3 (team, testing program):**
- Variant testing: test headlines first (highest leverage), then social proof, then CTA copy
- Segment-specific pages: different messaging for different personas or use cases
- Dynamic keyword insertion for search ad landing pages (if volume justifies it)

---

## Email Sequences

### Onboarding Sequence Blueprint

Onboarding emails have one job: get the user to their "aha moment" — the point where they experience the product's core value for the first time.

**Before writing, identify the activation milestone:**
- APIWatch: user sets up monitoring on their first endpoint and receives a working alert
- RankGap: user runs their first gap analysis and sees keyword opportunities

Every email in the sequence should push toward that milestone.

#### Tier 1: 3-email onboarding (minimum viable)

**Email 1: Welcome (send immediately)**
```
Subject: Your [product] account is ready
Content:
- Confirm signup
- One clear next step toward activation: "Here's how to get started in the next 2 minutes:"
- Link directly to the first action (not the dashboard — the specific action)
- Sign off with a real name
```

APIWatch Email 1:
```
Subject: APIWatch is ready — add your first endpoint
Body: "[Name], your account is live. Add your first endpoint to start monitoring:
      [Button: Add Your First Endpoint]
      It takes about 30 seconds. Once it's added, you'll see latency and error data
      within a minute."
```

RankGap Email 1:
```
Subject: Run your first keyword gap analysis
Body: "[Name], you're in. Here's the fastest way to find keywords you're missing:
      [Button: Start Your First Gap Analysis]
      Enter your domain and one competitor. You'll see results in under 2 minutes."
```

**Email 2: Value nudge (Day 2-3)**
```
Subject: [Specific thing they can do next]
Content:
- If they completed the activation step: congratulate, suggest the next feature
- If they haven't: remind them of the benefit, reduce friction ("takes 30 seconds")
```

**Email 3: Social proof + urgency (Day 5-7)**
```
Subject: [How another customer uses the product]
Content:
- Short testimonial or use case showing the outcome
- Reiterate the core benefit
- CTA back to the product
```

#### Tier 2-3: 5-7 email onboarding with behavioral branching

Add to the Tier 1 sequence:
- **Email 2b (if activated):** Feature highlight — show the next valuable thing they haven't tried
- **Email 4 (Day 5):** Integration email — connect to their existing stack (Slack, tools, etc.)
- **Email 5 (Day 7):** Case study email — longer social proof with specific metrics
- **Email 6 (Day 10):** Value summary — "Here's what you've seen so far" with usage data
- **Email 7 (Day 12-14):** Trial decision email — if on trial, transition to trial expiry sequence

**Behavioral branching:** Use activation status as the branch point. Users who activated get feature-expansion emails. Users who didn't get re-engagement emails with progressively stronger CTAs and lower friction ("reply to this email and I'll set it up for you").

### Trial Expiry Sequence

**Tier 1: 2 emails**

```
Email 1 (3 days before expiry):
  Subject: Your trial ends in 3 days
  Content: Recap what they've used. State what happens when the trial ends
  (data preserved? read-only? deleted?). CTA to upgrade.

Email 2 (1 day before or day of expiry):
  Subject: Last day of your [product] trial
  Content: Direct, no-pressure. Remind them of their usage metrics if available.
  CTA to upgrade. If they're not ready: "Reply and tell us what's holding you back."
```

**Tier 2-3: 4-email countdown**

Add:
- Email 1b (5 days before): feature they haven't tried yet ("Before your trial ends, try...")
- Email 3 (day after expiry): "Your trial ended — here's what you're missing" with a 48-hour extension offer or discount (if your pricing strategy supports it)

### Nurture Sequence

For leads who aren't ready to try the product yet (waitlist signups, content leads, webinar attendees).

**Tier 1: Skip this.** Focus onboarding and trial expiry sequences on people who already signed up. Nurture is a Tier 2+ activity.

**Tier 2-3: 4-6 emails over 2-3 weeks**

Structure each email around a single insight or proof point:
1. Problem education — deepen understanding of the pain your product solves
2. Solution education — how products in your category approach the problem (not a pitch — genuine education)
3. Social proof — customer story with a specific metric
4. Differentiator — what makes your approach different (this is the first "pitch" email)
5. Offer — CTA to try the product with a specific reason to act now
6. (Optional) Follow-up on #5 — lighter touch, different angle

### Subject Line Formulas

Subject lines determine open rates. Keep them short (40-60 characters), specific, and curiosity-driven.

**Formulas that work for SaaS:**

| Formula | Example (APIWatch) | Example (RankGap) |
|---|---|---|
| [Specific number] + [outcome] | "3 alerts that would've saved your Friday" | "47 keywords you're missing" |
| [Question about their pain] | "How fast do you find out about downtime?" | "Publishing content nobody searches for?" |
| [Action] + [in timeframe] | "Set up monitoring in 90 seconds" | "Find keyword gaps in 2 minutes" |
| [What peers are doing] | "How Stripe's team monitors APIs" | "How Buffer finds content ideas" |
| [Direct and honest] | "Your trial ends in 3 days" | "Your free trial ends Friday" |

**Anti-patterns:**
- ALL CAPS or excessive punctuation (!!!!) — triggers spam filters and looks desperate
- "Quick question" — overused, feels like a cold sales tactic
- Clickbait that doesn't match the email body — erodes trust permanently
- Emojis in B2B — divisive. Default to no emojis unless the brand is very casual.

---

## Ad Copy

### Search Ad Frameworks

Search ads match declared intent — the user told Google what they want. Your job is to match that intent in the ad copy and carry it through to the landing page.

**Framework: Intent → Match → Differentiate → Act**

```
Headline 1: [Match the search intent — include the keyword or close variant]
Headline 2: [Differentiate — why you vs. alternatives]
Headline 3: [CTA — specific action + friction reducer]
Description: [Expand on the benefit, add a proof point, repeat CTA]
```

**By keyword type:**

| Keyword type | H1 approach | H2 approach | H3 approach |
|---|---|---|---|
| Brand | Your product name | Key benefit or tagline | Primary CTA |
| Competitor | "Switch from [X]" or "[X] Alternative" | Your differentiator vs. them | Free trial / no commitment |
| Category | Category match + qualifier | Differentiator | CTA |
| Problem | Problem restatement | Solution hint | CTA |

**APIWatch — competitor keyword "datadog alternative":**
```
H1: Looking for a Datadog Alternative?
H2: 70% Lower Cost, Same Coverage
H3: Start Free — No Credit Card
Desc: APIWatch monitors APIs with 30-second resolution. No per-host pricing.
      Free for up to 10 endpoints. Set up in 90 seconds.
```

**RankGap — category keyword "keyword gap analysis tool":**
```
H1: Keyword Gap Analysis in Minutes
H2: See Exactly Where You're Losing Traffic
H3: Try Free — 14 Day Trial
Desc: Compare your rankings against any competitor. Find keywords they rank for
      and you don't — sorted by traffic potential. Trusted by 2,000+ SEOs.
```

### Social Ad Hook Formulas

Social ads interrupt — the user wasn't looking for you. You have 1-2 seconds to earn attention. The hook is everything.

**Formula 1: Contrarian claim**
```
"Most SaaS companies are monitoring the wrong metrics."
"Keyword difficulty scores are lying to you."
```

**Formula 2: Specific pain recognition**
```
"Finding out about API downtime from your customers' tweets?"
"Publishing 4 blog posts a month and organic traffic is flat?"
```

**Formula 3: Surprising metric**
```
"The average API outage takes 12 minutes to detect. Ours takes 30 seconds."
"We found 147 keyword gaps for a site that thought they'd covered everything."
```

**Formula 4: Before/after**
```
"Before APIWatch: 'Is the API down?' → check manually → wait → confirm → page someone.
After: Alert fires in 30 seconds. On-call gets paged automatically."
```

**Formula 5: "I was today years old"**
```
"I was today years old when I found out Datadog charges per host, not per endpoint."
"TIL that 60% of my competitor's traffic comes from keywords I'm not even targeting."
```

**Tier 1:** Pick one hook formula, write 2-3 variations. Run them against the same audience. Kill the losers after 500-1000 impressions.

**Tier 2-3:** Test across multiple formulas. Different hooks attract different segments. Use creative fatigue signals (declining CTR over 2-3 weeks) to rotate new hooks in.

### Ad Copy by Intent Level

| Intent level | Where they are | Copy approach | Example CTA |
|---|---|---|---|
| High (competitor, pricing keywords) | Evaluating solutions | Direct comparison, offer | "Switch in 10 minutes" |
| Medium (category, solution keywords) | Exploring options | Benefit-led, social proof | "Start free trial" |
| Low (problem, educational keywords) | Aware of pain, not solution | Problem recognition, education | "See how it works" |
| Cold (social, display) | Not looking | Hook + curiosity | "Find out what you're missing" |

**Match CTA aggressiveness to intent.** High-intent visitors can handle "Start free trial" or "Switch now." Cold audiences need "See how it works" or "Learn more" — they're not ready to commit.

---

## Sales Collateral

### One-Pager Template

A one-pager is the minimum viable sales document. It should work without a salesperson present — someone should be able to forward it internally and the recipient should understand the value.

**Layout (single page, PDF or web):**

```
[Logo]

HEADLINE: Core value proposition (one sentence)

THE PROBLEM
2-3 sentences describing the pain — in the buyer's language, not yours.

THE SOLUTION
What [product] does about it. Focus on outcomes, not architecture.

KEY BENEFITS
• [Benefit 1] — [one-sentence proof or metric]
• [Benefit 2] — [one-sentence proof or metric]  
• [Benefit 3] — [one-sentence proof or metric]

PROOF
[Testimonial quote with name, title, company]
—or—
[Key metric: "Reduced MTTD from 12 minutes to 30 seconds" — Company Name]

NEXT STEP
[CTA: Book a demo / Start free trial / Contact us]
[URL] | [Email]
```

**APIWatch one-pager example:**
```
HEADLINE: Detect API issues before your customers do.

THE PROBLEM: Most monitoring tools check every 5 minutes. That's 5 minutes of
users hitting errors before you even know there's a problem. And per-host
pricing means costs spike as your infrastructure scales.

THE SOLUTION: APIWatch monitors every endpoint with 30-second resolution and
alerts via Slack, PagerDuty, or webhook. Pricing is per endpoint, not per host.

KEY BENEFITS:
• 30-second detection → Reduces mean time to detect from minutes to seconds
• Per-endpoint pricing → Monitoring costs scale with your API, not your server count
• 90-second setup → Add one config line and you're live

PROOF: "We cut our mean time to detection by 95%. APIWatch paid for itself in
the first week." — Jane C., VP Engineering, [Company]

NEXT STEP: Start free at apiwatch.com — free up to 10 endpoints.
```

### Case Study Structure

Case studies are the strongest form of social proof for considered purchases. Write them as narratives, not brochures.

**Structure: Situation → Problem → Solution → Results**

```
1. The customer (who, what industry, what size)
2. The problem (in their words — use a direct quote if possible)
3. What they tried before (previous solution or workaround)
4. Why they chose your product (the decision moment)
5. The implementation (how long, how hard — be honest)
6. The results (specific metrics, before/after)
7. Quote from the customer (name, title)
```

**Tier 1:** You probably don't have case studies yet. That's fine. Use short testimonials instead. Even "We switched from [competitor] and it just works" is usable.

**Tier 2:** One case study per primary use case or persona.

**Tier 3:** Case study library organized by industry, company size, or use case.

### Competitive Comparison Sheet

Use carefully — these expire fast as competitors change pricing and features.

**Structure:**

| Dimension | Your product | Competitor A | Competitor B |
|---|---|---|---|
| [Most important differentiator] | Your advantage | Their limitation | Their limitation |
| [Second differentiator] | ... | ... | ... |
| [Pricing model] | ... | ... | ... |
| [Key feature 1] | ... | ... | ... |

**Rules for honest competitive comparison:**
- Only include dimensions where you have a genuine advantage or where the comparison is fair
- Don't misrepresent competitor capabilities
- Include dimensions where you're weaker (credibility move — if you're honest about weaknesses, the strengths are more believable)
- Date the document — competitor products change
- Update quarterly or kill it

---

## Copy Principles Reference

### Clarity Checklist

Run every piece of copy through this before shipping:

1. **Bar test:** If you read this headline to a friend at a bar, would they understand what the product does?
2. **"So what" test:** Does every claim connect to an outcome the buyer cares about?
3. **Jargon audit:** Circle every technical term. Is it language the BUYER uses, or language the BUILDER uses?
4. **Specificity check:** Replace every vague adjective ("fast," "powerful," "easy") with a number, timeframe, or comparison.
5. **One reader test:** Is this written for one specific person, or for "everyone"? Copy for "everyone" persuades no one.
6. **CTA clarity:** After reading, does the reader know exactly what to do next?

### Specificity Patterns

Vague copy converts poorly. Specificity builds credibility.

| Vague | Specific |
|---|---|
| "Fast monitoring" | "30-second detection" |
| "Affordable pricing" | "Starts at $49/mo, free tier available" |
| "Easy setup" | "One line of config, live in 90 seconds" |
| "Trusted by thousands" | "Used by 2,347 engineering teams" |
| "Comprehensive analysis" | "Analyzes 1M+ keywords across 47 countries" |
| "Great support" | "Average response time: 4 hours" |

### Social Proof Hierarchy

Not all social proof is equal. Listed from strongest to weakest:

1. **Named testimonial with metric** — "We reduced MTTD by 95%" — Jane C., VP Eng, Acme
2. **Customer logo bar** — recognizable brands signal "people like us use this"
3. **Usage metric** — "Monitoring 50M+ API calls daily"
4. **User count** — "Trusted by 2,000+ teams"
5. **Rating/review score** — "4.8/5 on G2" (works for buyer personas who check review sites)
6. **Generic testimonial** — "Great product!" — these are almost worthless. Push for specificity.
7. **No social proof** — better than fake social proof. Don't fabricate.

**Tier 1 founders with no social proof yet:** Use a usage metric if you have one ("Monitoring X API calls" counts even in beta). If you have nothing, skip social proof — an empty testimonial section looks worse than no section at all. Get your first 3-5 users and ask them for a quote. One honest sentence from a real user beats any number of carefully crafted fictions.

### CTA Best Practices

| Pattern | Example | When to use |
|---|---|---|
| [Action] + [object] | "Start free trial" | Default for self-serve products |
| [Action] + [timeframe] | "Try free for 14 days" | When trial length is an advantage |
| [Action] + [friction reducer] | "Start free — no credit card" | When reducing signup anxiety |
| [Action] + [outcome] | "Find your keyword gaps" | When the value prop is clear and specific |
| [Talk to us] | "Book a demo" / "Talk to sales" | Enterprise or high-ACV products |

**Anti-patterns:**
- "Submit" — robotic, gives no information about what happens next
- "Learn more" — acceptable only for low-intent cold traffic; too weak for warm visitors
- "Click here" — says nothing about value
- Multiple CTAs competing — one primary CTA per page section. Secondary CTAs should be visually subordinate.

**CTA button copy should complete the sentence: "I want to ___."**
- "I want to start my free trial" ✓
- "I want to submit" ✗
- "I want to find my keyword gaps" ✓
- "I want to learn more" — only if they're genuinely early-stage in awareness
