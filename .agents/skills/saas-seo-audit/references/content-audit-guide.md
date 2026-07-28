# Content SEO Audit Guide

Complete content analysis framework for SaaS products. Covers keyword mapping, content gap analysis, on-page optimization, content strategy, and content brief templates.

---

## Table of Contents

1. [Content Inventory](#content-inventory)
2. [Keyword Mapping](#keyword-mapping)
3. [Content Gap Analysis](#content-gap-analysis)
4. [On-Page Optimization](#on-page-optimization)
5. [Content Quality Assessment](#content-quality-assessment)
6. [Content Strategy for SaaS](#content-strategy-for-saas)
7. [Content Types That Work for SaaS](#content-types-that-work-for-saas)
8. [Content Brief Template](#content-brief-template)
9. [Content Refresh Process](#content-refresh-process)
10. [Keyword Cannibalization](#keyword-cannibalization)

---

## Content Inventory

Before analyzing content quality, inventory what exists. Build a spreadsheet with:

| Column | Where to get it |
|---|---|
| URL | Crawl output or sitemap |
| Title | Crawl output |
| Primary keyword (if any) | Manual review or inferred from title/H1 |
| Organic traffic (last 30 days) | Search Console or analytics |
| Top ranking keyword | Search Console → Performance → Pages |
| Average position for top keyword | Search Console |
| Impressions (last 30 days) | Search Console |
| Word count | Crawl output |
| Last updated | CMS or manual check |
| Content type | Manual: blog post, landing page, docs, comparison, etc. |

This inventory becomes the operating document for the content audit. Every recommendation references rows in this sheet.

### Without paid tools

Google Search Console provides: pages sorted by clicks, impressions, average position, and CTR. This is enough to identify your top pages, pages with untapped potential (high impressions, low clicks), and pages that have lost traffic.

Screaming Frog free crawl gives: titles, H1s, meta descriptions, word count, and page depth for up to 500 URLs.

### With paid tools

Ahrefs/Semrush adds: estimated traffic value, all keywords each page ranks for (not just the top one), keyword difficulty scores, and historical ranking data. This dramatically accelerates the audit.

---

## Keyword Mapping

A keyword map assigns one primary keyword to each page. This prevents cannibalization and ensures intentional targeting.

### Building the keyword map

1. **Export all keywords the site ranks for** from Search Console (Performance → Queries → export). Or from Ahrefs/Semrush if available.
2. **Group keywords by intent** — cluster keywords that a single page should satisfy. For example, "api monitoring tool", "api monitoring software", and "best api monitoring" are all served by the same page.
3. **Assign each cluster to one page** — either an existing page or a page that needs to be created.
4. **Identify gaps** — keyword clusters with no assigned page are content opportunities.
5. **Identify conflicts** — keyword clusters assigned to multiple pages are cannibalization risks.

### Keyword intent categories for SaaS

| Intent type | Example keywords (API monitoring product) | Example keywords (SEO keyword tool) | Target page type |
|---|---|---|---|
| **Navigational** | "pingforge login", "pingforge pricing" | "keyscope dashboard", "keyscope api" | Branded pages (homepage, pricing, login) |
| **Commercial investigation** | "best api monitoring tools", "api monitoring comparison" | "best keyword research tools 2024", "ahrefs vs semrush" | Comparison/listicle pages |
| **Transactional** | "api monitoring free trial", "buy api monitoring" | "keyword research tool free trial", "keyscope pricing" | Pricing/signup pages |
| **Informational** | "how to monitor api uptime", "what is api latency" | "how to find keywords", "what is keyword difficulty" | Blog posts, guides, docs |
| **Problem-aware** | "api keeps going down", "api timeout errors" | "why is my organic traffic dropping", "not ranking on google" | Blog posts, guides |
| **Alternative-seeking** | "datadog alternative", "pingdom alternative cheaper" | "ahrefs alternative", "semrush alternative for small teams" | Alternative/comparison landing pages |

### For pre-launch or very early stage

Don't build a full keyword map. Instead:
1. Identify your 3–5 core category terms (what is your product category called?)
2. List 5–10 problem keywords your customers would search
3. Note 2–3 competitor names (for future comparison pages)
4. That's enough. Build the full map when you have content to map.

---

## Content Gap Analysis

Content gaps are keywords your competitors rank for that you don't. This is the highest-signal source for content ideas because it's validated by actual competitor traffic.

### With paid tools (recommended)

Run a content gap report in Ahrefs or Semrush:
- Input: your domain vs. 2–3 competitor domains
- Output: keywords where at least one competitor ranks in top 20, but you don't

Filter the results:
1. Remove branded competitor keywords (you won't rank for "ahrefs tutorial")
2. Sort by search volume × relevance
3. Group into content topics (many keywords will cluster around one page idea)
4. Prioritize: high volume + low difficulty + high relevance = best opportunities

### Without paid tools

Manual content gap analysis:
1. Visit each competitor's blog/content section
2. List their top 20–30 topics based on what appears prominent
3. Check: do you have content on each of these topics? If not, that's a potential gap.
4. Search each topic in Google — look at the top 10 results. If competitors appear and you don't, it's a confirmed gap.
5. Check competitor sitemaps (`/sitemap.xml`) to find pages you might have missed

This is slower and less complete than a tool-based analysis, but still surfaces the biggest gaps.

### Prioritizing content gaps

Not every gap is worth filling. Prioritize:

| Priority | Signal |
|---|---|
| **High** | Keyword maps to a page that would directly support conversion (comparison pages, alternative pages, use-case pages) |
| **High** | Keyword has significant volume and competitors are ranking with mediocre content you could improve on |
| **Medium** | Keyword has moderate volume and fits your topical authority |
| **Medium** | Keyword maps to a problem your product solves, even if indirectly |
| **Low** | Keyword has volume but is tangential to your product (traffic without conversion potential) |
| **Skip** | Keyword requires content type you can't produce (e.g., original data study when you have no data) |

---

## On-Page Optimization

For each page, check these elements. Listed in order of impact:

### Title tag

- Includes primary keyword (ideally near the beginning)
- Under 60 characters (or it gets truncated in SERPs)
- Compelling enough to click — not just keyword-stuffed
- Unique across the site (no duplicate titles)

Bad: "Blog - PingForge"
Okay: "API Monitoring Tools - PingForge"
Good: "API Monitoring for Developers — Uptime Alerts in 30 Seconds | PingForge"

### Meta description

- 120–155 characters
- Includes primary keyword naturally
- Contains a value proposition or reason to click
- Unique per page

The meta description doesn't directly affect rankings, but it affects CTR — which affects traffic. A page ranking #5 with a compelling meta description can get more clicks than a page ranking #3 with a generic one.

### H1 tag

- One H1 per page (not zero, not multiple)
- Contains primary keyword or close variant
- Describes the page content clearly

### Heading hierarchy (H2–H4)

- Logical hierarchy (H2 sections, H3 subsections)
- H2s cover the main subtopics a searcher would expect
- Include secondary keywords naturally in H2s/H3s
- Don't skip levels (no H1 → H3 without an H2)

### Content body

- Answers the search intent completely (if someone searches this keyword, does this page satisfy their need?)
- Sufficient depth — not necessarily long, but comprehensive for the topic
- Includes related terms and entities naturally (Google uses semantic understanding, not exact keyword matching)
- Readable: short paragraphs, clear language, formatting that aids scanning
- Includes internal links to related content on the site
- Includes relevant images or visuals with descriptive alt text

### URL slug

- Contains primary keyword
- Short and descriptive
- No unnecessary parameters, IDs, or dates (unless dates are meaningful, like news)

---

## Content Quality Assessment

### The content quality spectrum for SaaS

Not all content needs to be a 5,000-word pillar post. Different content types serve different functions:

| Content quality level | When it's appropriate | Example |
|---|---|---|
| **Utilitarian (300–500 words)** | Answering a specific question, changelog entries, integration pages | "How to connect PingForge to Slack" |
| **Solid (800–1,500 words)** | Standard blog posts, how-to guides, comparison pages | "API Monitoring Best Practices for Startups" |
| **Comprehensive (1,500–3,000 words)** | Pillar content, definitive guides, high-competition keywords | "The Complete Guide to API Uptime Monitoring" |
| **Flagship (3,000+ words)** | Original research, industry reports, ultimate guides | "State of API Reliability: 2024 Report" |

Match content depth to keyword competition and search intent. A 5,000-word guide for "how to add a webhook in Slack" is overkill. A 300-word post targeting "api monitoring tools" won't compete.

### Assessing existing content

For each page in the content inventory, assess:

1. **Does it match search intent?** Search the primary keyword in Google. Look at the top 5 results. Is their content type (guide, listicle, tool, comparison) the same as yours? If the top results are all comparison lists and yours is a single-product pitch, you have an intent mismatch.

2. **Is it competitive in depth?** Compare your word count and topic coverage to the top 3 results. You don't need to be longest, but you need to be at least as comprehensive on the core topic.

3. **Is it current?** Content with outdated information (old screenshots, deprecated features, last year's stats) loses rankings over time. Check the "last updated" field.

4. **Does it convert?** Does the content have a relevant CTA? Is there a logical next step for the reader? Blog posts that dead-end without a CTA are wasted organic traffic.

---

## Content Strategy for SaaS

### The topical authority model

Google evaluates expertise at the site level, not just the page level. A site with 30 high-quality articles about API monitoring has more authority on "api monitoring tools" than a site with 1 article, even if that 1 article is excellent.

Build topical authority by:
1. Pick 2–3 core topic clusters tied to your product
2. Create a comprehensive "pillar" page for each cluster
3. Write supporting content (blog posts, guides, comparisons) that link back to the pillar
4. Internal link everything in the cluster together

**Example for an API monitoring product (PingForge):**

Cluster 1: API Monitoring
- Pillar: "The Complete Guide to API Monitoring"
- Supporting: "API Monitoring Best Practices", "How to Set Up API Alerts", "API Monitoring vs APM: What's the Difference?", "Top API Monitoring Tools Compared"

Cluster 2: API Reliability
- Pillar: "How to Build Reliable APIs"
- Supporting: "Understanding API Uptime SLAs", "How to Reduce API Latency", "Incident Response for API Outages"

Cluster 3: Integrations
- Pillar: "PingForge Integrations" (hub page)
- Supporting: One page per integration — "PingForge + Slack", "PingForge + PagerDuty", etc.

**Example for an SEO keyword research tool (KeyScope):**

Cluster 1: Keyword Research
- Pillar: "The Complete Guide to Keyword Research"
- Supporting: "How to Find Low-Competition Keywords", "Keyword Research for SaaS", "Long-Tail Keywords: Why They Matter", "How to Build a Keyword Map"

Cluster 2: Competitive SEO
- Pillar: "How to Analyze Competitor SEO"
- Supporting: "Keyword Gap Analysis Explained", "How to Find Competitor Keywords", "SEO Competitor Benchmarking"

Cluster 3: Comparisons
- Hub: "KeyScope vs. The Competition"
- Supporting: "KeyScope vs. Ahrefs", "KeyScope vs. Semrush", "Best Keyword Research Tools for Small Teams"

### Content velocity by tier

| Tier | Content pace | Focus |
|---|---|---|
| **Tier 1 (1–3 hrs/wk)** | 1 post every 1–2 weeks | Only high-priority keywords from gap analysis. Optimize existing content first. |
| **Tier 2 (3–6 hrs/wk)** | 1 post per week | Mix of new content and content refreshes. Build toward cluster completeness. |
| **Tier 3 (6+ hrs/wk)** | 2+ posts per week + refreshes | Full content program. New content, refreshes, programmatic pages, data studies. |

---

## Content Types That Work for SaaS

In order of typical conversion rate (highest first):

1. **Comparison pages** — "[Your product] vs [Competitor]" → Very high conversion, captures bottom-funnel intent
2. **Alternative pages** — "[Competitor] alternatives" → High conversion, captures switching intent
3. **Use-case pages** — "[Your product] for [use case/industry]" → High conversion, captures specific need
4. **Integration pages** — "[Your product] + [Tool]" → Medium-high conversion, captures ecosystem intent
5. **Best-of listicles** — "Best [category] tools" → Medium conversion, but you must include your product honestly
6. **How-to guides** — "How to [solve problem your product solves]" → Medium conversion, top-of-funnel
7. **Definitive guides** — "Complete guide to [topic]" → Low-medium conversion, builds authority and links
8. **Glossary/education** — "What is [concept]" → Low conversion, high volume, builds topical authority
9. **Original research** — "[Data study about your industry]" → Low direct conversion, but excellent for links and authority

Don't start at the bottom of this list. Many SaaS blogs start with educational content that drives traffic but not customers. Start with comparison, alternative, and use-case pages — they're closer to revenue.

---

## Content Brief Template

When planning new content (whether the founder writes it or someone else), use this structure:

```
## Content Brief: [Working Title]

**Primary keyword:** [target keyword]
**Secondary keywords:** [2-5 related terms]
**Search intent:** [informational / commercial / transactional]
**Target word count:** [range based on competition analysis]
**Target audience:** [who is searching this and what do they need]

**SERP analysis:**
- Current top 3 results and their approach:
  1. [URL] — [content type, word count, angle]
  2. [URL] — [content type, word count, angle]
  3. [URL] — [content type, word count, angle]
- What the top results do well:
- What's missing from the top results (your opportunity):

**Outline:**
- H1: [title]
- H2: [section 1]
- H2: [section 2]
- [etc.]

**CTA:** [what should the reader do after reading this?]
**Internal links to include:** [related pages on your site]
**Internal links pointing to this page:** [existing pages that should link to this new piece]
```

---

## Content Refresh Process

Refreshing existing content is often higher ROI than creating new content, especially for pages that rank positions 5–20.

### When to refresh

- Page ranks positions 5–20 for a valuable keyword (close but not there)
- Page has lost rankings or traffic over the past 3–6 months
- Page content is factually outdated (old stats, deprecated features, dead links)
- Page ranks well but CTR is low (title/meta description problem)
- Competitors have published better content on the same topic

### How to refresh

1. Check what keyword the page ranks for now (may have shifted from original intent)
2. Analyze the current top 3 results for that keyword — what do they cover that you don't?
3. Update factual information (dates, stats, screenshots, links)
4. Add missing sections that top competitors cover
5. Improve the title tag if CTR is low
6. Add or update internal links (both to and from this page)
7. Update the "last updated" date (show it on the page if possible)
8. Resubmit the URL in Search Console after significant changes

### Refresh cadence

| Content type | Refresh frequency |
|---|---|
| Product/feature pages | When the product changes |
| Comparison pages | Quarterly (competitor products change) |
| Best-of listicles | Every 6 months |
| How-to guides | Annually, or when the process changes |
| Evergreen educational | Only if rankings drop or information changes |
| Data/research posts | Annually with new data |

---

## Keyword Cannibalization

Cannibalization happens when multiple pages on your site target the same keyword, causing Google to split authority between them and rank neither as well as a single focused page would.

### How to detect

1. Search Console → Performance → filter by a keyword → check if multiple pages appear in the Pages tab
2. If 2+ pages get impressions for the same keyword, and neither ranks well, that's cannibalization
3. In Ahrefs/Semrush, check if a URL's top keyword keeps changing — this signals Google is testing different pages

### How to fix

| Situation | Fix |
|---|---|
| Two similar blog posts on the same topic | Merge into one comprehensive post, 301 redirect the other |
| Blog post and landing page targeting same keyword | Differentiate intent — landing page targets commercial intent, blog targets informational |
| Multiple pages accidentally targeting same keyword | Pick the strongest, add canonical or redirect others, differentiate remaining pages' targeting |
| Tag/category pages competing with actual content | Noindex tag/category pages or add enough unique content to differentiate |

### Prevention

The keyword map prevents cannibalization before it happens. Before creating new content, check: does a page already target this keyword? If yes, refresh that page instead of creating a new one.
