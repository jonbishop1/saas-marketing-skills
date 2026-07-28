# Content Types Guide

Complete writing frameworks, structures, brief templates, and examples for every SaaS content type. Each section covers: what it is, when to produce it, how to structure it, a brief template, and examples for both an API monitoring product (PingForge) and an SEO keyword research product (KeyScope).

---

## Table of Contents

1. [Comparison Pages](#comparison-pages)
2. [Alternative Pages](#alternative-pages)
3. [Use-Case Pages](#use-case-pages)
4. [Integration Pages](#integration-pages)
5. [How-To Guides](#how-to-guides)
6. [Definitive Guides](#definitive-guides)
7. [Case Studies](#case-studies)
8. [Docs-as-Content](#docs-as-content)
9. [Data Studies and Original Research](#data-studies-and-original-research)
10. [Changelog and Product Updates](#changelog-and-product-updates)
11. [Brief Templates](#brief-templates)

---

## Comparison Pages

### What it is
"[Your Product] vs [Competitor]" pages targeting people actively evaluating tools. Bottom-funnel, high conversion rate.

### When to produce
Immediately post-launch. Create one for each direct competitor. These are some of the highest-converting pages a SaaS site can have.

### Structure

```
H1: [Your Product] vs [Competitor]: [Honest framing]
├── Quick summary table (features, pricing, best for)
├── H2: Overview of [Competitor]
│   └── What they do well, who they're best for
├── H2: Overview of [Your Product]
│   └── Your strengths, who you're best for
├── H2: Detailed comparison
│   ├── H3: [Dimension 1 — e.g., Setup & onboarding]
│   ├── H3: [Dimension 2 — e.g., Core features]
│   ├── H3: [Dimension 3 — e.g., Pricing]
│   ├── H3: [Dimension 4 — e.g., Integrations]
│   └── H3: [Dimension 5 — e.g., Support & docs]
├── H2: When to choose [Competitor]
│   └── Be honest — say when they're the better fit
├── H2: When to choose [Your Product]
│   └── Your winning scenarios
└── CTA: Try [Your Product] free
```

### Writing principles
- **Be honest.** Concede where the competitor wins. Readers can smell bias, and honesty builds trust. "If you need a full enterprise observability suite, Datadog is the better choice" makes "If you need focused API monitoring at a fraction of the cost, PingForge wins" far more credible.
- **Compare on dimensions that matter to the buyer**, not dimensions where you win. If pricing isn't a differentiator, don't lead with it.
- **Include the quick comparison table above the fold.** Most readers scan the table, then read the sections relevant to their decision.
- **Target word count:** 1,200–2,500 words depending on how many dimensions to compare.

### PingForge example brief

```
Target keyword: "PingForge vs Better Uptime"
Intent: Commercial investigation — reader is choosing between two tools
Structure: Comparison page
Honest angle: Better Uptime has a broader feature set and more integrations.
PingForge wins on: setup speed (30 sec vs 5 min), developer experience,
latency monitoring depth (percentile tracking), pricing simplicity.
When to choose Better Uptime: Need status pages, broader incident management.
When to choose PingForge: Developer team wanting fast, focused API monitoring.
CTA: Start monitoring free — 30-second setup
Word count: ~1,500
```

### KeyScope example brief

```
Target keyword: "KeyScope vs Mangools"
Intent: Commercial investigation — reader is evaluating mid-market keyword tools
Structure: Comparison page
Honest angle: Mangools has a more established brand and broader feature suite
(rank tracking, SERP analysis, link analysis). KeyScope is focused.
KeyScope wins on: keyword gap analysis depth, opportunity scoring accuracy,
speed to first insight (5 min vs 20+ min), simpler UX.
When to choose Mangools: Need an all-in-one SEO suite at mid-market pricing.
When to choose KeyScope: Keyword gap analysis is your primary workflow.
CTA: Try free for 14 days — see your keyword gaps in 5 minutes
Word count: ~1,800
```

---

## Alternative Pages

### What it is
"[Competitor] alternatives" pages targeting people actively looking to switch or explore options. Bottom-funnel.

### When to produce
Immediately post-launch. Create one for each major competitor. These target searchers who've already decided the competitor isn't right — they're looking for you.

### Structure

```
H1: Best [Competitor] Alternatives [for Your Audience] in [Year]
├── Quick comparison table (you + 3-5 alternatives, including yourself)
├── H2: Why look for [Competitor] alternatives?
│   └── Common pain points that drive switching (research these from reviews, forums)
├── H2: [Your Product] — Best for [your differentiator]
│   └── Why you're listed first (you are the author, and you genuinely fit)
├── H2: [Alternative 2] — Best for [their strength]
├── H2: [Alternative 3] — Best for [their strength]
├── H2: [Alternative 4] — Best for [their strength]
├── H2: How to choose the right [Competitor] alternative
│   └── Decision framework based on use case, budget, team size
└── CTA
```

### Writing principles
- **List yourself, but include real alternatives.** A page with only your product isn't credible. Include 4–6 real alternatives with honest assessments.
- **Research actual pain points.** Check G2 reviews, Reddit threads, and Twitter complaints about the competitor. Use real frustrations as the framing for "why switch."
- **Don't trash the competitor.** Acknowledge their strengths while positioning alternatives for specific needs.
- **Target word count:** 1,500–3,000 words depending on how many alternatives.

---

## Use-Case Pages

### What it is
"[Your Product] for [specific use case or industry]" pages. Target searchers with a specific need that your product solves.

### When to produce
Month 1–3 post-launch. Prioritize use cases where you have the strongest product fit and customer evidence.

### Structure

```
H1: [Your Product] for [Use Case/Industry]
├── H2: The [use case] challenge
│   └── What makes this problem hard? What are the current solutions?
├── H2: How [Your Product] solves [use case]
│   └── Specific features mapped to specific pain points
├── H2: [Feature 1] for [use case]
│   └── Concrete example of how this feature helps
├── H2: [Feature 2] for [use case]
├── H2: Results / social proof
│   └── Customer testimonials, metrics, or case study excerpt
├── H2: Getting started with [Your Product] for [use case]
│   └── Quick setup guide specific to this use case
└── CTA
```

### PingForge example
"PingForge for E-Commerce APIs" — targeting API teams at e-commerce companies where downtime means lost revenue.

### KeyScope example
"KeyScope for SaaS Content Teams" — targeting content marketers at SaaS companies who need to find keyword gaps to plan their editorial calendar.

---

## Integration Pages

### What it is
"[Your Product] + [Tool]" pages. Target users of the integrated tool who are searching for how to extend it.

### When to produce
As each integration ships. These are evergreen pages that also earn links from partner integration directories.

### Structure

```
H1: Connect [Your Product] with [Tool]
├── H2: What the integration does
│   └── 2-3 sentence summary of the value
├── H2: How it works
│   └── Step-by-step setup (with screenshots)
├── H2: Use cases
│   └── 2-3 specific scenarios where this integration helps
├── H2: Getting started
│   └── Prerequisites, setup link, time to value
└── CTA
```

### Writing principles
- Keep it practical. Integration pages are task-oriented — the reader wants to know what it does and how to set it up.
- Include screenshots. Integration setup is visual.
- Short: 500–1,000 words is usually sufficient.
- These double as documentation and marketing content.

---

## How-To Guides

### What it is
Guides that solve a specific problem the target audience has. Mid-funnel — the reader has a problem, and your content teaches them to solve it (with your product being one path to the solution).

### When to produce
Month 2–4 post-launch. After bottom-funnel pages exist.

### Structure

```
H1: How to [Solve Problem] [optional: qualifier like "in 2024" or "for Developers"]
├── H2: Why [problem] matters / what happens if you don't solve it
│   └── Establish urgency or stakes
├── H2: [Approach/Method 1]
│   ├── Step-by-step instructions
│   └── Code examples, screenshots, or concrete details
├── H2: [Approach/Method 2] (if applicable)
├── H2: [Approach/Method 3] (if applicable)
├── H2: Common mistakes / pitfalls
├── H2: Tools that help (mention your product naturally among others)
└── CTA
```

### Writing principles
- **Actually solve the problem.** The reader came for a solution, not a product pitch. If the guide is useful without your product, you've done it right — and the natural product mention in the "tools" section is more credible.
- **Be specific.** "Use monitoring" is not a how-to. "Set up endpoint monitoring with 30-second check intervals and Slack alerts for 5xx errors" is a how-to.
- **Include code when relevant.** For developer audiences, runnable code examples dramatically increase content quality and shareability.
- **Target word count:** 1,000–2,500 words depending on topic complexity.

### PingForge example
"How to Monitor REST API Uptime: A Developer's Guide" — walks through monitoring setup with multiple approaches, including manual curl scripts, open-source tools, and SaaS tools (PingForge mentioned naturally alongside Uptime Robot, Better Uptime).

### KeyScope example
"How to Find Keywords Your Competitors Rank For" — explains the keyword gap analysis process using free methods (manual SERP analysis, Search Console) and paid tools (Ahrefs, KeyScope), with KeyScope's gap analysis as one approach.

---

## Definitive Guides

### What it is
Comprehensive, authoritative content on a core topic in your space. Top-to-mid funnel. These build topical authority and attract backlinks.

### When to produce
Month 3–6 post-launch. These require significant investment — don't produce them before bottom-funnel content exists.

### Structure

```
H1: The Complete Guide to [Topic] [optional: for Audience]
├── Table of contents (these are long — readers need navigation)
├── H2: What is [topic]?
│   └── Definition and framing for the audience
├── H2: Why [topic] matters for [audience]
├── H2: [Core concept 1]
│   └── Deep explanation with examples
├── H2: [Core concept 2]
├── H2: [Core concept 3]
├── H2: How to get started with [topic]
│   └── Practical first steps
├── H2: Tools for [topic]
│   └── Your product among others
├── H2: Common mistakes
├── H2: FAQ
└── CTA
```

### Writing principles
- **This is your authority piece.** It should be the best single resource on this topic on the internet. That's a high bar — don't publish a definitive guide that isn't definitively useful.
- **Include original insights.** Anyone can compile information from other guides. Your guide should contain things that come from your expertise, your data, or your experience.
- **Link heavily internally.** A definitive guide is the hub of a topic cluster. Link to every related piece on your site.
- **Target word count:** 2,500–5,000+ words. Length should be driven by topic coverage, not word count targets.

---

## Case Studies

### What it is
Customer success stories that demonstrate real-world results. Bottom-funnel — shows prospects that people like them are succeeding with your product.

### When to produce
When you have customer stories worth telling. Don't fabricate urgency — wait for genuine results.

### Structure

```
H1: How [Customer] [achieved result] with [Your Product]
├── H2: The challenge
│   └── What problem did the customer face? (In their words if possible)
├── H2: Why [Your Product]
│   └── What were they using before? Why did they switch?
├── H2: The solution
│   └── How they implemented your product (specific, not generic)
├── H2: The results
│   └── Metrics, quotes, before/after comparison
├── Key metrics callout box (visual highlight of top numbers)
└── CTA
```

### Writing principles
- **Metrics are mandatory.** A case study without numbers is a testimonial. "Reduced API downtime by 73%" is a case study. "Really improved our monitoring" is not.
- **Name the customer if possible.** Named case studies are 3–5× more credible than anonymous ones.
- **Include the customer's voice.** Direct quotes from the actual user, ideally with their name and title.
- **Keep it focused.** One customer, one problem, one solution, one result. Don't try to cover everything they use your product for.
- **Target word count:** 800–1,500 words. Case studies should be concise.

---

## Docs-as-Content

### What it is
Product documentation that also ranks in search and attracts organic traffic. Not separate from docs — the documentation itself serves double duty.

### When to produce
When your documentation answers questions people actively search for. Common for developer tools and API products.

### What qualifies as docs-as-content
- API reference pages that answer "how to [do thing] with [technology]"
- Setup guides that answer "how to integrate [tool] with [ecosystem tool]"
- Conceptual docs that answer "what is [concept]" or "how does [concept] work"
- Troubleshooting pages that answer "why is [thing] not working"

### Writing principles
- **Don't compromise documentation quality for SEO.** The primary audience is your users. If SEO optimization hurts the docs experience, keep it as docs.
- **Add SEO elements without disrupting the UX.** Title tags, meta descriptions, and structured data can be added without changing the content.
- **Make docs publicly accessible.** Docs behind a login wall can't rank. Many SaaS products gate docs unnecessarily.
- **Stripe's playbook:** Stripe's documentation ranks for thousands of developer queries because it's comprehensive, publicly accessible, well-structured, and answers the exact questions developers search for. You don't need Stripe's scale — you need their approach.

---

## Data Studies and Original Research

### What it is
Content based on original data analysis — typically from your product's data (anonymized) or from research you conduct. Top-funnel but extremely valuable for link building and brand authority.

### When to produce
Month 6+ post-launch, when you have meaningful data. Don't force this earlier — bad data studies are worse than no data study.

### Structure

```
H1: [Headline with key finding]: We Analyzed [Data Set]
├── Key findings summary (3-5 bullet points above the fold)
├── H2: Methodology
│   └── What data, how collected, sample size, limitations
├── H2: Finding 1
│   └── Data visualization + analysis + implications
├── H2: Finding 2
├── H2: Finding 3
├── H2: What this means for [audience]
│   └── Practical takeaways
├── H2: Methodology notes / limitations
└── CTA
```

### PingForge example
"We Analyzed 1M API Health Checks: Here's What We Learned About Uptime Patterns" — using anonymized data from PingForge's monitoring to reveal insights about when APIs fail, most common failure modes, and correlation between check frequency and incident detection time.

### KeyScope example
"The Real Accuracy of Keyword Difficulty Scores: We Tested 50,000 Keywords" — using KeyScope's data to compare predicted keyword difficulty against actual ranking outcomes, revealing how often difficulty scores are misleading.

### Writing principles
- **Methodology matters.** Explain how you got the data. Without methodology, it's opinion, not research.
- **Visualize data.** Charts and graphs make data studies shareable and link-worthy.
- **Lead with the most surprising finding.** The headline should make someone think "I need to read this."
- **Be honest about limitations.** "Our data comes from [specific source], which may skew toward [specific pattern]" builds credibility.
- **Target word count:** 1,500–3,000 words. Dense with data, not padded with filler.

---

## Changelog and Product Updates

### What it is
Regular updates about what's new in the product. Low effort, mid-funnel, and signals freshness to both users and search engines.

### Structure
Keep it simple and consistent:

```
H1: [Month Year] Updates: [Headline Feature]
├── H2: [Major feature]
│   └── What it does, why it matters, screenshot/gif
├── H2: Improvements
│   └── Bullet list of meaningful improvements
├── H2: Bug fixes
│   └── Brief list (users appreciate transparency)
└── What's next (optional teaser)
```

### Writing principles
- **Frame features as outcomes.** "New Slack integration" → "Get API alerts in Slack without leaving your workflow."
- **Publish consistently.** Monthly or bi-weekly. Consistency builds an audience for updates.
- **Keep it scannable.** Users skim changelogs. Use headings, bullets, and screenshots.
- **Target word count:** 300–800 words. Short and focused.

---

## Brief Templates

### Universal brief template

Use this as the starting point for any content type. Adapt per type using the structures above.

```
## Content Brief

**Content type:** [blog post / guide / comparison / alternative / use-case / case study / etc.]
**Target keyword:** [primary keyword]
**Secondary keywords:** [2-5 related terms]
**Search intent:** [informational / commercial investigation / transactional]
**Target audience:** [who is reading, what's their role, what do they know]
**Awareness level:** [problem-aware / solution-aware / product-aware]

**SERP analysis:**
- Top 3 current results:
  1. [URL] — [type, word count, approach, what they do well, what's missing]
  2. [URL] — [same]
  3. [URL] — [same]
- Opportunity: [what can you say/do that they can't?]

**Outline:**
[H2 and H3 structure with notes under each]

**Key points to cover:**
- [Point 1 — with source or evidence]
- [Point 2]
- [Point 3]

**Unique angle / founder expertise to include:**
[What original insight, data, or experience makes this piece different?]

**CTA:** [What should the reader do next?]
**Internal links:** [Pages to link to from this piece + pages that should link to it]
**Word count target:** [Based on SERP analysis]
**Deadline:** [Date]
```

### Quick brief (Tier 1 — 10 minutes)

When the founder is writing for themselves and needs speed:

```
**Keyword:** [target keyword]
**Who's reading:** [audience in one sentence]
**What they need:** [what would satisfy this search?]
**My angle:** [what can I say that Google's top results can't?]
**Structure:** [H2 headings as bullet list]
**CTA:** [next step]
**Word count:** [rough target]
```

Even this abbreviated brief dramatically improves output quality vs. writing without any brief.
