# Technical SEO Audit Guide

Complete technical audit checklist for SaaS products. Each issue includes severity, what to check, how to fix, and which tool tier can detect it.

---

## Table of Contents

1. [Crawlability & Indexation](#crawlability--indexation)
2. [Site Architecture & Internal Linking](#site-architecture--internal-linking)
3. [Page Speed & Core Web Vitals](#page-speed--core-web-vitals)
4. [JavaScript Rendering & SPA Issues](#javascript-rendering--spa-issues)
5. [URL Structure & Canonicalization](#url-structure--canonicalization)
6. [Structured Data](#structured-data)
7. [Mobile & Responsive](#mobile--responsive)
8. [Security & HTTPS](#security--https)
9. [International & Multilingual](#international--multilingual)
10. [Technical Audit Checklist by Tier](#technical-audit-checklist-by-tier)

---

## Crawlability & Indexation

### Robots.txt

**Severity: Critical if misconfigured**

Check:
- `robots.txt` exists at domain root
- Not blocking important pages or directories (common SaaS mistake: blocking `/app/` when `/app/pricing/` should be crawlable)
- Not blocking CSS/JS files (Google needs these to render pages)
- Sitemap URL is declared in `robots.txt`

Common SaaS mistakes:
- Blocking `/api/` thinking it's the API endpoint, when `/api-docs/` lives under that path
- Blanket `Disallow: /app/` when some app-adjacent pages (pricing, docs, changelog) live under `/app/`
- Blocking staging or preview URLs in production robots.txt (happens with copy-paste from staging environment)

Fix: Review every `Disallow` rule. The principle is: block only pages that should never appear in search results (login pages, admin panels, user-specific dashboards). Everything else should be crawlable.

**Tool tier: Free** — just visit `yourdomain.com/robots.txt`

### XML Sitemap

**Severity: Critical if missing**

Check:
- Sitemap exists and is submitted to Search Console
- Sitemap contains only 200-status, indexable, canonical pages
- Sitemap doesn't contain noindexed pages, redirects, or 404s
- Sitemap is updated when pages are added/removed
- For large sites (1,000+ URLs): sitemap index file with sub-sitemaps

Common SaaS mistakes:
- Auto-generated sitemaps that include every URL including login, signup confirm, password reset pages
- Stale sitemaps that haven't been updated since initial deployment
- Sitemap lists www version but site redirects to non-www (or vice versa)

Fix: Generate sitemaps dynamically if possible (most frameworks have plugins). If static, set a reminder to update when pages change. Validate with Search Console's Sitemaps report.

**Tool tier: Free** — Google Search Console → Sitemaps

### Indexation Status

**Severity: Critical**

Check:
- Search Console → Pages → see how many pages are indexed vs. excluded
- Review each exclusion reason: "Crawled - currently not indexed", "Discovered - currently not indexed", "Excluded by noindex tag", "Alternate page with proper canonical tag", "Blocked by robots.txt"
- For each exclusion category, check if any pages should be indexed but aren't

Key signals:
- "Crawled - currently not indexed" at high numbers → Google crawled the pages but decided they weren't worth indexing. Usually a quality/thin content problem.
- "Discovered - currently not indexed" at high numbers → Google knows the URLs exist but hasn't bothered to crawl them. Usually a crawl budget or priority problem.
- Important pages in any exclusion category → Something is actively wrong.

**Tool tier: Free** — Google Search Console → Pages (Indexing)

### Crawl Errors

**Severity: High**

Check:
- Search Console → Pages → check for 404s, server errors, redirect errors
- Run a crawl (Screaming Frog free tier for <500 URLs, or paid for larger sites)
- Look for: soft 404s (page returns 200 but shows error content), redirect chains (A → B → C), redirect loops

Common SaaS crawl error patterns:
- Deleted blog posts that still have internal or external links pointing to them
- Changed URL structure without redirects (e.g., moved from `/blog/post-slug` to `/resources/post-slug`)
- Dynamic pages returning 200 with empty content when the data source is missing

**Tool tier: Free** — Search Console + Screaming Frog free (500 URL limit)

---

## Site Architecture & Internal Linking

### Click Depth

**Severity: Medium**

Every important page should be reachable in 3 clicks or fewer from the homepage. Pages buried deeper get crawled less frequently and receive less authority.

Check:
- Run a crawl and check crawl depth for key pages (Screaming Frog shows this)
- Blog posts older than 6 months are often 4+ clicks deep — they fall off the blog index as new posts push them down
- Important landing pages should be linked from the main navigation or footer

Fix for deep blog posts: Category/topic hub pages that link to all related posts. Sidebar or footer "most popular" sections. Internal links within post content.

**Tool tier: Free** — Screaming Frog free crawl shows depth

### Internal Link Distribution

**Severity: Medium**

Check:
- Are key pages (pricing, product features, top blog posts) receiving enough internal links?
- Are there orphaned pages (no internal links pointing to them)?
- Is link equity concentrated on the homepage with little flowing to deeper pages?

The internal linking mental model for engineers: Think of your site as a directed graph. PageRank flows along edges. If your homepage has 10 outbound links and your pricing page has 2 inbound links (one from the nav, one from a blog post), the pricing page is underpowered relative to its importance.

Fix: Add contextual internal links in blog content pointing to product/feature pages. Create hub pages that link to clusters of related content. Ensure navigation includes your highest-priority pages.

**Tool tier: Free** — Screaming Frog shows inlinks per page. Budget tier — Ahrefs/Semrush show internal link distribution.

### URL Structure

**Severity: Low-Medium**

Best practices for SaaS:
- Descriptive, keyword-containing slugs: `/blog/api-monitoring-best-practices` not `/blog/post-12847`
- Consistent hierarchy: `/blog/category/post-slug` or `/blog/post-slug` — pick one, be consistent
- No URL parameters for content differentiation (use paths instead)
- Lowercase only, hyphens not underscores

Don't change existing URL structure unless it's actively causing problems. Every URL change requires redirects, and redirects lose a small amount of link equity.

**Tool tier: Free** — manual review + Screaming Frog

---

## Page Speed & Core Web Vitals

### Core Web Vitals (CWV)

**Severity: High** — CWV is a confirmed ranking factor. Not the most important one, but poor CWV can hold back otherwise strong pages.

The three metrics:
- **Largest Contentful Paint (LCP)**: How fast the main content loads. Target: < 2.5s. The biggest LCP issue for SaaS sites is hero images or above-the-fold content loading slowly.
- **Cumulative Layout Shift (CLS)**: Visual stability — does the page jump around as it loads? Target: < 0.1. Common SaaS culprits: web fonts loading late (FOUT), images without explicit dimensions, dynamic content injected above the fold.
- **Interaction to Next Paint (INP)**: Responsiveness to user input. Target: < 200ms. Common SaaS culprits: heavy JavaScript blocking the main thread, analytics/tracking scripts, third-party widgets.

Check:
- Search Console → Core Web Vitals report (shows field data from real users)
- PageSpeed Insights for per-page analysis (lab data + field data)
- Chrome DevTools → Performance tab for debugging specific issues

Common SaaS speed issues:
- Unoptimized images (hero images at 2MB+ when 100KB WebP would work)
- Too many third-party scripts (analytics, chat widgets, A/B testing tools, heatmaps — each adds 100–500ms)
- No CDN for static assets
- Server-side rendering without caching (every page load hits the database)
- Web fonts loading synchronously (blocks rendering until fonts download)

Fix priority:
1. Optimize images (biggest bang for the buck — use WebP/AVIF, lazy load below-fold images, set explicit width/height)
2. Defer non-critical JavaScript (analytics, chat widgets don't need to load before content)
3. Use a CDN (Cloudflare free tier is fine for most SaaS sites)
4. Cache server-rendered pages where content doesn't change per-user
5. Preload critical fonts, use `font-display: swap`

**Tool tier: Free** — PageSpeed Insights, Search Console CWV report, Chrome DevTools

---

## JavaScript Rendering & SPA Issues

### The SPA problem for SEO

**Severity: Critical if applicable**

If the site's public-facing pages are built as a client-side SPA (React, Vue, Angular without SSR), Googlebot may not see the content. Google's rendering pipeline:

```
1. Googlebot fetches HTML  →  sees empty <div id="root">
2. Adds to rendering queue  →  may wait hours/days
3. Renders JavaScript      →  now sees content
4. Indexes rendered content →  but may miss dynamic content loaded on scroll/interaction
```

The risk: Google's rendering is delayed and imperfect. Pages that work fine in a browser may be partially or fully invisible to Googlebot.

**How to check:**
- Google Search Console → URL Inspection → "View Tested Page" → compare HTML source vs. rendered page
- `site:yourdomain.com` in Google — if pages show with empty or partial descriptions, rendering may be failing
- Fetch as Googlebot in Search Console and inspect the screenshot

**The fix spectrum:**

| Approach | Effort | SEO result |
|---|---|---|
| **Static Site Generation (SSG)** | Low if starting fresh, high to retrofit | Best — HTML is ready at crawl time |
| **Server-Side Rendering (SSR)** | Medium — framework-dependent (Next.js makes this easy) | Excellent — HTML is ready at crawl time |
| **Hybrid (SSR for marketing, SPA for app)** | Medium | Excellent for marketing pages |
| **Dynamic rendering** (serve pre-rendered HTML to bots) | Medium — maintenance burden | Good but Google discourages this as a long-term solution |
| **Prerender service** (Prerender.io, Rendertron) | Low — drop-in service | Acceptable — adds latency, may miss dynamic content |
| **Do nothing** | None | Poor — relying on Google's rendering queue is gambling |

Recommended for most SaaS: **Hybrid approach.** Use SSR/SSG for all public-facing pages (homepage, pricing, features, blog, docs, landing pages). Keep the SPA for the logged-in app experience. Most modern frameworks (Next.js, Nuxt, SvelteKit) make this straightforward.

**Tool tier: Free** — Google Search Console URL Inspection, `site:` operator

---

## URL Structure & Canonicalization

### Canonical Tags

**Severity: High if misconfigured**

Check:
- Every indexable page should have a self-referencing canonical tag
- No pages with canonical pointing to a different page unless intentional (e.g., paginated pages canonicalizing to page 1)
- HTTP and HTTPS versions resolve to one (canonical + redirect)
- www and non-www versions resolve to one (canonical + redirect)
- No conflicting signals (canonical says page A, but internal links and sitemap point to page B)

Common SaaS canonical issues:
- SPA frameworks inserting wrong canonical tags (often the homepage URL on every page)
- URL parameters creating duplicate versions without canonicals (`/pricing` vs. `/pricing?ref=header`)
- Trailing slash inconsistency (`/blog/post` vs. `/blog/post/` — pick one, redirect the other)

**Tool tier: Free** — Screaming Frog extracts canonical tags. Manual check via "View Page Source."

### Duplicate Content

**Severity: Medium**

Check for:
- Same content accessible at multiple URLs (with/without trailing slash, with/without www, HTTP vs. HTTPS)
- Boilerplate-heavy pages with little unique content
- Paginated content without proper `rel="next"/"prev"` or canonical handling
- Blog tag/category pages that duplicate post content

**Tool tier: Free** — Screaming Frog detects duplicate titles/content. Budget tier — Siteliner, Semrush Site Audit.

---

## Structured Data

### SaaS-Relevant Schema Types

**Severity: Low-Medium** — doesn't directly affect rankings but enables rich results in SERPs.

| Schema type | When to use | Rich result potential |
|---|---|---|
| `Organization` | Homepage | Knowledge panel |
| `SoftwareApplication` | Product/pricing page | Software details in SERP |
| `FAQPage` | Pages with FAQ sections | FAQ expandable in SERP |
| `HowTo` | Tutorial/guide content | Step-by-step in SERP |
| `Article` / `BlogPosting` | Blog posts | Article features in SERP |
| `BreadcrumbList` | All pages | Breadcrumb display in SERP |

Implementation: Use JSON-LD (not microdata or RDFa). Validate with Google's Rich Results Test.

Don't over-invest here early on. Structured data is a nice-to-have that becomes more valuable as the site gains authority. A site with 10 blog posts doesn't need FAQ schema on every page.

**Tool tier: Free** — Google Rich Results Test, Schema Markup Validator

---

## Mobile & Responsive

**Severity: High** — Google uses mobile-first indexing.

Check:
- All content visible on mobile (not hidden behind "click to expand" or absent from mobile layout)
- Touch targets (buttons, links) are appropriately sized (minimum 48x48px)
- No horizontal scrolling
- Text readable without zooming
- Interstitials don't block content (Google penalizes intrusive interstitials)

For SaaS: The marketing site must be fully responsive. The app itself is less critical for SEO (it's behind a login), but if any app-adjacent pages are public and indexed, they need to work on mobile.

**Tool tier: Free** — Chrome DevTools device emulation, PageSpeed Insights mobile test

---

## Security & HTTPS

**Severity: Critical if missing**

Check:
- Site serves over HTTPS (HTTPS is a confirmed ranking signal)
- No mixed content warnings (HTTP resources loaded on HTTPS pages)
- HTTP URLs redirect to HTTPS (301 redirect)
- SSL certificate is valid and not expired
- HSTS header is set (optional but recommended)

This should be a non-issue for most modern SaaS products, but check anyway — certificate expiry and mixed content are common oversights.

**Tool tier: Free** — browser padlock, SSL Labs test, Screaming Frog flags mixed content

---

## International & Multilingual

**Severity: Medium if applicable, ignore otherwise**

Only relevant if the SaaS product serves multiple language markets.

Check:
- `hreflang` tags correctly implemented if serving content in multiple languages
- Each language version has unique content (not just auto-translated)
- Language-specific URLs are consistent (`/en/pricing`, `/de/pricing` or `en.domain.com`, `de.domain.com`)
- Search Console is configured for each language/country version

Most early-stage SaaS products don't need this. Add international SEO when you're actively marketing in non-English markets with localized content.

**Tool tier: Free** — Screaming Frog extracts hreflang tags. Manual review of implementation.

---

## Technical Audit Checklist by Tier

### Tier 1 — Free tools (Screaming Frog free, Search Console, PageSpeed Insights)

- [ ] Search Console set up and verified
- [ ] Sitemap submitted and valid
- [ ] `robots.txt` reviewed — no important pages blocked
- [ ] Crawl with Screaming Frog free (up to 500 URLs)
  - [ ] Check for 4xx/5xx errors
  - [ ] Check for missing/duplicate titles and meta descriptions
  - [ ] Check for pages missing H1 tags
  - [ ] Check canonical tag implementation
  - [ ] Review crawl depth — key pages within 3 clicks
- [ ] Search Console → Pages → review indexation exclusions
- [ ] Search Console → Core Web Vitals → check for failing URLs
- [ ] PageSpeed Insights on top 5 pages — note critical issues
- [ ] Manual check: HTTPS, mobile responsiveness, robots.txt
- [ ] `site:yourdomain.com` — does the indexed page count match expectations?
- [ ] If SPA: URL Inspection in Search Console to verify rendering

### Tier 2 — Add paid crawler (Screaming Frog paid, Sitebulb, or SEO platform's audit tool)

Everything in Tier 1, plus:
- [ ] Full site crawl (no URL limit)
- [ ] JavaScript rendering audit (crawl with JS rendering enabled)
- [ ] Internal link analysis — orphaned pages, link distribution
- [ ] Redirect chain detection and cleanup
- [ ] Duplicate content detection across site
- [ ] Structured data validation across all pages
- [ ] Image optimization audit (missing alt text, oversized images)
- [ ] Crawl budget analysis (if 1,000+ pages)

### Tier 3 — Add log file analysis and advanced tools

Everything in Tier 2, plus:
- [ ] Log file analysis — compare Googlebot crawl behavior to crawl simulation
- [ ] Identify pages Googlebot crawls frequently vs. rarely
- [ ] Detect crawl budget waste (Googlebot crawling low-value pages)
- [ ] Advanced rendering audit (compare rendered DOM vs. raw HTML across page types)
- [ ] Edge SEO opportunities (CDN-level redirects, header optimization)
- [ ] Automated monitoring for crawl errors and indexation drops
