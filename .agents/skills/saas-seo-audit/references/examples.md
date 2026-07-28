# Worked Examples

Two complete examples showing how the SEO audit skill works end-to-end: from intake through situation assessment, audit findings, and prioritized action plan. These examples demonstrate how recommendations change based on the founder's actual situation.

---

## Table of Contents

1. [Example 1: API Monitoring Product (Early-Stage, Solo Founder, No SEO Tools)](#example-1-api-monitoring-product)
2. [Example 2: SEO Keyword Research Tool (Growth-Stage, Small Team, Has Tools)](#example-2-seo-keyword-research-tool)

---

## Example 1: API Monitoring Product

### Scenario: PingForge

**The founder:** Solo technical founder. Senior backend engineer, 8 years experience. Built and shipped the product. Zero marketing experience, zero SEO experience. "I've heard of keyword research but I've never done it." Comfortable with terminals, APIs, and debugging — not comfortable with content writing or outreach.

**The product:** API uptime and latency monitoring for developer teams. 5 months post-launch. ~80 paying customers. The site is built on Next.js (SSR enabled for marketing pages, SPA for the app dashboard). Has a blog with 6 posts written by the founder — mostly technical deep-dives on API reliability topics.

**Current organic state:**
- ~200 organic visits/month (per Google Analytics)
- Google Search Console set up 3 months ago
- Top ranking keyword: "api latency percentiles explained" at position 8 (one of the blog posts)
- No other keywords ranking in top 20
- 12 referring domains (mostly directories: Product Hunt, SaaSHub, HackerNews thread)

**Tools:** Google Search Console, Google Analytics. No paid SEO tools. Budget of ~$50-100/month available if needed.

**Time:** 3–4 hours per week for SEO, on top of product work.

**Competitors mentioned:** "Datadog is the big player but they're way broader than us. Better Uptime is closest to us — their blog seems to rank for a lot of stuff. Uptime Robot is the cheap option, they've been around forever and rank for everything. I don't think I can compete with any of them on content volume."

---

### Situation Assessment

**Launch stage:** Post-launch, ~200 organic visits/month. → Foundation-building stage. Enough data to make informed decisions, but early enough that getting the fundamentals right matters more than optimization.

**SEO experience:** Zero. → Explain everything in engineering terms. Map concepts to systems he knows. Don't assume any SEO vocabulary.

**Technical skill level:** Strong backend engineer, Next.js app with SSR. → Technical SEO will be easy for him to execute. The site is likely in decent technical shape already. Focus coaching on content and link strategy, not technical implementation.

**Available tools:** Free only, but $50–100/mo budget available. → Recommend Ahrefs Lite ($29/mo for the Starter plan) or Semrush's entry plan once we establish that the content gap analysis justifies it. Start with the free audit using Search Console + Screaming Frog, then decide.

**Time available:** 3–4 hours/week. → Tier 1–2 hybrid. Can do more than bare minimum but can't run a full content program. Every hour must be high-ROI.

**Competitive landscape (in their words):** Feels outmatched but has correctly identified the competitive field. Hasn't analyzed competitors' actual SEO strategies — just has a general sense. This is common. The audit will reveal specific, actionable gaps.

---

### Recommended Tier: Tier 2 (with Tier 1 time constraints)

A Tier 2 audit with a Tier 1 time budget. We'll use one paid tool to get competitive intelligence, then execute only the highest-priority actions within the 3–4 hours/week constraint.

**Step 1: Technical audit first (week 1, ~2 hours)**

Run Screaming Frog free crawl on pingforge.com. With a Next.js SSR site and likely under 500 pages, the free tier covers the full site.

Expected findings for a 5-month-old Next.js SaaS site:
- Likely fine: HTTPS, mobile responsiveness, basic crawlability (Next.js handles this well by default)
- Check: Are all 6 blog posts indexed? Use Search Console → URL Inspection for each
- Check: Are there any accidental noindex tags? (Common with Next.js when `noindex` is set in development and not removed)
- Check: Core Web Vitals — Next.js sites sometimes have LCP issues if the hero section loads images without priority
- Check: Does the sitemap exist and include all public pages?
- Check: Is the app dashboard (`/dashboard/*`) excluded from crawling? It should be.

Given the tech stack, the technical audit will likely produce 2–5 minor fixes, not major blockers. If the site is fundamentally broken technically, that changes the plan — but for a well-built Next.js app, this is unlikely.

**Step 2: Content audit (week 1–2, ~3 hours)**

Inventory the 6 blog posts + marketing pages:

| Content | Expected finding |
|---|---|
| 6 blog posts | Probably well-written (engineer who writes well) but not keyword-targeted. Topics chosen based on founder interest, not search demand. |
| Homepage | May describe the product well for direct visitors but probably doesn't target any keyword effectively. |
| Pricing page | Exists, probably not optimized for "api monitoring pricing" or similar keywords. |
| Feature pages | May not exist as separate pages — common miss for SaaS sites. |
| Docs | If public and indexed, could be a content asset. If behind login or not indexed, missed opportunity. |

Key assessment: The one post ranking (#8 for "api latency percentiles explained") proves the site can rank when content happens to match search intent. The other 5 posts probably target topics with no search volume or too much competition.

**Step 3: Competitive analysis (week 2, ~2 hours with paid tool)**

This is where a paid tool earns its cost. Sign up for Ahrefs Lite.

Run content gap analysis: pingforge.com vs. betteruptime.com vs. uptimerobot.com

Expected findings:
- Better Uptime likely ranks for 200–500 keywords with content covering the monitoring and uptime space comprehensively
- Uptime Robot likely ranks for 1,000+ keywords due to age and authority
- The gap will reveal dozens of keywords where competitors rank but PingForge doesn't — many of which are achievable

Categorize the top 20–30 gap keywords into:
1. **Bottom-funnel (act now):** "api monitoring tools", "api monitoring free", "better uptime alternatives", "uptime robot alternative for developers"
2. **Mid-funnel (next quarter):** "how to monitor api endpoints", "api uptime monitoring best practices", "api monitoring vs apm"
3. **Top-funnel (later):** "what is api monitoring", "api reliability best practices", "sla calculator"

**Step 4: Backlink assessment (week 2, ~1 hour)**

Using Ahrefs, compare link profiles:
- PingForge: likely 12–20 referring domains
- Better Uptime: likely 200–500 referring domains
- Uptime Robot: likely 1,000+ referring domains

The gap is large but expected. The good news: many of Better Uptime's links are probably from directories and tool roundups that PingForge can also get listed on.

---

### Prioritized Action Plan

Given 3–4 hours/week, here are the top 3 priorities for months 1–3:

**Priority 1: Create 3 bottom-funnel pages (month 1)**

These pages directly capture buying-intent traffic:

1. **Comparison page:** "PingForge vs Better Uptime" — targeting "[competitor] vs" and "[competitor] alternative" searches
2. **Alternative page:** "Better Uptime Alternatives for Developer Teams" — targeting alternative-seeking searches
3. **Category page:** Optimize the homepage or create a landing page targeting "api monitoring tool for developers"

Why these first: Bottom-funnel content converts at the highest rate. One visitor searching "better uptime alternative" is worth 50 visitors searching "what is api monitoring." These pages are also relatively easy for a technical founder to write — they're comparing products, not writing thought leadership.

Time: ~4–5 hours total. One page per week for 3 weeks.

**Priority 2: Optimize the existing ranking post (month 1)**

The post ranking #8 for "api latency percentiles explained" is close to driving real traffic. Optimize it:
- Improve the title tag for CTR
- Add missing subtopics that top-ranking competitors cover
- Add internal links from this post to the new comparison page and homepage
- Expand if needed based on what competitors include

Time: ~2 hours.

**Priority 3: Submit to directories and build integration links (months 1–2)**

Low-effort link building:
- Submit to G2, Capterra, AlternativeTo, StackShare (if not already listed)
- For each integration PingForge has (Slack, PagerDuty, etc.), check if the partner has a marketplace or integrations page that lists partners. Request listing.

Time: ~3–4 hours total, one-time effort.

**Month 2–3 content calendar:**

| Week | Content piece | Target keyword | Type |
|---|---|---|---|
| 5 | "How to Monitor API Endpoints: A Developer's Guide" | "how to monitor api endpoints" | How-to guide |
| 6 | "API Monitoring vs APM: What's the Difference?" | "api monitoring vs apm" | Comparison/educational |
| 7 | Refresh + optimize post #2 from the existing blog | (depends on audit of existing posts) | Content refresh |
| 8 | "Uptime Robot vs PingForge" (if the founder is comfortable with direct comparison) | "uptime robot alternative" | Comparison page |

**What's intentionally deferred:**
- Link outreach (not enough content to promote yet — build content first)
- Guest posting (time-intensive; premature at this stage)
- Programmatic SEO (needs more content foundation first)
- Advanced technical SEO (site is probably fine technically)
- Top-funnel educational content (low conversion, save for later)

**Expected results in 6 months:**
- Organic traffic: 200/mo → 800–1,500/mo (realistic for Tier 2 effort on a new domain)
- Keywords ranking top 20: from ~1 to 15–25
- Referring domains: from 12 to 30–50
- First organic signups from comparison/alternative pages by month 3–4

---

## Example 2: SEO Keyword Research Tool

### Scenario: KeyScope

**The founders:** Two-person team — one technical founder (full-stack engineer) and one growth co-founder with 4 years of digital marketing experience, including SEO for a previous company. The growth co-founder drives SEO strategy.

**The product:** Keyword research tool focused on keyword gap analysis and opportunity scoring. 10 months post-launch. 340 paying customers. Organic traffic: ~4,200 visits/month and growing. The site is on Webflow (marketing site) with a React SPA for the app.

**Current organic state:**
- 4,200 organic visits/month, up from 1,800 six months ago
- 380 keywords ranking in top 100, 45 in top 20
- Top pages by organic traffic: "best keyword research tools" (blog post, ranks #11), "keyword gap analysis" (blog post, ranks #6), "what is keyword difficulty" (blog post, ranks #4)
- 23 blog posts published over 10 months
- 186 referring domains
- DR 38 (Ahrefs)

**Tools:** Ahrefs Standard subscription, Google Search Console, Google Analytics 4, Screaming Frog paid license.

**Time:** Growth co-founder dedicates ~15 hours/week to marketing overall, of which ~8 hours go to SEO and content. Technical founder helps with technical SEO issues and builds free tools.

**Competitors mentioned:** "Ahrefs and Semrush are the giants — we can't compete with them head-on. Our real SEO competitors are SE Ranking, Mangools, and Ubersuggest. We're all fighting for the same long-tail keywords. Mangools seems to punch above their weight in SEO — their blog ranks really well. SE Ranking has more content but it's more generic. We want to own the 'keyword gap analysis' and 'opportunity scoring' space."

---

### Situation Assessment

**Launch stage:** Growth stage, 4,200 organic visits/month, 340 customers. → Full audit with optimization focus. They have data, assets, and momentum. The goal is to accelerate and fix leaks, not build from scratch.

**SEO experience:** Growth co-founder has real experience. → Skip basics entirely. Coach at the strategy level. Challenge their assumptions where needed. They need a sparring partner, not a teacher.

**Technical skill level:** Full-stack engineer + Webflow. → Technical SEO is well-covered. Webflow has some SEO limitations (no server-side rendering, limited URL control) — flag these. The technical founder can build free tools and programmatic pages.

**Available tools:** Full Ahrefs + Screaming Frog paid. → Tier 3 audit depth is possible. All data is available.

**Time available:** ~8 hours/week for SEO. → Tier 3 is feasible. Full program with content creation, optimization, and link building.

**Competitive landscape (in their words):** Sophisticated understanding. Correctly identified the real competitive set (not Ahrefs/Semrush but the mid-market tools). Has a clear positioning thesis ("own keyword gap analysis"). This is a strong foundation. The audit should validate or challenge the positioning with data.

---

### Recommended Tier: Tier 3 — Systematic

Full audit across all three pillars with a strategic focus on accelerating the existing organic growth trajectory.

### Technical Audit Findings

Run a full Screaming Frog crawl with JavaScript rendering enabled.

**Webflow-specific issues to check:**

| Issue | Webflow concern | Impact |
|---|---|---|
| URL structure | Webflow forces `/blog/post-slug` structure — can't customize without workarounds | Low — the structure is fine for SEO |
| Site speed | Webflow sites can be slower than static/SSR due to their rendering approach | Medium — check CWV scores |
| Programmatic pages | Webflow CMS has limits on programmatic page generation | Medium — may constrain programmatic SEO |
| Canonical handling | Webflow auto-generates canonicals correctly in most cases | Low — verify anyway |
| JavaScript dependencies | Webflow uses JavaScript for interactions — ensure content isn't dependent on JS execution | Medium — audit specific pages |

Expected technical findings for a well-maintained Webflow site:
- CWV may show LCP issues (Webflow's rendering pipeline isn't the fastest)
- Image optimization likely has room for improvement
- Structured data probably missing (Webflow doesn't add it automatically)
- Internal linking structure may be suboptimal (depends on how deliberate they've been)

**Estimated technical work: 5–8 hours of fixes. No critical blockers expected.**

### Content Audit Findings

With 23 blog posts and Ahrefs data available, conduct a full content audit:

**Content performance distribution (expected pattern):**
- 3 posts drive 70% of organic traffic (power law)
- 8–10 posts rank in top 50 but could be improved
- 10–12 posts have minimal organic traction

**Specific assessments:**

Post ranking #4 for "what is keyword difficulty": This is a top-of-funnel educational post. It drives traffic but likely converts poorly. Assess: does it have a CTA for KeyScope? Does it explain how KeyScope's opportunity scoring improves on traditional keyword difficulty? If not, it's leaving money on the table.

Post ranking #6 for "keyword gap analysis": This is their core topic. Rank #6 is good but not great. Assess: what do the #1–5 results have that this post doesn't? Usually it's depth, freshness, better visuals, or more backlinks. This post should be a priority for optimization — it's the most strategically important page.

Post ranking #11 for "best keyword research tools": This is a competitive keyword with high commercial intent. Rank #11 means they're on page 2 — close but not visible. Assess: are they including KeyScope in the list honestly? (They should.) Is the post comprehensive enough to compete with the top results? What's the backlink gap between their post and the #1–5 results?

**Content gap analysis (KeyScope vs. Mangools vs. SE Ranking):**

Expected high-priority gaps:
- "keyword research for beginners" (high volume, educational — builds topical authority)
- "how to find low competition keywords" (mid-funnel, maps to product value prop)
- "[competitor] alternatives" pages for each mid-market competitor
- Comparison pages: "keyscope vs mangools", "keyscope vs se ranking", "keyscope vs ubersuggest"
- Integration-specific content: "keyword research with google search console", "keyword research for [specific CMS/platform]"
- Use-case content: "keyword research for SaaS", "keyword research for ecommerce", "keyword research for local business"

**Keyword cannibalization check:**
With 23 posts, check if multiple posts compete for overlapping keywords. Common in growing blogs: "keyword research guide" and "how to do keyword research" may be cannibalizing each other. If so, merge into one comprehensive piece.

### Backlink Audit Findings

With 186 referring domains and DR 38:

**Profile health:** Likely healthy for a 10-month-old SaaS in a competitive space. DR 38 is respectable.

**Competitive comparison (expected):**
- Mangools: likely DR 70+, 5,000+ referring domains (years of accumulated authority)
- SE Ranking: likely DR 65+, 3,000+ referring domains
- Ubersuggest: likely DR 85+, massive link profile (Neil Patel's domain)

**The reality check:** KeyScope will not close the referring domain gap with Mangools through outreach alone. The gap is too large. But they don't need to match Mangools' total link profile — they need enough authority to compete for their target keywords, combined with better content.

**Link gap priorities:**
1. Tool roundup posts that include Mangools/SE Ranking but not KeyScope — request inclusion
2. SEO community blogs that review tools — pitch for KeyScope reviews
3. "Best keyword research tools" posts (high-authority sites) — these drive both links and traffic
4. Industry publications (Search Engine Journal, Search Engine Land, Moz blog) — pitch data studies using KeyScope's data

### Prioritized Action Plan

**Month 1: Fix and optimize existing assets**

1. Optimize the "keyword gap analysis" post to push from #6 toward #1–3. This is the single highest-impact action. Specific improvements based on top-result analysis.
2. Optimize the "best keyword research tools" post to push from #11 to page 1. This keyword drives direct commercial traffic.
3. Add structured data (FAQ schema, SoftwareApplication) across the site.
4. Fix any CWV issues found in the technical audit.
5. Add strong CTAs to the "what is keyword difficulty" post — connecting traditional KD to KeyScope's opportunity scoring.

**Month 2: Bottom-funnel content blitz**

Create the pages that directly capture buying intent:
- "KeyScope vs Mangools" comparison page
- "KeyScope vs SE Ranking" comparison page
- "Mangools Alternatives" page
- "SE Ranking Alternatives for Small Teams" page
- "Best Keyword Research Tools for [SEO Agencies/Freelancers/Small Teams]" (segment-specific listicles)

Each comparison page should be honest, acknowledging where competitors are stronger while clearly articulating where KeyScope wins.

**Month 3: Topical authority expansion + link building**

Content:
- Publish the "Complete Guide to Keyword Gap Analysis" (pillar page — this is their claimed territory)
- "How to Find Low Competition Keywords" (mid-funnel)
- "Keyword Research for SaaS Companies" (use-case targeting)

Link building:
- Start link gap outreach: target sites linking to Mangools/SE Ranking tool reviews
- Pitch to 3 SEO industry publications for guest posts or data study features
- Build a free tool: "Free Keyword Gap Checker" (lightweight version of KeyScope's core feature) — this becomes a permanent link magnet and top-of-funnel acquisition

**Ongoing cadence:**
- 2 new content pieces per week (one bottom-funnel, one mid-funnel)
- 1 content refresh per week (optimize existing posts ranking 5–20)
- 5–10 outreach emails per week (link gap prospects + resource page pitches)
- Monthly: review rankings, update content calendar based on data

**Expected results in 6 months:**
- Organic traffic: 4,200/mo → 12,000–18,000/mo
- Keywords ranking top 20: 45 → 120–150
- Referring domains: 186 → 300–400
- Comparison/alternative pages becoming a meaningful signup source by month 3
- "Keyword gap analysis" becoming their #1 organic traffic driver with top-3 ranking

**Longer-term opportunities (months 6–12):**
- Programmatic SEO: build pages for individual keyword difficulty scores, SERP analysis for popular keywords, or keyword cluster tools (requires engineering work)
- Data studies: "We analyzed 10M keyword difficulty scores — here's what we found" → digital PR for links
- Content partnerships with complementary tools (rank tracking tools, content optimization tools)
- Explore Webflow migration to Next.js if Webflow's limitations are constraining growth (only if CWV issues persist or programmatic SEO is blocked)
