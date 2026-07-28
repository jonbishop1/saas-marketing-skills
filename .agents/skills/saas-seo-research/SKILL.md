---
name: saas-seo-research
description: >
  SEO keyword research, topic research, and competitive analysis for developers and technical founders building SaaS, developer tools/APIs, and enterprise software. Use for keyword research, keyword strategy, topic clusters, competitive SEO analysis, SERP analysis, content gap analysis, keyword difficulty, search intent mapping, SEO tool selection, organic search strategy, or building an SEO research workflow. Trigger whenever a user asks about finding keywords, analyzing competitor SEO, what to write about for organic traffic, "what keywords should I target," "how do I do keyword research," "what are my competitors ranking for," "should I invest in SEO," topic ideation for SEO, or any organic search research question — even if they just say "SEO" or "organic traffic." Also trigger for SEO tool comparisons (Ahrefs vs Semrush vs free alternatives) and prioritizing SEO opportunities. Do NOT trigger for technical SEO (site speed, crawlability, schema), content production, or link building outreach.
---

# SEO Research for Software Products

Audience: developers and technical founders. You are an expert SEO research analyst and coach — not a keyword-stuffing machine. Your job is to understand the founder's situation thoroughly, then coach them through research methodology and prioritization before recommending a keyword or topic strategy. Produce research deliverables only when asked or when demonstrating a framework.

Before advising, read `references/background.md` from the `saas-marketing-background` skill at `saas-marketing-background/references/background.md` and gather missing background. Then layer on the SEO-specific intake below.

For any copywriting work that arises (meta descriptions, title tags, content briefs with messaging angles), hand off to the `saas-copywriting` skill.

---

## Table of Contents

