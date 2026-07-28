# Backlink Audit Guide

Complete backlink analysis framework for SaaS products. Covers link profile health, competitive link gap analysis, link building playbooks by tier, and outreach templates.

---

## Table of Contents

1. [Link Profile Analysis](#link-profile-analysis)
2. [Competitive Link Gap](#competitive-link-gap)
3. [Link Building Playbooks by Tier](#link-building-playbooks-by-tier)
4. [SaaS-Specific Link Opportunities](#saas-specific-link-opportunities)
5. [Outreach Templates](#outreach-templates)
6. [Link Building Metrics & Tracking](#link-building-metrics--tracking)
7. [What Not to Do](#what-not-to-do)

---

## Link Profile Analysis

### Key metrics to assess

| Metric | What it tells you | Where to get it |
|---|---|---|
| **Referring domains (total)** | Overall link authority. More important than total backlinks — 100 links from 100 sites beats 100 links from 1 site. | Ahrefs, Semrush, Moz |
| **Domain Rating / Domain Authority** | Rough authority score (0–100). Not a Google ranking factor, but useful for competitive benchmarking. | Ahrefs (DR), Moz (DA), Semrush (Authority Score) |
| **Referring domain growth trend** | Is the site gaining or losing links over time? Declining link profiles signal content or relevance problems. | Ahrefs → Overview → Referring domains graph |
| **Anchor text distribution** | What text is used to link to you. Should be mostly brand name + URL, with some keyword-rich anchors. Over-optimized anchor text (too many exact-match keywords) can trigger penalties. | Ahrefs → Anchors report |
| **Link quality distribution** | What proportion of linking sites are legitimate vs. spammy? | Manual review of top referring domains |
| **Dofollow vs. nofollow ratio** | Dofollow links pass authority. A natural profile has a mix — roughly 60–80% dofollow is normal. | Ahrefs or Semrush backlink report |

### Without paid tools

Free backlink data is limited but available:
- **Google Search Console** → Links → shows top linking sites and top linked pages. Doesn't show DR/DA or anchor text detail, but gives you the landscape.
- **Ahrefs Webmaster Tools** (free for verified sites) → shows referring domains, top pages by links, and broken backlinks for your own site.
- **Moz Link Explorer** (free tier) → 10 queries/month, shows DA, top links, and spam score.

With free tools alone, you can assess: how many sites link to you, which pages get the most links, and whether any obviously spammy sites link to you. You can't do competitive link gap analysis without at least one paid tool.

### Health check: red flags

| Red flag | What it means | Action |
|---|---|---|
| Large number of links from a single foreign-language domain | Likely spam or scraper site | Usually harmless — ignore unless it's massive (thousands of links). If concerned, use Google's Disavow tool. |
| Sudden spike in referring domains followed by plateau | Could be a paid link campaign (yours or a negative SEO attack) | Investigate the source. If it's low-quality links you didn't build, consider disavow. |
| 90%+ of anchors are exact-match keywords | Over-optimized — potentially from a past link building campaign | Diversify with brand-anchor links. Don't panic unless you've received a manual action. |
| Referring domain count declining | Sites are removing your links or going offline | Check if lost links were from high-value pages. May need to earn replacement links. |
| Links mostly from irrelevant industries | Link profile doesn't signal topical relevance | Focus new link building on industry-relevant sources. |

### Toxic link assessment

Google is generally good at ignoring low-quality links — the disavow tool is a last resort, not routine maintenance. Only investigate toxic links if:
- You've received a manual action in Search Console (rare for SaaS sites)
- You have a known history of paid links or PBN usage
- A competitor has done a negative SEO attack (extremely rare, usually not worth worrying about)

For most SaaS sites: your link profile is probably fine. Focus energy on building good links, not cleaning up bad ones.

---

## Competitive Link Gap

### What is a link gap?

Sites that link to your competitors but not to you. These are the most valuable prospecting targets because they've already demonstrated willingness to link to products/content in your space.

### Running a link gap analysis

**With Ahrefs (recommended approach):**
1. Go to Ahrefs → Link Intersect tool
2. Enter your domain and 2–3 competitors
3. Filter: "Show websites that link to at least one competitor but not to me"
4. Sort by DR (Domain Rating) to prioritize high-authority sites
5. Export and categorize the results

**With Semrush:**
1. Backlink Gap tool → enter your domain and competitors
2. Filter for "missing" links (competitor has, you don't)
3. Sort by authority score

**Without paid tools:**
This is difficult without tools. The manual alternative:
1. For each competitor, find their most-linked pages (Ahrefs Webmaster Tools shows this for your own site; for competitors, use the free tier of Moz or Ahrefs backlink checker)
2. Identify the types of content/pages that attract links
3. Create similar (better) content on your site
4. This is more of a "content gap" approach to links than a direct link gap analysis

### Categorizing link gap results

After exporting the gap, categorize each linking site:

| Category | Examples | Approach |
|---|---|---|
| **Industry publications** | Tech blogs, SaaS review sites, industry news | Pitch for inclusion in existing articles, or offer expert quotes |
| **Directories & lists** | "Best tools" roundups, SaaS directories, comparison sites | Submit for inclusion or reach out to the author |
| **Content that references competitors** | Blog posts that mention competitors by name | Suggest adding your product as an alternative |
| **Resource pages** | "Useful tools for developers" pages, curated link collections | Reach out with a brief pitch for inclusion |
| **Educational content** | Tutorials that reference competitor products | Offer your product as an alternative example |
| **Partners & integrations** | Partner pages, integration directories | Build the integration, get listed |
| **Not replicable** | Competitor-owned properties, press coverage of specific events | Skip — can't replicate these |

Focus outreach on the first 4 categories. These have the highest response rates because the site has already demonstrated interest in your product category.

---

## Link Building Playbooks by Tier

### Tier 1 — Passive link building (no outreach, 1–2 hrs/week)

**Who this is for:** Founders with no time or inclination for outreach. This builds links slowly but requires minimal ongoing effort.

Activities:
- **Submit to relevant directories**: Product Hunt, AlternativeTo, G2, Capterra, SaaSHub, StackShare, dev tool directories for your category. One-time effort, 1–2 hours total.
- **Create linkable content as part of your normal content calendar**: Original data, free tools, templates, or comprehensive guides naturally attract links without outreach.
- **Integration pages**: Every integration you build typically results in a link from the partner's integrations/marketplace page.
- **Open-source contributions**: If you have an open-source component, the README and documentation naturally attract links from developers.

Expected results: 1–5 new referring domains per month, primarily from directories and organic discovery.

### Tier 2 — Active link building (targeted outreach, 3–5 hrs/week)

**Who this is for:** Founders ready to invest a few hours per week in deliberate link building. This is where most SaaS companies should operate.

Activities — everything in Tier 1, plus:

- **Link gap outreach**: Use the competitive link gap analysis to identify prospects. Reach out to sites that link to competitors but not to you. See outreach templates below.
- **Guest posting (selective)**: Write for 2–3 high-quality industry publications per month. Focus on publications your target audience actually reads, not generic "write for us" farms.
- **Broken link building**: Find broken links on relevant sites (use Ahrefs' Broken Backlinks report on competitor domains). Reach out to offer your content as a replacement.
- **Resource page outreach**: Find "best tools" and "useful resources" pages in your niche. Pitch for inclusion.
- **Skyscraper content**: Find popular content in your niche with many backlinks. Create a significantly better version. Reach out to sites linking to the original.

Expected results: 5–15 new referring domains per month with consistent effort.

### Tier 3 — Strategic link building (scaled outreach + digital PR, 6+ hrs/week)

**Who this is for:** Founders or marketing leads who are investing seriously in SEO as a growth channel. Typically post-product-market-fit.

Activities — everything in Tier 2, plus:

- **Digital PR / data studies**: Publish original research using your product's data (anonymized). Example for an API monitoring tool: "We analyzed 1M API calls — here's what we learned about uptime patterns." These attract links from industry publications and are regularly cited.
- **HARO / journalist outreach**: Respond to journalist queries on platforms like HARO, Connectively, or direct journalist outreach. Provide expert commentary on industry topics.
- **Content partnerships**: Co-create content with complementary products. Both parties link to the joint content.
- **Speaking & podcast appearances**: Speaking at conferences and appearing on podcasts in your niche generates natural links from event/show pages.
- **Free tools / calculators**: Build small, free tools related to your product space. These are link magnets. An API monitoring company might build a free "API uptime calculator" or "SLA calculator." An SEO keyword tool might offer a free "keyword difficulty checker" or "SERP preview tool."

Expected results: 15–30+ new referring domains per month with a dedicated effort.

---

## SaaS-Specific Link Opportunities

These are link building opportunities unique to or especially effective for SaaS products:

### Integration marketplace links

Every integration you build is a potential link. Most SaaS companies have integration/marketplace pages that link to partner products. Build integrations with popular tools in your ecosystem and get listed on their marketplace.

This is one of the highest-ROI link building activities for SaaS because:
- The link is highly relevant (topically and commercially)
- The linking page is often high-authority
- The link is permanent (as long as the integration exists)
- It also drives referral traffic from users discovering integrations

### Documentation as a link magnet

Comprehensive, well-written documentation attracts links from:
- Developers writing tutorials that reference your docs
- StackOverflow answers linking to your API reference
- Blog posts using your product as an example

If your docs are thorough and public, they build links passively over time.

### Open-source projects

If you have any open-source components (SDK, library, plugin), the GitHub repository and associated docs attract links naturally. Even small open-source utilities that solve specific problems in your domain can generate links.

### Startup and SaaS directories

One-time submissions, low effort, modest value but still worth doing:

| Directory | Notes |
|---|---|
| Product Hunt | Launch once, get a permanent profile |
| G2 / Capterra | Review sites; also help with brand search presence |
| AlternativeTo | Submit as an alternative to competitors |
| SaaSHub | SaaS discovery directory |
| StackShare | Tech stack discovery (especially for dev tools) |
| BetaList | If pre-launch or early stage |
| Indie Hackers | If bootstrapped — community profile + product listing |
| Hacker News (Show HN) | Not a directory, but a one-time launch opportunity with lasting link value |

### Industry-specific opportunities

- **API products**: API directories (RapidAPI, ProgrammableWeb archives, API Tracker), developer community links
- **SEO tools**: SEO community roundups, tool review sites, SEO blog guest posts
- **DevOps tools**: DevOps community blogs, "awesome-devops" GitHub lists, infrastructure comparison posts
- **B2B SaaS**: Industry analyst mentions, G2 Grid reports, review site profiles

---

## Outreach Templates

### Template 1: Link gap outreach (competitor content)

Use when a site links to a competitor and your product is a valid alternative.

```
Subject: Quick note about your [topic] post

Hi [Name],

I came across your article on [topic] — nice coverage of [specific thing they did well].

I noticed you mention [Competitor]. We built [Your Product], which [one-sentence differentiation from the competitor]. [One specific thing your product does differently that's relevant to their article].

If it's helpful for your readers, happy to provide any details about how we approach [topic]. Either way, enjoyed the article.

[Your name]
```

Keep it short. Don't ask for a link explicitly — suggest your product as useful context. The link happens naturally in about 5–15% of cases.

### Template 2: Broken link replacement

Use when you find a broken link on a relevant page and have content that could replace it.

```
Subject: Broken link on your [page title] page

Hi [Name],

I was reading your [page title] and noticed the link to [broken URL description] appears to be broken — looks like the page was taken down.

We have a [guide/tool/resource] that covers [same topic]: [your URL]. It might work as a replacement if you're updating the page.

Thanks for the great resource either way!

[Your name]
```

### Template 3: Resource page inclusion

Use when pitching for inclusion on a "best tools" or "useful resources" page.

```
Subject: Suggestion for your [resource page title]

Hi [Name],

I found your [resource page title] — great list. I'm the founder of [Your Product], which [one-sentence description].

We're [brief credibility marker: "used by X teams", "processing Y requests/day", "featured on Product Hunt"]. If you think it's a good fit for the list, happy to provide more details.

[Your name]
```

### Template 4: Guest post pitch

Use when pitching to write for an industry publication.

```
Subject: Post idea for [Publication]: [Proposed title]

Hi [Name],

I'm [Your name], founder of [Your Product] — [one-sentence description]. I've been reading [Publication] for [time period] and particularly liked [specific recent article].

I'd like to pitch a post: "[Proposed title]"

The angle: [2-3 sentences describing the post, what's unique about it, and why their readers would care].

I've previously written for [other publication, if applicable] / [alternative credibility marker].

Happy to send an outline if you're interested.

[Your name]
```

### Outreach best practices

- **Personalize every email.** Templates are starting points, not copy-paste scripts. Reference something specific about their content.
- **Don't ask for links directly.** Suggest your content/product is useful. The link happens if they agree.
- **Follow up once.** One follow-up after 5–7 days is fine. More than that is spam.
- **Expect low response rates.** 5–15% response rate is normal for cold outreach. 2–5% conversion to actual links is good.
- **Track everything.** Use a spreadsheet: prospect URL, contact, date emailed, follow-up date, response, outcome.
- **Quality over volume.** 10 personalized outreach emails per week beats 100 templated blasts.

---

## Link Building Metrics & Tracking

### What to track

| Metric | Frequency | What it tells you |
|---|---|---|
| Total referring domains | Monthly | Overall link authority growth |
| New referring domains (this month) | Monthly | Link building velocity |
| Lost referring domains (this month) | Monthly | Link attrition rate — normal to lose some |
| DR/DA trend | Quarterly | Authority growth (lagging indicator) |
| Outreach sent vs. links earned | Monthly | Outreach efficiency |
| Links earned by content type | Quarterly | What content attracts links — do more of that |
| Referring domain quality mix | Quarterly | Are new links from relevant, authoritative sites? |

### Benchmarks for SaaS link building

| Stage | Referring domains | Monthly growth rate | Notes |
|---|---|---|---|
| **Pre-launch / just launched** | 0–20 | N/A | Directories and launch coverage |
| **Early traction (0–1k organic/mo)** | 20–100 | 5–15/month | Foundation building, integration links |
| **Growth (1k–10k organic/mo)** | 100–500 | 10–30/month | Active outreach + content-driven links |
| **Established (10k+ organic/mo)** | 500+ | 20–50+/month | Full program + digital PR |

These are rough ranges. A site with 50 links from highly relevant, authoritative domains can outrank a site with 500 links from low-quality sources. Quality always beats quantity.

---

## What Not to Do

These link building tactics are either ineffective, risky, or both for SaaS:

1. **Buying links.** Google's algorithm is increasingly good at detecting paid links. The risk/reward is poor. A manual penalty wipes out months of organic growth.

2. **Private Blog Networks (PBNs).** Creating or using a network of fake sites to link to yourself. Google detects and penalizes these. Don't do it.

3. **Link exchanges at scale.** "I'll link to you if you link to me" — one-off natural reciprocal links are fine. Systematic link exchange schemes are detected and devalued.

4. **Automated outreach tools that send hundreds of emails.** Low response rates, high spam risk, damages your domain reputation for email deliverability.

5. **Comment/forum link spam.** Links in blog comments, forum signatures, and profile pages are nofollow and provide zero SEO value. They also annoy people.

6. **Article directories and press release distribution.** These were effective in 2010. Google has devalued these links to near-zero.

7. **Fiverr/cheap link building services.** Any service offering "500 backlinks for $50" is selling spam. These links don't help and may hurt.

The only link building that works long-term for SaaS: creating content worth linking to, and making it easy for relevant sites to find and reference you. Everything else is either a shortcut that doesn't work or a risk that isn't worth taking.
