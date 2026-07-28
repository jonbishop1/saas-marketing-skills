# Competitive Research: Complete Reference Guide

Detailed methods, templates, and tools for systematic competitive intelligence. This guide covers the how — the SKILL.md covers the why and the strategy.

---

## Table of Contents

1. [Competitive Audit — Full Template](#competitive-audit--full-template)
2. [Tools for Competitive Research](#tools-for-competitive-research)
3. [Channel-Level Competitive Analysis](#channel-level-competitive-analysis)
4. [Review Mining Methods](#review-mining-methods)
5. [Pricing Page Teardown Framework](#pricing-page-teardown-framework)
6. [Competitive Battle Cards](#competitive-battle-cards)
7. [Ongoing Competitive Monitoring](#ongoing-competitive-monitoring)
8. [Win/Loss Analysis](#winloss-analysis)

---

## Competitive Audit — Full Template

### The Complete Audit Template

Use this template for each of your 3–5 direct competitors. Claude should fill in as much as possible from web research and clearly mark fields that need founder input.

```
═══════════════════════════════════════════
COMPETITOR PROFILE: [Name]
Last updated: [date]
Researched by: [Claude / founder / both]
═══════════════════════════════════════════

OVERVIEW
  Website: [URL]
  Founded: [year]
  Headquarters: [location]
  Funding: [bootstrapped / seed / Series A-C / public — amount if known]
  Team size: [estimate — check LinkedIn "people" tab]
  Estimated revenue: [if public or estimable from pricing × customer count]
  Target market: [SMB / mid-market / enterprise / all]
  Target audience: [who their copy and pricing clearly target]

PRODUCT
  Core offering: [1–2 sentence description]
  Product type: [SaaS / API / open-source / hybrid]
  Key features (top 7):
    1. [feature — note if this is a differentiator or table stakes]
    2. ...
  Technical architecture: [cloud-hosted / self-hosted / both / API-first]
  Platforms: [web / mobile / desktop / CLI / API]
  Integrations: [major integrations listed on their site]
  Free tier: [what's included, limits]
  Trial: [length, CC required?]

PRICING (detailed in Pricing Page Teardown section)
  Plans: [name — price for each tier]
  Pricing model: [per seat / per usage / flat rate / hybrid]
  Annual discount: [%]
  Enterprise: [transparent or "contact us"]
  Notable: [usage caps, overage charges, hidden costs]

POSITIONING & MESSAGING
  Homepage headline: [verbatim — exact words]
  Subheadline: [verbatim]
  Primary value prop: [your interpretation]
  Positioning angle: [cheapest / simplest / most powerful / most comprehensive / most specific niche]
  Key differentiator claim: [what they say makes them unique]
  Social proof on homepage:
    - Type: [logos / customer count / revenue / testimonials / case studies]
    - Strength: [weak / moderate / strong — are the logos recognizable? are numbers impressive?]
  CTA: [what's the primary action they want visitors to take?]
  Trust signals: [security badges, compliance certs, guarantees, uptime SLAs]

MARKETING CHANNELS
  Website:
    Estimated monthly traffic: [from SimilarWeb]
    Top traffic sources: [from SimilarWeb — direct, organic, paid, social, referral]
    Domain authority/rating: [from Ahrefs/Moz]

  Content/Blog:
    Publishing frequency: [posts per week/month]
    Content topics: [what categories do they cover?]
    Content quality: [thorough / superficial / technical / beginner-friendly]
    Top organic pages: [from Ahrefs — their biggest traffic drivers]
    Estimated organic traffic: [from Ahrefs/Semrush]

  Paid Advertising:
    Google Ads: [active? top keywords from SpyFu? estimated spend?]
    Meta Ads: [active? number of ads in Meta Ad Library? creative style?]
    LinkedIn Ads: [active? content type?]
    Other paid: [sponsorships, display, podcast ads]

  Social Media:
    Twitter/X: [handle, followers, posting frequency, engagement, content style]
    LinkedIn: [page followers, posting frequency, engagement, content type]
    YouTube: [subscribers, video count, views, content format]
    Other: [Reddit presence, Discord, TikTok, etc.]

  Email:
    [Subscribe to their newsletter before filling this in]
    Send frequency: [daily / weekly / biweekly / monthly]
    Content type: [product updates / educational / promotional / mixed]
    Quality: [would you stay subscribed?]
    Welcome sequence: [how many emails, what's the pitch?]

  Community:
    Active communities: [subreddits, forums, Discord, Slack]
    Engagement style: [helpful / promotional / absent]
    Community reaction to them: [positive / neutral / negative]

  Product Hunt:
    Launched? [yes/no — date, upvotes, placement]
    Notable comments: [any revealing feedback?]

STRENGTHS (be honest — understanding real strengths helps you avoid head-on competition)
  1. [strength]
  2. [strength]
  3. [strength]

WEAKNESSES (from reviews, community sentiment, your own evaluation)
  1. [weakness — source: G2/Reddit/personal evaluation]
  2. [weakness]
  3. [weakness]

CUSTOMER SENTIMENT SUMMARY
  G2 rating: [X.X / 5.0, N reviews]
  Capterra rating: [X.X / 5.0, N reviews]
  Top praise theme: [what reviewers love most]
  Top complaint theme: [what reviewers complain about most]
  Switching reasons: [why do people leave? from reviews and community posts]

OPPORTUNITIES FOR YOU
  1. [gap in their offering you can fill]
  2. [audience they're not serving that you can]
  3. [channel they're weak on that you can own]
  4. [messaging angle they've left open]

[FOUNDER TO FILL IN — Claude can't determine these from public data]
  Win reasons: Why do your customers choose you over this competitor?
  Loss reasons: Why do prospects choose this competitor over you?
  Feature comparison: What do they have that you don't? Vice versa?
  Customer quotes: What do your customers say about this competitor?
  Sales objections: What objections come up when this competitor is in the evaluation?
```

### Running the Audit Efficiently

**Tier 1 — 30-minute scan (per competitor):**
Google their name. Read their homepage. Check their pricing page. Read 5 G2 reviews. Check Meta Ad Library. Done. Fill in Overview, Pricing, Positioning, and top-level Strengths/Weaknesses.

**Tier 2 — 1-hour audit (per competitor):**
Everything from Tier 1 + check SimilarWeb for traffic + SpyFu/Semrush for keywords + subscribe to newsletter + check social media profiles + read 15–20 reviews on G2/Capterra. Fill in the full template except for founder-input fields.

**Tier 3 — 2-hour deep dive (per competitor):**
Full template + Wayback Machine for positioning evolution + detailed ad creative analysis + content gap analysis + sign up for their free tier and evaluate the product firsthand.

---

## Tools for Competitive Research

### Free Tools (Use These Regardless of Tier)

| Tool | What it reveals | How to use it |
|---|---|---|
| **Google search** | Who ranks, who advertises, market landscape | Search your category keywords, "best [category]", "[competitor] alternative" |
| **Meta Ad Library** | Every active Meta ad for any advertiser | Search by competitor name — see their creative, copy, and how long ads have been running |
| **LinkedIn Ad Library** | Active LinkedIn sponsored content | Check competitor company pages for sponsored posts |
| **G2** | Structured reviews with pros/cons/recommendations | Read 20+ reviews per competitor, focus on "What do you dislike?" |
| **Capterra** | Reviews with different user base than G2 | Cross-reference with G2 for broader perspective |
| **Product Hunt** | Launch history, community reaction | Search competitor name — see their launches and comments |
| **SimilarWeb (free tier)** | Traffic estimates, sources, top pages | Enter competitor URL — see monthly visits and where traffic comes from |
| **BuiltWith (free tier)** | Technology stack | See what analytics, ad, and marketing tools competitors use |
| **Wayback Machine** | Historical website versions | Compare current positioning to 6–12 months ago |
| **Newsletter signup** | Email strategy, messaging, cadence | Subscribe to every competitor's email — free intelligence |
| **Their pricing page** | Pricing, packaging, conversion strategy | Visit monthly to catch changes |

### Paid Tools (Tier 2+)

| Tool | Cost | Best for | When to add |
|---|---|---|---|
| **SpyFu** | $39/mo | Google Ads competitive intelligence — keywords, spend estimates, ad history | When Google Ads is a primary channel for your category |
| **Semrush** | $130/mo | Comprehensive: organic keywords, backlinks, content gaps, ad research, traffic analytics | When you need one tool that covers everything |
| **Ahrefs** | $99/mo | Best backlink analysis, strong content explorer, keyword gap analysis | When SEO is a primary channel |
| **SparkToro** | $50/mo | Audience intelligence — who your competitors' audience follows, reads, watches | When you need to understand audience overlap |
| **Visualping** | $10/mo | Automated monitoring of pricing page changes | When you need to track competitor pricing changes automatically |

**You don't need all of these.** One SEO tool (Ahrefs OR Semrush, not both) plus the free tools covers 90% of competitive research needs. Add SpyFu only if Google Ads is central to your category.

---

## Channel-Level Competitive Analysis

### Analyzing Competitor Content Strategy

**What to look at:**
1. Blog frequency — how often do they publish?
2. Top pages by organic traffic (from Ahrefs) — what content drives their growth?
3. Content types — tutorials, comparisons, thought leadership, product updates?
4. Content depth — surface-level or comprehensive? Do they have 10x content on any topic?
5. Keyword focus — what topic clusters are they building?

**Finding content gaps:**
Use Ahrefs Content Gap or Semrush Keyword Gap: enter your domain and 2–3 competitor domains. The tool shows keywords they rank for that you don't. These are your opportunities.

Also look manually: browse community discussions for questions that competitor content doesn't answer well. Outdated competitor posts on important topics are especially ripe for a better version.

### Analyzing Competitor Ad Strategy

**Google Ads:**
- Use SpyFu or Semrush to see which keywords competitors bid on
- Note their ad copy — what headlines and descriptions do they use?
- Check their landing pages — where do ads send traffic?
- Estimate their spend (these tools provide rough estimates)
- Look for keywords they DON'T bid on — these may be opportunities with lower CPC

**Meta Ads:**
- Meta Ad Library shows every active ad for any advertiser
- Note: how many active ads (indicates testing volume), creative formats (static vs. video vs. carousel), messaging hooks, how long ads have been running (long-running = working for them)
- Download or screenshot interesting creative for reference (inspiration, not copying)

**LinkedIn Ads:**
- Harder to research systematically. Check their company page for sponsored posts.
- Note the targeting signals in their ad copy (job titles mentioned, company sizes referenced)

### Analyzing Competitor Community Presence

**Where to look:**
- Reddit: search "[competitor name]" across all of Reddit. Note which subreddits they're mentioned in and the sentiment.
- Hacker News: search via Algolia HN search. Check their Show HN post if they had one.
- Product-specific forums and communities: are they active? Helpful? Promotional?
- Their own community: do they have a Discord, Slack, or forum? What's the engagement like?

**What sentiment reveals:**
- Positive community sentiment = strong competitive moat. Users will defend them.
- Negative sentiment = opportunity. Common complaints are your positioning angles.
- Absent sentiment = they don't invest in community. If your audience lives in communities, this is an opening.

---

## Review Mining Methods

### Systematic Review Analysis

Read 20–30 reviews per competitor on G2, Capterra, and Product Hunt. Categorize each review's key points.

**What to extract:**

| Category | What to capture | What it tells you |
|---|---|---|
| Top praise (repeated 5+ times) | Exact phrases customers use | Table-stakes features you must match |
| Top complaints (repeated 5+ times) | Exact phrases describing frustration | Your positioning opportunities |
| Switching reasons | "I switched from X because..." | Direct competitive intelligence |
| Use cases described | "We use it for..." | How customers segment themselves |
| Reviewer roles/titles | Job titles from G2 profiles | Actual buyer personas for the category |
| Company sizes | G2 shows company size | Market segmentation by competitor |

### Review Analysis Shortcuts

**The "dislike" goldmine:** On G2, every review has a "What do you dislike?" section. Read these first — they're concentrated competitive intelligence. If 15 out of 30 reviews mention "confusing UI," that's your positioning opportunity.

**The "switching from" signal:** Some reviews mention what they used before. "Switched from [competitor]" reviews tell you the migration paths in your market — who loses customers to whom and why.

**Star rating distribution matters:** A competitor with an average 4.5 rating but a cluster of 1–2 star reviews has a specific failure mode. Read the low-star reviews carefully — they reveal who the product fails for. If it fails for your target audience, that's your opening.

### Building a Complaint Frequency Table

After reading 20+ reviews, tally complaints:

```
Complaint theme              | Frequency | Severity | Opportunity for you?
Too expensive at scale       | 12/30     | High     | Yes — predictable pricing
Complex setup / steep learning| 9/30     | High     | Yes — simplicity focus
Poor customer support        | 7/30     | Medium   | Maybe — depends on your support capacity
Missing [specific feature]   | 5/30     | Medium   | Maybe — if it's on your roadmap
Slow performance             | 4/30     | High     | Only if your product is genuinely faster
Limited integrations         | 3/30     | Low      | Lower priority
```

The top 2–3 complaints with the highest frequency AND severity are your primary positioning angles.

---

## Pricing Page Teardown Framework

### What to Analyze on Each Pricing Page

**Page structure:**
- How many tiers? (2, 3, 4, or usage-based?)
- Which tier is visually highlighted? (That's the one they want you to buy — usually the middle or second-highest tier)
- Is there a free tier or free trial? What are the limits?
- Is pricing transparent or "contact sales"? At which tier does it become opaque?

**Plan design:**
- Plan names — what do they signal? ("Starter/Pro/Enterprise" vs. "Solo/Team/Business" vs. "Free/Growth/Scale")
- Feature gating — what features are locked behind higher tiers? Are the gates logical or arbitrary?
- Usage limits — what gets capped? (seats, API calls, storage, monitors, keywords, etc.)
- Overage handling — what happens when you exceed limits? (hard cap, pay-per-unit, auto-upgrade)

**Conversion psychology:**
- Anchoring — is the most expensive plan shown first to make the middle plan seem reasonable?
- Annual vs. monthly — how aggressive is the annual discount? Is annual displayed by default?
- Social proof on the pricing page — logos, customer counts, testimonials near the CTA
- Risk reduction — money-back guarantee, no-CC-required trial, "cancel anytime"
- FAQ section — what questions do they anticipate? These are the real buyer objections.

**Competitive signals:**
- Feature comparison table — how do they frame the comparison? Which features do they emphasize?
- "Most popular" badges — which plan is most popular reveals their core customer segment
- Enterprise CTA — "Contact sales" vs. transparent enterprise pricing signals how important enterprise is to them
- Add-ons — are certain features sold separately? This reveals what customers value enough to pay extra for.

### Pricing Evolution Tracking

Use Wayback Machine to check a competitor's pricing page from 6, 12, and 24 months ago. Changes reveal strategy:

- Prices going up = they have pricing power and demand is strong
- Prices going down = they're competing on price or trying to gain market share
- New tiers added = they're expanding into a new segment
- Feature gates changing = they're learning what customers will pay for
- Free tier getting more generous = they're competing for top-of-funnel
- Free tier getting restricted = they've found that free users don't convert at the current limits

---

## Competitive Battle Cards

Battle cards are one-page reference documents for sales, marketing, and product decisions. Each card covers one competitor.

### Battle Card Template

```
═══════════════════════════════════════════
BATTLE CARD: [Competitor Name]
Updated: [date]
═══════════════════════════════════════════

ELEVATOR PITCH: [Their product in 1 sentence]

THEIR STRENGTHS                    OUR STRENGTHS vs. THEM
- [strength 1]                     - [advantage 1]
- [strength 2]                     - [advantage 2]
- [strength 3]                     - [advantage 3]

COMMON OBJECTIONS WHEN COMPETING AGAINST THEM:

Objection: "They have [feature] and you don't"
Response: [honest response — acknowledge the gap, redirect to your wedge]

Objection: "They're cheaper / more established / better known"
Response: [honest response — reframe on the axis where you win]

Objection: "We're already using them"
Response: [switching value prop — what they gain by switching, acknowledge switching cost]

PRICING COMPARISON:
  Their starter: $X → Our starter: $Y
  Their pro: $X → Our pro: $Y
  Key difference: [pricing model advantage you have]

THEIR CUSTOMERS WHO SWITCH TO US:
  Typical profile: [who switches and why]
  Common trigger: [what event causes the switch]

THEIR CUSTOMERS WHO STAY:
  Typical profile: [who stays and why — honest assessment]
  Why we lose: [the real reasons, not excuses]

LANDMINE QUESTIONS (ask prospects to create doubt about competitor):
  "How does [competitor] handle [thing you do better]?"
  "What happens when you [hit a limit/scale beyond their sweet spot]?"
  "Have you looked at [specific area where they're weak]?"
```

Build a battle card for each of your top 3 direct competitors. Update quarterly.

---

## Ongoing Competitive Monitoring

### Monitoring Cadence

| Activity | Frequency | Time investment |
|---|---|---|
| Check competitor social media for major announcements | Weekly | 15 minutes |
| Read competitor newsletter (if subscribed) | As received | 5 minutes per email |
| Check G2 for new reviews | Monthly | 30 minutes per competitor |
| Full pricing page check | Quarterly | 15 minutes per competitor |
| Homepage and positioning review | Quarterly | 10 minutes per competitor |
| Full competitive profile update | Quarterly | 1–2 hours per competitor |
| Review and update battle cards | Quarterly | 30 minutes per card |

### Monitoring Automation

| What to monitor | Tool | Cost |
|---|---|---|
| Competitor pricing page changes | Visualping, ChangeTower | $10–$30/mo |
| Competitor brand mentions on social | Google Alerts (free), Mention ($29/mo) | Free–$29/mo |
| Competitor new content published | RSS feed reader (Feedly free tier) | Free |
| Competitor new features/changelog | Subscribe to their changelog RSS or email | Free |
| New competitor reviews on G2 | G2 email alerts | Free |
| Competitor job postings | LinkedIn job alerts for their company | Free |

**Job posting intelligence:** Competitor job listings reveal strategy. Hiring a "Head of Enterprise" = moving upmarket. Hiring "Developer Advocates" = investing in community. Hiring "Growth Marketer" = scaling paid acquisition. Hiring in a new region = geographic expansion. Check monthly.

### When to Alert the Team

Not every competitor move matters. Alert on:
- Pricing changes (especially downward — competitive pressure)
- New product launch or major feature that directly competes with your wedge
- Major funding round (signals increased competition)
- Acquisition (changes the competitive landscape)
- Major customer wins that are in your target segment

Don't alert on: minor feature updates, blog posts, social media activity, hiring (track it but don't react).

---

## Win/Loss Analysis

Win/loss analysis tracks why deals are won or lost against specific competitors. This is the highest-quality competitive data because it comes directly from buying decisions.

### Collecting Win/Loss Data

**For every sales conversation or trial evaluation where a competitor is mentioned:**

```
Date: [date]
Prospect: [company name, size, role of evaluator]
Competitor(s) evaluated: [list]
Outcome: [won / lost / no decision]

If won:
  Primary reason: [why they chose us — in their words]
  Secondary reasons: [other factors]
  Competitor weakness that helped us: [specific]
  What almost lost the deal: [any concerns they had]

If lost:
  Primary reason: [why they chose the competitor — in their words]
  Secondary reasons: [other factors]
  Our weakness that hurt us: [specific]
  What almost won the deal: [where we were strong]
  
If no decision (chose to do nothing):
  Why: [not urgent enough? budget? build it themselves?]
```

### Analyzing Win/Loss Patterns

After collecting 15–20 data points, look for patterns:

**Win patterns:**
- Which competitor do you win against most often? Why?
- What prospect profile (company size, role, use case) are you winning?
- What feature or capability tips the decision in your favor?
- Is pricing ever the deciding factor? In which direction?

**Loss patterns:**
- Which competitor do you lose to most often? Why?
- What prospect profile are you losing?
- Is there a specific feature gap that causes losses repeatedly?
- Are you losing on product, pricing, brand trust, or something else?

**Strategic implications:**
- If you consistently win against Competitor A but lose to Competitor B, your marketing should target Competitor A's audience and avoid head-on competition with Competitor B.
- If you lose because of a specific feature gap, that's a product priority input.
- If you win on pricing, your pricing positioning is working. If you lose on pricing, either your value isn't clear or you're priced wrong for your market.
- If you lose to "no decision" more than to any single competitor, your real competition is inertia — and your marketing needs to emphasize urgency and cost of inaction.

### Connecting Win/Loss to Other Skills

Win/loss data feeds multiple skills:
- **Positioning language:** Win reasons become marketing copy → route to `saas-copywriting`
- **Audience understanding:** Loss patterns reveal which segments you don't serve well → route to `saas-audience-research`
- **Channel strategy:** Knowing which competitors you beat informs which competitor keywords to bid on → route to `google-ads-for-saas`
- **Product priorities:** Repeated feature-gap losses are product roadmap inputs
- **Pricing adjustments:** Win/loss by price point reveals pricing sensitivity