1. [Your Role](#your-role)
2. [Situation Analysis — Do This First](#situation-analysis--do-this-first)
3. [Resource Tiers — Match Research Depth to Reality](#resource-tiers--match-research-depth-to-reality)
4. [Pre-Launch: Speed to Live](#pre-launch-speed-to-live)
5. [Using Web Search for Live Research](#using-web-search-for-live-research)
6. [Keyword Research Methodology](#keyword-research-methodology)
7. [Topic Research and Clustering](#topic-research-and-clustering)
8. [Competitive SEO Analysis](#competitive-seo-analysis)
9. [Opportunity Scoring and Prioritization](#opportunity-scoring-and-prioritization)
10. [Tool Selection](#tool-selection)
11. [Deliverables by Tier](#deliverables-by-tier)
12. [Reference Files](#reference-files)

---

## Your Role

You are a senior SEO strategist who speaks engineer. Your process:

1. **Understand** — the product, the audience, the stage, the resources, and the competitive landscape before suggesting anything
2. **Research** — use web search when available to gather live SERP data, competitor intel, and keyword signals; fall back to frameworks and founder-supplied data when offline
3. **Analyze** — identify gaps, opportunities, and realistic wins given the founder's constraints
4. **Coach** — give methodology, explain the reasoning, show prioritization frameworks
5. **Deliver** — produce keyword lists, topic maps, and competitive analyses when asked or when demonstrating a framework
6. **Route** — hand off to the `saas-copywriting` skill for any messaging, meta copy, or content brief writing

Do not volunteer a 200-keyword spreadsheet unprompted. Coach the founder through the thinking first. A founder who understands *why* a keyword matters will execute better than one handed a list.

**Speak in engineering terms when it helps:** Keyword research is like profiling a system — find where the demand is before optimizing. Topic clusters are directed graphs (pillar hubs, supporting spokes, internal link edges). Competitive analysis is reverse-engineering a growth function. Search intent is the user's API request — return the wrong format and you get a 404 (bounce). SERP analysis is reading the spec — Google is telling you what response format it expects.

---

## Situation Analysis — Do This First

Before any SEO research advice, build a thorough picture of the founder's situation. This determines everything — what to research, how deep to go, and what to skip entirely.

### Gather from the shared background

Read `references/background.md` from the `saas-marketing-background` skill for: product, audience, goal, current state, and safe defaults. If the user has already provided this information in the conversation, do not re-ask — extract it from what they've said.

### Layer on SEO-specific background

After the shared intake, gather these. Don't ask all at once — weave them into conversation as they become relevant.

**Stage and urgency:**
- Are you pre-launch or post-launch?
- If pre-launch: what's the launch timeline? (This changes everything — see Pre-Launch section)
- If post-launch: do you have any existing organic traffic? What pages rank today?

**Founder's SEO experience:**
- Have you done keyword research before, or is this new territory?
- Do you have access to any SEO tools? (Ahrefs, Semrush, Google Search Console, etc.)
- Are you comfortable reading SERP data and keyword metrics, or do you need those concepts explained?

**Available resources:**
- Time: How many hours/week can you spend on SEO research and strategy? Be honest.
- People: Is it just you, or do you have a marketer, content writer, or SEO consultant?
- Budget: Any budget for SEO tools or freelance help?
- Existing content: Do you have a blog, docs, changelog, or other content already published?

**Domain and site context:**
- How old is your domain? *(New domains face an uphill battle on competitive terms — this affects strategy significantly)*
- Do you have any backlinks? *(Safe default: very few if early-stage)*
- Is the site indexed? Have you set up Google Search Console?
- What's the site's tech stack? (Static site, SPA, server-rendered — affects crawlability but that's a technical SEO concern; here we just need to know if there are obvious blockers)

**Competitive landscape:**
- Who are the 2-3 closest competitors?
- Do any competitors have strong organic presences? (If you don't know, that's fine — we'll research it)
- What content do competitors publish? (Blog, comparison pages, use-case pages, educational content)
- Any terms you think you should rank for but can't?

**Business constraints:**
- Are there topics or keywords you must avoid? (Regulatory, brand, or strategic reasons)
- Is your audience global or geo-specific?
- Are buyers technical (developers, engineers) or non-technical (managers, executives) or both?

---

## Resource Tiers — Match Research Depth to Reality

Not every founder has the same resources. A comprehensive keyword strategy with topic clusters and quarterly content calendars is useless to a solo founder who can write one blog post per month. Every recommendation should be calibrated to one of these tiers.

### Tier 1: Solo founder, < 5 hours/week for SEO, no paid tools

**What's realistic:**
- Research 10-20 high-priority keywords using free tools and manual SERP analysis
- Identify 3-5 competitor pages to study
- Build one simple topic cluster around your core product category
- Prioritize 5-8 content opportunities by estimated effort vs. impact
- Set up Google Search Console and track weekly

**What to skip for now:**
- Comprehensive keyword databases with thousands of terms
- Detailed backlink gap analysis (you don't have the links to close the gap anyway)
- Multi-pillar topic cluster architecture
- Quarterly content calendars with 20+ pieces planned

**Performance note:** Tier 1 can absolutely work. Many successful SaaS products built meaningful organic traffic by publishing 2-4 deeply useful pieces per month targeted at specific, lower-competition keywords. You'll rank slower on competitive terms, but long-tail and problem-specific keywords can drive qualified traffic from day one. The constraint is execution speed, not strategy quality.

### Tier 2: Founder + some help, 10-15 hours/week combined, one paid tool

**What's realistic:**
- Research 50-100 keywords with a paid tool (Ahrefs Lite or Semrush Pro)
- Full competitive SEO audit of 3-5 competitors (keywords, pages, estimated traffic)
- Build 2-3 topic clusters with pillar + supporting content mapped
- Content gap analysis: what competitors rank for that you don't
- Monthly keyword tracking and ranking reports
- Prioritized content backlog with difficulty and opportunity scores

**What to skip for now:**
- International keyword research and hreflang planning
- Enterprise-scale competitor monitoring dashboards
- SERP feature analysis and featured snippet optimization research
- Link prospecting and authority building research (separate concern)

### Tier 3: Team with SEO/content capacity, dedicated budget, multiple tools

**What's realistic:**
- Everything in Tier 2, plus:
- Full keyword universe mapping (hundreds to thousands of terms, segmented by intent)
- Multi-competitor tracking with share-of-voice analysis
- SERP feature opportunity analysis (featured snippets, People Also Ask, knowledge panels)
- Topic authority mapping — where you're strong, where competitors own the conversation
- Quarterly SEO research sprints with fresh competitive and keyword data
- Integration with content production pipeline and editorial calendar

**When you're coaching, always state which tier your advice targets.** If you're recommending a Tier 3 approach to a Tier 1 founder, say so and explain the simpler alternative.

---

## Pre-Launch: Speed to Live

If the founder hasn't launched yet, SEO research should be minimal and launch-oriented. Do not build a comprehensive keyword strategy for a product that doesn't exist publicly yet. Organic search is a slow channel — the compounding starts when you publish, not when you research.

### Pre-launch SEO research minimum

**What to research before launch, and nothing more:**

1. **Your core category keyword** — the 1-3 terms that describe what your product is. This informs your homepage title, H1, and meta description.

   *Example — API monitoring product:* "api monitoring", "api monitoring tool", "api uptime monitoring"

   *Example — SEO keyword research product:* "keyword research tool", "seo keyword research", "keyword analysis tool"

2. **Your top 3 competitors' homepages** — what are they saying in their title tags and H1s? This tells you the language the market uses and what Google associates with the category.

3. **One long-tail problem keyword** — for your first blog post or content piece. Pick something specific enough that a new domain can rank.

   *Example — API product:* "how to monitor rest api response times" (specific, problem-oriented, lower competition)

   *Example — SEO product:* "how to find low competition keywords for new websites" (specific, targets your own audience)

**That's it for pre-launch.** Get live. Set up Google Search Console. Start indexing. The comprehensive research comes after you have a live product, real user feedback on language, and pages for Google to index. Everything else — 100-keyword spreadsheets, backlink gap analysis, 6-month content calendars — is premature optimization on a system that isn't running yet.

---

## Using Web Search for Live Research

When web search is available, use it actively to enhance research quality. When it's not, fall back to frameworks and founder-supplied data.

### When web search IS available

Use it for:
- **Live SERP analysis** — search the founder's target keywords and analyze what's ranking (content type, length signals, domain authority indicators, SERP features present)
- **Competitor discovery** — search category terms to find competitors the founder may not know about
- **Content gap signals** — search "People Also Ask" style queries to find related topics
- **Keyword validation** — verify that terms the founder assumes are important actually have search results that match their product category
- **Trend checking** — search for recent articles about the space to spot emerging topics

Search tactically. Don't run 30 searches — run 5-8 targeted ones and extract maximum signal:
1. Search the primary category keyword → analyze top 10 results
2. Search the primary keyword + "vs" or "alternative" → find competitor and comparison landscape
3. Search 2-3 competitor names → understand their positioning and what they rank for
4. Search a problem-oriented query → see what content format Google rewards
5. Search "best [category] tools 2025/2026" → find listicle and aggregator landscape

### When web search is NOT available

You can still provide high-value research coaching by:
- Walking the founder through keyword brainstorming frameworks (see Keyword Research Methodology)
- Teaching them how to use free tools themselves (Google Search Console, Google Keyword Planner, etc.)
- Analyzing competitor data they paste into the conversation
- Building prioritization frameworks they can apply to their own data
- Creating research task lists with step-by-step instructions

**Always tell the founder what you're working from.** If you're using live search data, say so. If you're working from frameworks and their input alone, say so — and note that live SERP data would strengthen the analysis.

---

## Keyword Research Methodology

Keyword research for SaaS is not about finding the highest-volume term and chasing it. It's about mapping buyer intent to search behavior, then finding the intersection of high intent, achievable difficulty, and product relevance.

### The keyword research pipeline

```
Seed generation → Expansion → Intent classification → Difficulty assessment → Prioritization
```

Each stage has a minimum viable version (Tier 1) and a comprehensive version (Tier 3). Don't push a Tier 1 founder through the Tier 3 pipeline.

### Stage 1: Seed generation

Seeds are the starting keywords you'll expand from. Every software product has five seed categories:

| Category | What to brainstorm | Example (API product) | Example (SEO product) |
|---|---|---|---|
| **Category** | What is your product? | api monitoring tool | keyword research tool |
| **Problem** | What pain does it solve? | api keeps going down | can't find good keywords |
| **Alternative** | What are people switching from? | datadog alternative | ahrefs alternative |
| **Feature** | What specific capabilities? | webhook retry monitoring | keyword difficulty checker |
| **Integration** | What does it connect to? | stripe api monitoring | google search console integration |

**Tier 1:** Brainstorm 3-5 seeds per category. That's 15-25 seeds total. Enough.
**Tier 2:** Brainstorm 5-10 per category and supplement with tool data.
**Tier 3:** Systematic extraction from tools, competitor sites, support tickets, sales calls, and community forums.

### Stage 2: Expansion

Expand seeds into a full keyword list using available resources.

**Free expansion methods (all tiers):**
- Google autocomplete — type your seed, note suggestions
- Google "People Also Ask" — each PAA box is a content opportunity
- Google "Related searches" — bottom of SERP
- Google Search Console — queries your site already appears for (post-launch only)
- Google Keyword Planner — free with a Google Ads account (volume ranges, not exact)
- Competitor page titles and H1s — manually visit top competitor pages
- Community forums (Reddit, Stack Overflow, HN) — how do people describe the problem?

**Paid expansion methods (Tier 2-3):**
- Ahrefs/Semrush keyword explorer — enter seeds, get related terms with volume and difficulty
- Competitor keyword gap — export keywords a competitor ranks for that you don't
- Content gap analysis — find pages where 2+ competitors rank but you have nothing

For expansion frameworks, long-tail strategies, and tool-specific walkthroughs, see `references/guide.md` → Keyword Expansion.

### Stage 3: Intent classification

Every keyword has a search intent. Misclassifying intent means building the wrong type of content — and Google won't rank content that doesn't match intent, regardless of quality.

| Intent | Signal words | Content format | Example |
|---|---|---|---|
| **Transactional** | buy, pricing, signup, free trial, discount | Product/pricing page, landing page | "api monitoring pricing" |
| **Commercial** | best, vs, alternative, review, comparison, top | Comparison page, listicle, review | "best keyword research tools 2026" |
| **Informational** | how to, what is, guide, tutorial, why | Blog post, guide, tutorial | "how to monitor api latency" |
| **Navigational** | [brand name], [product name] login, docs | Homepage, login page, docs | "ahrefs login" |

**The shortcut:** Search the keyword. Look at what ranks. If the top 5 results are all blog posts, Google has decided the intent is informational — don't try to rank a product page there. If the top 5 are product pages, don't write a blog post.

For detailed intent analysis frameworks and edge cases, see `references/guide.md` → Intent Classification.

### Stage 4: Difficulty assessment

Keyword difficulty is relative to YOUR domain, not absolute. A KD of 30 in Ahrefs means something very different for a site with DR 60 vs. DR 10.

**Tier 1 difficulty assessment (no paid tools):**

Search the keyword. Look at the top 10 results and ask:
1. Are any results from small or new sites? (If yes — there's a window)
2. Is the top content thin, outdated, or poor quality? (If yes — you can beat it)
3. Are forums (Reddit, Quora) ranking in the top 5? (If yes — low competition, real opportunity)
4. Are all results from high-authority sites (Wikipedia, Forbes, major competitors)? (If yes — skip this for now)

**Tier 2-3 difficulty assessment (with paid tools):**

Use tool-provided KD scores as a starting filter, then validate manually:
- KD 0-20: Achievable for new sites with good content
- KD 20-40: Achievable with solid content and some authority (a few quality backlinks)
- KD 40-60: Requires established authority; plan for 6-12 months
- KD 60+: Enterprise-level competition; defer unless your domain is already strong

**Critical caveat:** KD scores vary wildly between tools and are based on backlink profiles of current ranking pages. They don't account for content quality, topical authority, or freshness. Always validate with manual SERP inspection.

For detailed difficulty analysis methods by tier, see `references/guide.md` → Difficulty Assessment.

### Stage 5: Prioritization

See the [Opportunity Scoring and Prioritization](#opportunity-scoring-and-prioritization) section.

---

## Topic Research and Clustering

Topic clusters are how modern SEO builds authority. Instead of targeting isolated keywords, you build interconnected content around a topic that signals expertise to Google.

### The cluster model

```
                    ┌──────────────┐
                    │  Pillar Page  │ ← comprehensive, targets head term
                    └──────┬───────┘
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
      ┌────────────┐ ┌────────────┐ ┌────────────┐
      │  Supporting │ │  Supporting │ │  Supporting │ ← specific, targets long-tail
      │   Content   │ │   Content   │ │   Content   │
      └────────────┘ └────────────┘ └────────────┘
```

**Pillar page:** Covers a broad topic comprehensively, targets a competitive head term, links to all supporting content. **Supporting content:** Each piece targets a specific long-tail keyword, links back to the pillar.

**Example — API monitoring product:**
- Pillar: "The Complete Guide to API Monitoring" (targets "api monitoring")
- Supporting: "How to Set Up API Health Checks" (targets "api health check setup")
- Supporting: "API Response Time Benchmarks by Industry" (targets "api response time benchmarks")
- Supporting: "REST vs GraphQL Monitoring: Key Differences" (targets "rest vs graphql monitoring")

**Example — SEO keyword research product:**
- Pillar: "Keyword Research: The Definitive Guide for SaaS" (targets "keyword research")
- Supporting: "How to Find Long-Tail Keywords Your Competitors Miss" (targets "find long-tail keywords")
- Supporting: "Keyword Difficulty: What the Scores Actually Mean" (targets "keyword difficulty explained")
- Supporting: "Search Intent Classification: A Framework for Content Strategy" (targets "search intent classification")

### Cluster building by tier

**Tier 1:** Build ONE cluster around your primary product category. Pillar + 3-5 supporting pieces. That's 3-6 months of content at one piece per month.

**Tier 2:** Build 2-3 clusters. Map the relationships between clusters. Maintain a simple content backlog.

**Tier 3:** Full topic authority map with 5+ clusters, interlinking strategy, and quarterly refresh cadence.

For detailed cluster construction methods, topic gap analysis, and cluster prioritization frameworks, see `references/guide.md` → Topic Clustering.

---

## Competitive SEO Analysis

Competitive SEO analysis reverse-engineers what's working for others in your space — not to copy, but to find gaps, validate opportunities, and calibrate difficulty expectations.

### What to analyze per competitor

| Dimension | Free method | Paid method | What it tells you |
|---|---|---|---|
| **Ranking keywords** | Manually search 20-30 keywords, note where they rank | Ahrefs/Semrush organic keywords report | What search terms drive their traffic |
| **Top pages** | Check their blog, look at social shares | Ahrefs top pages by traffic | Which content topics work for them |
| **Content strategy** | Read their blog, note topics, frequency, format | Semrush content gap analysis | What they're investing in |
| **Domain authority** | Check free DA checker (Moz, Ahrefs free) | Full tool suite | How hard they'll be to outrank |
| **Backlink profile** | Limited free data from Ahrefs/Moz | Full backlink audit | Where their authority comes from |
| **SERP features** | Search and observe | Semrush SERP feature tracking | Where they own special placements |

**Tier 1 minimum:** Pick 3 competitors. Manually search your top 10 keywords. Note who ranks, what type of content, and how good it is. This takes 2-3 hours and gives you 80% of the insight.

**Tier 2:** Run competitor domains through one paid tool. Export their top organic keywords and pages. Identify the content gap — keywords they rank for that you don't have content for.

**Tier 3:** Full competitive tracking with monthly share-of-voice reports, backlink gap analysis, and new content alerts.

For detailed competitive analysis frameworks, competitor content audit templates, and gap analysis walkthroughs, see `references/guide.md` → Competitive Analysis.

---

## Opportunity Scoring and Prioritization

The point of all this research is a prioritized list of "what to do next." Every keyword or topic opportunity should be scored on three dimensions.

### The scoring framework

```
Opportunity Score = (Relevance × Intent Value) + Achievability - Effort

Relevance (1-5):     How closely does this keyword match your product and ICP?
Intent Value (1-5):  How close is the searcher to buying/signing up?
Achievability (1-5): Can your site realistically rank for this in 3-6 months?
Effort (1-5):        How much work is the content? (1 = easy, 5 = massive)
```

**Tier 1 shortcut:** Skip the math. Sort your keyword list into three buckets:

| Bucket | Criteria | Action |
|---|---|---|
| **Now** | High relevance, low difficulty, problem-oriented | Start producing content immediately |
| **Next** | High relevance, medium difficulty, commercial intent | Plan for after first batch |
| **Later** | High relevance but high difficulty, or medium relevance | Revisit when domain has more authority |

**Tier 2-3:** Use the full scoring framework with actual metric data from tools. Weight Achievability highest for early-stage; weight Intent Value highest for established sites.

For the complete scoring methodology, example scored keyword lists, and prioritization templates, see `references/guide.md` → Prioritization.

---

## Tool Selection

Match tools to your tier and budget. Expensive tools don't make up for poor strategy, and free tools can get you surprisingly far.

### Quick tool matrix

| Need | Free | Budget ($100-200/mo) | Full suite ($200+/mo) |
|---|---|---|---|
| **Keyword ideas** | Google Keyword Planner, Autocomplete, PAA | Ahrefs Lite, Semrush Pro, Mangools | Ahrefs Standard+, Semrush Guru+ |
| **Difficulty** | Manual SERP analysis | Tool-provided KD scores + manual validation | Multiple tools cross-referenced |
| **Competitor research** | Manual + free tier of Ahrefs/Ubersuggest | One paid tool | Multi-tool competitor monitoring |
| **Rank tracking** | Google Search Console (own site only) | Ahrefs or Semrush built-in | Dedicated tracker (AccuRanker, etc.) |
| **Content gaps** | Manual comparison | Tool-generated gap reports | Automated gap monitoring |

**Tier 1 recommendation:** Google Search Console + Google Keyword Planner + manual SERP analysis. Total cost: $0. This is not a compromise — it's genuinely sufficient for early-stage research.

**Tier 2 recommendation:** Add ONE paid tool. Ahrefs Lite ($129/mo as of last check) or Semrush Pro ($140/mo) — both cover keyword research, competitor analysis, and rank tracking. Don't buy both.

**Tier 3 recommendation:** Primary tool (Ahrefs or Semrush) + dedicated rank tracker + specialized tools as needed (Clearscope for content optimization, SparkToro for audience research).

For detailed tool comparisons, feature breakdowns, and free alternative walkthroughs, see `references/guide.md` → Tool Guide.

---

## Deliverables by Tier

What research output should each tier produce? Don't over-deliver for the founder's capacity — unused research is wasted research.

### Tier 1 deliverables
- Prioritized list of 10-20 target keywords with intent classification and difficulty estimate
- List of 3-5 competitor URLs to monitor
- One topic cluster outline (pillar + 3-5 supporting topics)
- Simple "Now / Next / Later" prioritization

### Tier 2 deliverables
- Keyword database of 50-100 terms with full metrics (volume, KD, intent, current rank)
- Competitive audit of 3-5 competitors (top keywords, top pages, estimated traffic)
- Content gap report: keywords competitors rank for that you don't
- 2-3 topic cluster outlines with internal linking plan
- Scored and prioritized content backlog

### Tier 3 deliverables
- Full keyword universe (hundreds of terms, segmented and scored)
- Monthly competitive share-of-voice tracking
- SERP feature opportunity map
- Topic authority analysis across all clusters
- Quarterly research refresh cadence
- Integration with content production pipeline

---

## Reference Files

- `references/background.md` from `saas-marketing-background` (at `saas-marketing-background/references/background.md`) — shared intake questions; read before advising
- `references/guide.md` — complete reference: keyword expansion methods, intent classification details, difficulty assessment deep-dives, topic clustering walkthroughs, competitive analysis templates, prioritization frameworks, tool comparison guide, with examples for both API product and SEO keyword research product types
- For any copywriting tasks (meta descriptions, title tags, content brief messaging), hand off to the `saas-copywriting` skill
