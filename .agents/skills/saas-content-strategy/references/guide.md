# Content Strategy: Complete Reference Guide

---

## Table of Contents

1. [Channel Deep-Dives](#channel-deep-dives)
   - [Blog / Long-Form](#blog--long-form)
   - [Documentation](#documentation)
   - [Twitter/X](#twitterx)
   - [LinkedIn](#linkedin)
   - [Email / Newsletter](#email--newsletter)
   - [Video / YouTube](#video--youtube)
   - [Podcast](#podcast)
2. [Editorial Planning](#editorial-planning)
   - [The Prioritized List (Tier 1)](#the-prioritized-list-tier-1)
   - [The 4-6 Week Lookahead (Tier 2)](#the-4-6-week-lookahead-tier-2)
   - [The Quarterly Content Roadmap (Tier 3)](#the-quarterly-content-roadmap-tier-3)
   - [Topic Sourcing Workflows](#topic-sourcing-workflows)
3. [Content Audits](#content-audits)
   - [Full Audit Walkthrough](#full-audit-walkthrough)
   - [Content Audit Spreadsheet Template](#content-audit-spreadsheet-template)
   - [Quick Audit for Smaller Sites](#quick-audit-for-smaller-sites)
4. [Competitor Content Analysis](#competitor-content-analysis)
   - [Competitive Content Inventory Template](#competitive-content-inventory-template)
   - [Gap Analysis Framework](#gap-analysis-framework)
   - [Ongoing Monitoring Setup](#ongoing-monitoring-setup)
5. [Content-Market Fit](#content-market-fit)
   - [Diagnostic Framework](#diagnostic-framework)
   - [The 15-Piece Test](#the-15-piece-test)
   - [Pivot Signals](#pivot-signals)
6. [Repurposing](#repurposing)
   - [The Repurposing Matrix](#the-repurposing-matrix)
   - [Tier 1 Repurposing Workflow](#tier-1-repurposing-workflow)
   - [Tier 2-3 Repurposing System](#tier-2-3-repurposing-system)
7. [Measurement](#measurement)
   - [Metrics Definitions and Benchmarks](#metrics-definitions-and-benchmarks)
   - [Tier 1 Monthly Report Template](#tier-1-monthly-report-template)
   - [Tier 2 Weekly Dashboard](#tier-2-weekly-dashboard)
   - [Tier 3 Full Content Analytics](#tier-3-full-content-analytics)
8. [Content Types for SaaS](#content-types-for-saas)
   - [Types Ranked by Effort and Impact](#types-ranked-by-effort-and-impact)
   - [Content Type Selection by Stage](#content-type-selection-by-stage)

---

## Channel Deep-Dives

### Blog / Long-Form

The blog is the workhorse channel for SaaS content. It compounds via SEO, serves as the hub for repurposing, and establishes thought leadership. But it's also the channel most founders do poorly — because they treat it like a personal journal instead of a strategic asset.

#### When to choose blog as your primary channel
- Your audience searches for answers to problems your product solves
- You enjoy (or can tolerate) writing 800-2000 word pieces
- You're willing to commit to a 6-month horizon before expecting SEO results
- Your product's value proposition requires explanation (not just a screenshot)

#### Blog strategy by tier

**Tier 1 (2-4 posts/month):**

Publish two types of posts:
1. **Problem-solution posts:** Target a specific problem your audience has. Write the best answer on the internet. Mention your product where relevant, but the post should be valuable even without your product.
2. **Opinion/insight posts:** Share a genuine perspective on your industry. These don't need to rank for SEO — they establish credibility and are shareable on social.

*Example cadence — API monitoring product (Tier 1):*
- Week 1: "How to Set Up API Health Checks for Microservices" (problem-solution, SEO target)
- Week 3: "Why Alert Fatigue Is the Real Monitoring Problem" (opinion, shareable)

*Example cadence — SEO keyword research product (Tier 1):*
- Week 1: "How to Find Keywords Your Competitors Miss" (problem-solution, SEO target)
- Week 3: "The Keyword Difficulty Lie: What Actually Predicts Rankings" (opinion, shareable)

**Tier 2 (4-8 posts/month):**

Add to the Tier 1 mix:
3. **Comparison and alternatives posts:** "[Competitor] vs [Your product]" or "[Competitor] alternatives." These target high-intent commercial keywords.
4. **Tutorial/how-to posts:** Detailed technical walkthroughs that demonstrate expertise and attract developers.

*Example additions — API product:*
- "Datadog vs [Your Product]: Which API Monitor Fits Small Teams?"
- "Tutorial: Building a Custom API Monitoring Dashboard with Grafana"

*Example additions — SEO product:*
- "Ahrefs vs Semrush: Which Keyword Tool Is Worth the Price?"
- "Step-by-Step: How to Build a Keyword Research Workflow from Scratch"

**Tier 3 (8+ posts/month):**

Add:
5. **Pillar content:** Comprehensive, 3000+ word guides that serve as the hub for topic clusters. Coordinate with `saas-seo-research` for topic cluster architecture.
6. **Data-driven posts:** Original research, benchmarks, or analyses that attract backlinks and press coverage.
7. **Case studies / customer stories:** Social proof that doubles as SEO content for "[use case] + [category]" keywords.

#### Blog post structure that works for SaaS

```
Title: [Clear benefit or answer to a question — include primary keyword]
Meta description: [Specific outcome the reader will get — 150-160 chars]

Introduction (100-150 words):
- Hook: state the problem or question
- Credibility: why you can speak to this
- Promise: what the reader will learn

Body (organized by subheadings):
- Break into 3-7 sections with clear H2s
- Each section should deliver one complete idea
- Use code blocks, screenshots, or diagrams where relevant
- Include practical examples, not just theory

Conclusion (50-100 words):
- Summarize the key takeaway
- Mention your product IF relevant (don't force it)
- One CTA: try the product, subscribe, or read the next related post
```

### Documentation

For developer tools and API products, documentation IS content strategy. Great docs drive adoption, reduce churn, and rank in search. Bad docs drive users to competitors.

#### When to choose docs as your primary channel
- Your product is an API, SDK, CLI, or developer tool
- Users need to write code to use your product
- Self-serve adoption is your growth model (PLG)
- Your audience trusts documentation more than marketing pages

#### Documentation as content strategy

**Docs-as-marketing approach:**
1. **Getting started guides** that rank for "[category] tutorial" keywords
2. **Integration guides** that rank for "[integration] + [your category]" (e.g., "Stripe webhook monitoring setup")
3. **Conceptual guides** that explain the domain, not just your product (e.g., "Understanding API Rate Limiting")
4. **Migration guides** that target competitor keywords (e.g., "Migrating from Datadog to [Your Product]")

*Example — API monitoring product docs-as-content:*
- Quick start: "Monitor Your First API in 5 Minutes" → ranks for "api monitoring quickstart"
- Integration: "Monitor Stripe Webhooks with [Product]" → ranks for "stripe webhook monitoring"
- Conceptual: "API Monitoring vs APM: What's the Difference?" → ranks for comparison keyword

*Example — SEO product docs-as-content:*
- Quick start: "Your First Keyword Research in [Product]" → ranks for "keyword research tutorial"
- Integration: "Import Google Search Console Data into [Product]" → ranks for "google search console keyword data"
- Conceptual: "Search Intent Types Explained" → ranks for informational keyword, builds topical authority

**Tier 1:** Focus on getting started guide + 3-5 core workflow docs. These serve both users and search engines.

**Tier 2:** Add integration guides, conceptual guides, and a troubleshooting section. Expand docs to cover every major feature with examples.

**Tier 3:** Full documentation site with versioning, API reference, community-contributed guides, and a structured learning path.

### Twitter/X

Twitter/X is the fastest channel to build a personal brand and connect with technical audiences — but it's also the most ephemeral. Posts have a half-life of hours, not months.

#### When to choose Twitter/X as your primary channel
- Your audience is active on Twitter/X (check: search your product category — are people discussing it?)
- You can commit to posting 3-5 times per week
- You're comfortable with short-form, opinionated content
- Your product has visual elements (screenshots, dashboards, results) that work in feeds

#### Content types that work on Twitter/X for SaaS founders

| Content type | Format | Example (API product) | Example (SEO product) |
|---|---|---|---|
| **Insight thread** | 5-10 tweet thread | "Here's what we learned monitoring 10M API calls last month" | "We analyzed 1,000 SERPs. Here's what actually predicts ranking difficulty" |
| **Quick tip** | Single tweet + screenshot | "Pro tip: Set your health check interval to 2x your expected response time, not 1x" | "Quick keyword research hack: Google 'site:reddit.com [topic]' to find real user language" |
| **Building in public** | Progress update | "Just shipped automatic false-alert suppression. Here's how it works [screenshot]" | "This week we added SERP snapshot history. See how rankings change over time [demo]" |
| **Hot take / opinion** | Single tweet or short thread | "Your monitoring tool shouldn't be more complex than your API" | "KD scores are a crutch. Learn to read a SERP instead." |
| **Community engagement** | Reply, quote tweet | Respond to DevOps pain points in your feed | Respond to SEO questions with genuine help |

**Tier 1 cadence:** 3-5 posts/week. Spend 15-20 min/day. Focus on 2 types: quick tips and community engagement (replying to others is free and high-leverage).

**Tier 2 cadence:** 5-7 posts/week plus 1 thread/week. Allocate 30 min/day. Add insight threads derived from blog content.

**Tier 3 cadence:** Daily posting, 2+ threads/week, systematic engagement with industry conversations, DM outreach for partnerships. Likely needs a dedicated person.

### LinkedIn

LinkedIn favors professional insight over technical depth. It's the best channel for reaching non-technical buyers, VPs, and enterprise decision-makers.

#### When to choose LinkedIn as your primary channel
- Your buyer is a manager, VP, or C-suite (not individual contributor developers)
- Your product is sales-led or enterprise-focused
- Your industry values professional credibility
- You sell to non-technical stakeholders who need to understand the business case

#### LinkedIn content types for SaaS

| Content type | Format | Works well for |
|---|---|---|
| **Lesson learned** | Text post, 100-300 words | Establishing founder credibility |
| **Industry observation** | Text post with a strong opening hook | Thought leadership, engagement |
| **Carousel / PDF** | Slide-format visual content | Frameworks, step-by-step guides |
| **Case study mini** | Short customer win story | Social proof, value demonstration |
| **Data point + insight** | Single stat with commentary | High engagement, easy to create |

**Tier 1 cadence:** 2-3 posts/week. LinkedIn rewards consistency over volume. A strong post every other day outperforms mediocre daily posting.

**LinkedIn-specific tips:**
- First line must hook — it's the only line visible before "see more"
- Personal stories outperform company announcements
- No external links in the post body (LinkedIn suppresses reach). Put links in comments.
- Engage with 5-10 relevant posts daily to build visibility in your network's feed

### Email / Newsletter

Email is the only channel where you own the audience. No algorithm changes, no platform risk. But it requires consistent delivery and a reason for people to subscribe.

#### When to choose email as your primary channel
- You have a strong unique perspective that people want regularly
- Your audience makes decisions over time (enterprise sales cycle, considered purchases)
- You want to build a direct relationship with potential buyers
- You already have a growing email list from signups, waitlist, or content

#### Newsletter strategy by tier

**Tier 1 — The simple product newsletter:**
- Frequency: Bi-weekly or monthly. Don't start weekly if you can't sustain it.
- Content: Product updates + one useful tip or insight. That's it.
- Goal: Keep users engaged, reduce churn, stay top-of-mind.
- Template: 1 product update (2-3 sentences), 1 tip of the week (3-5 sentences), 1 CTA.
- Build time: 30-60 minutes per issue.

*Example — API product Tier 1 newsletter:*
```
Subject: [Product] Update: Smarter Alert Grouping + Quick Tip

What's New: We shipped alert grouping — related API errors now consolidate
into a single notification instead of 47 separate ones. [Try it →]

Tip of the Week: If your health check is returning false positives,
try adding a retry with a 2-second delay before alerting. Most transient
errors resolve within one retry. Here's how to set that up: [link to docs]

That's it for this week. Reply to this email if you have questions — I
read every reply.
```

**Tier 2 — The industry newsletter:**
- Frequency: Weekly.
- Content: 1 original insight + 2-3 curated links + 1 product mention.
- Goal: Become a trusted voice in your space, build audience beyond users.
- Build time: 1-2 hours per issue.

**Tier 3 — The content hub newsletter:**
- Frequency: Weekly, with segmented automations.
- Content: Original analysis, exclusive content, curated resources.
- Segments: Users vs. leads, by use case, by engagement level.
- Goal: Nurture pipeline, support sales, build brand.
- Build time: 3-5 hours per issue including planning and design.

### Video / YouTube

Video is high-effort but high-reward for products that benefit from visual demonstration — dashboards, UIs, developer workflows, and anything where seeing is understanding.

#### When to invest in video
- Your product has a visual interface that screenshots can't fully convey
- You (or someone on the team) is comfortable on camera or doing screencasts
- Your audience watches YouTube for learning (developers learning tools, operators learning workflows)
- You have Tier 2+ resources — video is too time-intensive for most Tier 1 founders

#### Video types for SaaS

| Type | Length | Effort | Best for |
|---|---|---|---|
| **Screen recording tutorial** | 5-15 min | Low-medium | Feature demos, setup guides, workflows |
| **Talking head + screen** | 5-20 min | Medium | Thought leadership with demonstration |
| **Short-form (Shorts/Reels)** | 30-90 sec | Low | Tips, quick demos, reach expansion |
| **Webinar recording** | 30-60 min | Medium-high | Deep dives, repurpose as multiple short clips |
| **Customer interview** | 15-30 min | Medium | Social proof, case study content |

**Tier 2 approach:** Start with screen recording tutorials of your product. These are the easiest to produce (no camera, no editing beyond cuts) and serve double duty as documentation. Aim for 2-4 videos/month.

*Example — API product video series:*
- "Set Up API Monitoring in 3 Minutes" (getting started)
- "How to Reduce False Alerts — Live Walkthrough" (feature demo)
- "Monitoring Microservices: Our Architecture Explained" (thought leadership)

*Example — SEO product video series:*
- "Find Your First 10 Keywords in 5 Minutes" (getting started)
- "Live Keyword Research Session: B2B SaaS Example" (practical demo)
- "Why I Ignore Keyword Difficulty Scores" (thought leadership)

**Tier 3 approach:** Dedicated video production with weekly uploads, structured series, community engagement via comments, and repurposing into blog posts and social clips.

### Podcast

Podcasts build deep audience relationships and are excellent for networking (inviting guests creates business relationships). But they have the slowest audience growth of any channel.

#### When to invest in podcast
- You enjoy conversational formats and interviewing people
- You want to build relationships with industry leaders (guests become advocates)
- Your audience has commute or workout time where they consume audio
- You're okay with a slow build — podcasts rarely drive traffic quickly

#### Podcast strategy for SaaS founders

**Tier 2 approach — minimum viable podcast:**
- Format: Interview-style with industry practitioners (not other founders — actual users/buyers)
- Cadence: Bi-weekly or monthly (don't start weekly)
- Length: 20-30 minutes (respect listener time)
- Production: Record via Riverside/Zencastr, basic editing, publish via Buzzsprout/Transistor
- Repurpose: Each episode → 3-5 audiogram clips for social, 1 blog post summary, key quote graphics

**Tier 3 approach:** Weekly episodes with a consistent theme, guest pipeline, professional editing, transcript-based blog posts, and video recording for YouTube cross-posting.

---

## Editorial Planning

### The Prioritized List (Tier 1)

The simplest effective editorial planning tool — a ranked list of topic ideas you draw from when it's time to create.

**Template:**

```
CONTENT BACKLOG
Last reviewed: [date]
Primary channel: [blog / social / etc.]

PRIORITY  │ TOPIC                                         │ TYPE          │ SOURCE
──────────┼───────────────────────────────────────────────┼───────────────┼─────────────
1         │ How to reduce API false alerts                │ Tutorial      │ Support FAQ
2         │ [Competitor] vs [Your Product] for startups   │ Comparison    │ SEO research
3         │ Why we chose [architecture decision]          │ Opinion       │ Founder insight
4         │ Setting up webhooks with [integration]        │ Tutorial      │ User request
5         │ State of API monitoring in 2026               │ Data/insight  │ Industry trend
...
──────────┴───────────────────────────────────────────────┴───────────────┴─────────────

IDEAS PARKING LOT (unranked — add here, prioritize monthly)
- [topic idea]
- [topic idea]
```

**How to maintain it:**
- Add ideas whenever they come up (from support tickets, user conversations, competitor research, personal insights)
- Prioritize monthly: sort by relevance × feasibility × timeliness
- When it's time to create: pick item #1, don't deliberate

### The 4-6 Week Lookahead (Tier 2)

A lightweight calendar that creates accountability without over-planning.

**Template:**

```
EDITORIAL CALENDAR — [Month Year]

WEEK │ DATE   │ TOPIC                                │ CHANNEL │ FORMAT    │ KEYWORD       │ STATUS
─────┼────────┼──────────────────────────────────────┼─────────┼───────────┼───────────────┼────────
1    │ Mar 2  │ How to monitor GraphQL APIs           │ Blog    │ Tutorial  │ graphql api   │ Draft
     │ Mar 3  │ Thread: GraphQL monitoring mistakes    │ Twitter │ Thread    │ —             │ Idea
     │ Mar 5  │ Newsletter: March product updates      │ Email   │ Newsletter│ —             │ Idea
─────┼────────┼──────────────────────────────────────┼─────────┼───────────┼───────────────┼────────
2    │ Mar 9  │ [Competitor] alternative for dev teams │ Blog    │ Comparison│ [comp] alt    │ Idea
     │ Mar 11 │ Quick tip: webhook retry config        │ Twitter │ Single    │ —             │ Idea
─────┼────────┼──────────────────────────────────────┼─────────┼───────────┼───────────────┼────────
3    │ Mar 16 │ API error budget tutorial              │ Blog    │ Tutorial  │ api error     │ Idea
     │ Mar 17 │ LinkedIn: Lessons from 1M API calls    │ LinkedIn│ Post      │ —             │ Idea
─────┼────────┼──────────────────────────────────────┼─────────┼───────────┼───────────────┼────────
4    │ Mar 23 │ Customer story: [Company] monitoring   │ Blog    │ Case study│ —             │ Idea
     │ Mar 25 │ Thread: results from customer story    │ Twitter │ Thread    │ —             │ Idea

Status: Idea → Outline → Draft → Review → Published
```

**How to use it:**
- Fill in 4-6 weeks ahead each Monday
- Pull topics from your prioritized backlog (Tier 1 template feeds this)
- Match topics to channels and formats
- Update status as pieces move through production (hand off to `saas-content-production` for the production workflow)
- Review results at end of month — what performed?

### The Quarterly Content Roadmap (Tier 3)

Quarterly themes tied to business goals, broken into monthly plans.

**Template:**

```
Q2 2026 CONTENT ROADMAP

QUARTERLY THEME: "Enterprise Readiness" (aligned with enterprise launch in June)

STRATEGIC GOALS:
- Rank for 5 new enterprise-related keywords
- Publish 3 enterprise case studies
- Launch bi-weekly enterprise newsletter segment
- Build comparison pages for top 3 enterprise competitors

MONTHLY BREAKDOWN:

APRIL — Foundation
  Blog (8 posts): 3 enterprise tutorials, 2 comparisons, 2 SEO pieces, 1 opinion
  Social (20 posts): Daily LinkedIn, 3 Twitter threads, ongoing engagement
  Email (4 issues): Weekly newsletter with enterprise-focused tips
  Video (2): Enterprise setup walkthrough, customer interview
  New cluster: "Enterprise API Monitoring" — pillar + 4 supporting (coordinate w/ SEO research)

MAY — Acceleration
  Blog (8 posts): 2 case studies, 2 comparisons, 2 tutorials, 1 data piece, 1 opinion
  Social (20 posts): Case study amplification, enterprise pain point threads
  Email (4 issues): Introduce enterprise segment, targeted content
  Video (2): Case study video, feature deep-dive

JUNE — Launch Support
  Blog (10 posts): Launch announcement, migration guides, enterprise FAQ, 4 SEO, 2 comparison
  Social (25 posts): Launch campaign, daily enterprise content
  Email (4 issues): Launch sequence, onboarding for enterprise tier
  Video (4): Launch video, 2 migration guides, enterprise demo

CONTENT BACKLOG: [link to full prioritized backlog]
KEYWORD TARGETS: [link to SEO research deliverable from saas-seo-research]
```

### Topic Sourcing Workflows

Where do content topics come from? Different sources have different signal quality.

| Source | How to extract topics | Signal quality | Examples |
|---|---|---|---|
| **Customer support tickets** | Categorize top 10 repeated questions monthly | Very high — these are real user problems | "How do I set up alerts for specific endpoints?" → tutorial |
| **Sales call recordings** | Note objections and questions that come up repeatedly | Very high — these block purchases | "How is this different from Datadog?" → comparison page |
| **SEO keyword research** | Use `saas-seo-research` to find target keywords with content opportunities | High — search-validated demand | "api monitoring best practices" → comprehensive guide |
| **Community forums** | Browse Reddit, HN, Stack Overflow for questions in your domain | High — real problems, real language | r/devops thread about monitoring fatigue → opinion piece |
| **Competitor content** | Note what competitors publish that gets engagement | Medium — validated but not differentiated | Competitor's popular tutorial → write a better version with your angle |
| **Product updates** | Tie feature releases to content that explains the value | Medium — internal motivation, external value varies | New alert grouping feature → "How to Stop Alert Fatigue" tutorial |
| **Industry trends** | Follow industry news, conference talks, research reports | Medium — timely but may not be evergreen | New API standard release → "What [Standard] Means for Your Monitoring" |
| **Personal insight** | Your unique perspective as a founder/builder | Variable — high if genuine, low if self-serving | "What We Learned Building a Monitoring Tool from Scratch" |

**Tier 1:** Focus on support tickets + SEO research + personal insight. These three sources give you months of content ideas.

**Tier 2:** Add sales calls + competitor analysis + community forums.

**Tier 3:** All sources feeding into a centralized topic backlog with scoring and prioritization.

---

## Content Audits

### Full Audit Walkthrough

A content audit is a systematic review of all existing content to decide what to keep, refresh, consolidate, or remove. It's most valuable after a positioning shift, a long gap in content production, or when traffic is declining.

**Step 1: Export inventory**

Pull a list of every content URL from:
- Your CMS (WordPress, Ghost, etc.)
- Google Search Console → Pages report
- Sitemap XML
- Google Analytics → Pages report

Create a spreadsheet with: URL, title, publish date, word count (approximate), primary keyword (if any).

**Step 2: Add performance data**

For each URL, add:
- Organic sessions (last 90 days) — from Google Analytics or Search Console
- Impressions (last 90 days) — from Search Console
- Conversions attributed — from analytics (if tracked)
- Backlinks — from Ahrefs/Semrush free check or paid tool
- Last updated date

**Step 3: Score each piece**

| Score | Label | Criteria |
|---|---|---|
| 5 | **Star** | High traffic, converting, on-brand, accurate. Don't touch it. |
| 4 | **Strong** | Good traffic or engagement, mostly accurate. Minor refresh only. |
| 3 | **Refresh** | Good topic, but outdated stats, stale examples, or underperforming. Update and republish. |
| 2 | **Consolidate** | Overlaps with another piece. Merge the best parts into one stronger page. |
| 1 | **Remove** | Off-topic, inaccurate, embarrassing, or cannibalizing better pages. Redirect or noindex. |

**Step 4: Create action plan**

Group by action:
- **Keep (score 4-5):** No action needed beyond monitoring.
- **Refresh (score 3):** Prioritize by traffic potential. A score-3 page on a high-volume keyword is the highest-ROI content action you can take — often higher than creating something new.
- **Consolidate (score 2):** Identify merge targets. Pick the URL with the most authority (backlinks, age), merge content there, 301 redirect the others.
- **Remove (score 1):** 301 redirect to the most relevant remaining page, or noindex if no relevant redirect target exists.

### Content Audit Spreadsheet Template

```
| URL | Title | Published | Updated | Words | Keyword | Org Sessions (90d) | Impressions | Conversions | Backlinks | Score | Action | Notes |
|-----|-------|-----------|---------|-------|---------|---------------------|-------------|-------------|-----------|-------|--------|-------|
```

### Quick Audit for Smaller Sites

If you have fewer than 20 content pieces, a formal audit is overkill. Instead:

1. Open Google Search Console → Performance → Pages
2. Sort by impressions (descending)
3. For each page: is the content still accurate and on-brand? Yes → leave it. No → refresh or remove.
4. Check for any pages with 0 impressions over 90 days — these are invisible to Google. Either improve them significantly or remove them.
5. Total time: 30-60 minutes.

---

## Competitor Content Analysis

### Competitive Content Inventory Template

For each competitor, document:

```
COMPETITOR CONTENT INVENTORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━

Company: [name]
URL: [domain]
Content hub URL: [blog / resources / docs URL]

CHANNELS ACTIVE:
  □ Blog       Frequency: ___/month    Quality: Low / Medium / High
  □ Docs       Comprehensiveness: Basic / Good / Excellent
  □ Twitter/X  Followers: ___          Activity: Low / Medium / High
  □ LinkedIn   Followers: ___          Activity: Low / Medium / High
  □ Newsletter Frequency: ___          Subscribers (est): ___
  □ YouTube    Videos: ___             Avg views: ___
  □ Podcast    Episodes: ___           Frequency: ___

TOP 5 CONTENT PIECES (by engagement, shares, or estimated traffic):
1. [title] — [URL] — [topic] — [why it works]
2. [title] — [URL] — [topic] — [why it works]
3. [title] — [URL] — [topic] — [why it works]
4. [title] — [URL] — [topic] — [why it works]
5. [title] — [URL] — [topic] — [why it works]

CONTENT THEMES (what topics do they consistently cover?):
- [theme 1]
- [theme 2]
- [theme 3]

CONTENT GAPS (what do they NOT cover or cover poorly?):
- [gap 1]
- [gap 2]
- [gap 3]

CONTENT STRENGTHS:
- [what they do well]

CONTENT WEAKNESSES:
- [where their content falls short]

OUR OPPORTUNITIES:
- [what we can do differently or better]
```

### Gap Analysis Framework

A content gap is a topic your audience searches for or cares about that your competitors don't cover well — or at all.

**Three types of gaps:**

| Gap type | How to find it | Example (API product) | Example (SEO product) |
|---|---|---|---|
| **Topic gap** | Topics competitors don't cover at all | No competitor writes about "monitoring serverless APIs" | No competitor covers "keyword research for marketplaces" |
| **Quality gap** | Topic is covered, but poorly | Competitor has a thin "API monitoring best practices" post with 300 words and no examples | Competitor's "keyword difficulty" article is outdated and doesn't reflect current SERP realities |
| **Angle gap** | Topic is covered, but only from one perspective | Every competitor writes about monitoring from the ops perspective; nobody writes for the developer who owns the API | Every SEO tool targets agencies; nobody writes for solo SaaS founders doing their own keyword research |

**Finding gaps:**

1. List the top 20 topics in your space (from `saas-seo-research` keyword data + manual competitor review)
2. For each topic, note: who covers it, how well, and from what angle
3. Mark any topic where coverage is missing, thin, or one-dimensional — these are your opportunities
4. Prioritize gaps by: audience relevance, search volume, your ability to create something genuinely better

### Ongoing Monitoring Setup

**Tier 1:** Check competitor blogs monthly. 15 minutes. Note any new topics or formats.

**Tier 2:** Set up Google Alerts for competitor names and key industry terms. Review weekly.

**Tier 3:** Use a tool like Feedly, Semrush content monitoring, or a custom RSS feed to track competitor publishing. Weekly review and log.

---

## Content-Market Fit

### Diagnostic Framework

Content-market fit has three components. All three must be present.

```
Content-Market Fit = Right Audience + Right Topics + Right Channel

Missing "Right Audience":
  You get traffic but they're not your ICP.
  → Revisit targeting. Check keyword intent with saas-seo-research.

Missing "Right Topics":
  Your audience visits but doesn't engage or convert.
  → Revisit topic selection. Are you solving their problems or talking about yours?

Missing "Right Channel":
  Great content, right audience, but no distribution.
  → Revisit channel selection. Are you publishing where they already look?
```

### The 15-Piece Test

Before investing heavily in content infrastructure, validate content-market fit with a minimum experiment.

**How it works:**

1. Choose your primary channel and 2-3 content types
2. Publish 15 pieces over 8-12 weeks
3. Mix formats: 5 problem-solution, 5 opinion/insight, 5 comparison/practical
4. Measure: traffic, engagement, conversions, qualitative feedback
5. Analyze: which content types, topics, and formats performed best?

**What to look for:**

| Signal | Interpretation | Action |
|---|---|---|
| 2-3 pieces get 3x+ the traffic of others | You found a topic vein. Dig deeper. | Create more content on those topics. |
| One format consistently outperforms others | Your audience prefers that format. | Shift your mix toward it. |
| Traffic but zero conversions | Wrong audience or wrong CTA. | Check if traffic is from your ICP. Adjust targeting or add conversion paths. |
| Engagement on social but no blog traffic | Your audience is on social, not searching. | Consider shifting primary channel to social. |
| Crickets everywhere | Wrong channel, wrong topics, or too early to tell. | If < 10 pieces: keep going. If 15+ pieces and still nothing: reassess everything. |

**Tier 1 adaptation:** If you can only do 1-2 pieces/month, run a lighter version: 8-10 pieces over 4-6 months. The signal will be noisier but still directional.

### Pivot Signals

When should you change your content strategy?

| Signal | Timeline to watch | What to consider |
|---|---|---|
| Zero organic traffic growth after 6 months of consistent publishing | 6 months | Are you targeting the right keywords? Is technical SEO blocking indexing? |
| High traffic but zero conversions | 3 months | Wrong audience or missing conversion path. Check analytics for audience match. |
| Content takes too long to produce and you keep missing cadence | 2 months | You chose a format that's too heavy for your tier. Simplify. |
| You dread content creation and it shows in quality | Immediately | Switch format or channel. Content you hate creating will be content nobody wants to read. |
| Your product/positioning has significantly changed | Immediately | Audit existing content. Your old content may now attract the wrong audience. |
| A competitor has dramatically outpaced you in content | Ongoing | Don't panic. Analyze their strategy and find gaps. Competing on volume is usually wrong; compete on quality or angle. |

---

## Repurposing

### The Repurposing Matrix

One source piece can become many derivative pieces. This is the highest-leverage content activity after the initial creation.

**From a single blog post, you can create:**

| Derivative | Effort | Channel | Example |
|---|---|---|---|
| Twitter/X thread | Low (15 min) | Twitter | Pull key insights into a 5-tweet thread |
| LinkedIn post | Low (15 min) | LinkedIn | Rewrite the key takeaway as a personal insight |
| Newsletter section | Low (10 min) | Email | Summarize in 3-5 sentences for newsletter |
| Short video | Medium (30-60 min) | YouTube/social | Screencast walkthrough of the tutorial |
| Infographic / diagram | Medium (30-60 min) | Social / blog | Visualize the framework or data from the post |
| Documentation snippet | Low (15 min) | Docs | Extract the how-to section into docs |
| Slide deck / carousel | Medium (30-60 min) | LinkedIn / SlideShare | Turn key points into slides |
| Podcast topic | Low (reference only) | Podcast | Use the post as a conversation starter |

### Tier 1 Repurposing Workflow

**Rule: Every blog post becomes 3 additional pieces.** Don't create them all on publish day — spread them over the following week.

```
Day 1: Publish blog post
Day 2: Post key insight as a tweet / LinkedIn post
Day 3: Share a tip from the post on social with a link
Day 5: Include a summary in the next newsletter
```

Time investment: ~30 minutes of additional work per blog post.

### Tier 2-3 Repurposing System

**Rule: Every pillar piece becomes 8-12 derivative pieces.**

```
PILLAR PIECE: [Blog post / Video / Webinar]
│
├── Twitter thread (Day 1)
├── LinkedIn post (Day 2)
├── Newsletter summary (Day 3)
├── 3 social graphics with key quotes (Days 3-7)
├── Short video clip (Day 5)
├── Docs snippet if applicable (Day 7)
├── Follow-up blog post expanding on one sub-topic (Week 2)
├── Carousel / slide deck (Week 2)
└── Community post on Reddit / HN if relevant (Week 3)
```

**Tracking template:**

```
| Source Piece | Published | Derivative | Channel | Status | Published Date |
|---|---|---|---|---|---|
| How to Monitor APIs | Mar 1 | Twitter thread | Twitter | Done | Mar 2 |
| How to Monitor APIs | Mar 1 | LinkedIn post | LinkedIn | Done | Mar 3 |
| How to Monitor APIs | Mar 1 | Newsletter mention | Email | Planned | Mar 7 |
| How to Monitor APIs | Mar 1 | Short video | YouTube | Idea | — |
```

---

## Measurement

### Metrics Definitions and Benchmarks

| Metric | Definition | Benchmark (early SaaS) | Benchmark (established SaaS) |
|---|---|---|---|
| **Organic sessions** | Visits from search engines | Growing month-over-month after month 3 | Steady or growing; 40-60% of total traffic |
| **Content conversion rate** | Signups or demos ÷ content page visits | 0.5-2% for blog, 3-8% for comparison pages | 1-3% for blog, 5-15% for comparison pages |
| **Email subscribers** | New subscribers per month | 50-200/month for early-stage | 500+/month for established |
| **Social engagement rate** | (Likes + comments + shares) ÷ followers | 1-3% on LinkedIn, 0.5-2% on Twitter | Same ranges; consistency matters more |
| **Time on page** | Average time visitors spend | 2-4 min for blog posts | 3-6 min for in-depth content |
| **Backlinks earned** | Links from other sites to your content | 1-5 per high-quality post over 6 months | 5-20 per post for authoritative content |
| **Keyword rankings** | Positions for target keywords | Any page 1 ranking in first 6 months is a win | Growing number of page 1 rankings |

### Tier 1 Monthly Report Template

```
CONTENT PERFORMANCE — [Month Year]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PUBLISHED THIS MONTH:
- [title] — [channel] — [date]
- [title] — [channel] — [date]

TRAFFIC:
- Total organic sessions: _____ (vs last month: _____)
- Top content page by traffic: [title] — _____ sessions

CONVERSIONS:
- Content-attributed signups: _____ (even if manually counted)

QUALITATIVE:
- Did anyone share, comment, or mention your content? Y/N
- Notes: ________________________

NEXT MONTH PRIORITIES:
1. [topic]
2. [topic]

Time spent on this report: ~15 minutes
```

### Tier 2 Weekly Dashboard

```
WEEKLY CONTENT DASHBOARD — Week of [date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PUBLISHING:
- Published this week: [list]
- On track for monthly target: Yes / Behind by ___

TRAFFIC (7-day):
- Organic sessions: _____ (vs prior week: _____)
- Top 3 pages: ________
- Any new pages entering top 20 for target keywords? [list]

ENGAGEMENT (7-day):
- Social posts: _____ | Engagement: _____
- Newsletter (if sent): Open rate ____% | Click rate ____%
- Notable social interactions: ________

CONVERSIONS (7-day):
- Content-attributed signups/demos: _____
- Conversion rate from content pages: _____%

ACTIONS:
- What to adjust based on this week's data: ________
```

### Tier 3 Full Content Analytics

Tier 3 content analytics should be integrated into your marketing analytics stack. Key additions beyond Tier 2:

**Attribution modeling:**
- First-touch attribution: which content first brought a customer to the site?
- Multi-touch attribution: which content pieces appeared in the customer journey?
- Content-assisted conversions: pages that appear in the journey even if not the final touchpoint

**Channel performance:**
- Revenue or pipeline attributed per channel
- Cost per lead per channel (if using paid content promotion)
- Channel-specific conversion rates

**Content production metrics:**
- Time from idea to published (content velocity)
- Production capacity: how many pieces per month can you sustain?
- Content backlog depth: how far ahead are you planned?

**Competitive metrics:**
- Share of voice on target keywords (from `saas-seo-research`)
- Competitive content gap closure: how many of the identified gaps have you filled?

---

## Content Types for SaaS

### Types Ranked by Effort and Impact

Not all content types are created equal. This ranking accounts for a typical SaaS product with a technical audience.

| Content type | Effort | SEO impact | Social impact | Conversion impact | Best for |
|---|---|---|---|---|---|
| **Comparison / vs page** | Medium | Very high | Low | Very high | BOFU — capturing buyers actively evaluating |
| **Alternatives page** | Medium | Very high | Low | Very high | BOFU — capturing competitor searchers |
| **Tutorial / how-to** | Medium | High | Medium | Medium | MOFU — demonstrating expertise, helping users |
| **Problem-solution post** | Medium | High | Medium | Medium | TOFU/MOFU — attracting audience by solving real problems |
| **Documentation** | Varies | High (for dev tools) | Low | High (adoption) | All stages for dev tools / API products |
| **Opinion / thought leadership** | Low-medium | Low | Very high | Low | TOFU — building brand, shareable on social |
| **Data / original research** | High | Very high | High | Low | TOFU — attracts backlinks and press |
| **Case study** | Medium-high | Medium | Medium | Very high | BOFU — social proof for buyers |
| **Guest post** | Medium | Medium (backlinks) | Low | Low | Link building, audience expansion |
| **Listicle / roundup** | Low-medium | Medium-high | Medium | Low | TOFU — easy to produce, often ranks well |
| **Product update / changelog** | Low | Low | Low | Medium (retention) | Existing users — keep them engaged |
| **Video tutorial** | High | Medium-high | Medium | Medium | MOFU — visual learners, complex topics |
| **Newsletter** | Medium (ongoing) | None | Low | Medium (nurture) | MOFU/BOFU — nurture and retention |
| **Podcast** | High (ongoing) | Low | Medium | Low | TOFU — brand building, networking |

### Content Type Selection by Stage

**Pre-launch:**
- Landing page copy (hand off to `saas-copywriting`)
- One thought leadership piece
- Basic documentation (if dev tool)

**Post-launch, pre-product-market fit:**
- Problem-solution posts (2-3/month)
- Documentation (ongoing)
- Social content (if your audience is there)
- One comparison page (your product vs. alternatives)

**Post-product-market fit, scaling:**
- Full blog strategy (tutorials + comparisons + opinion)
- Case studies (as soon as you have happy customers)
- Newsletter
- Social across 1-2 platforms
- Comparison and alternatives pages for all major competitors

**Established / growth stage:**
- Everything above, plus:
- Original research / data content
- Video series
- Guest content and partnerships
- Comprehensive topic cluster strategy (coordinate with `saas-seo-research`)