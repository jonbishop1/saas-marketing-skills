# Section Blueprints by Product Type

Full section-by-section page architecture for each SaaS product type. Sections are listed in recommended order. Priority indicates whether the section is essential (must-have for Tier 1), important (include in Tier 2), or optional (Tier 3 or context-dependent).

---

## Table of Contents

1. [How to Use These Blueprints](#how-to-use-these-blueprints)
2. [PLG / Self-Serve SaaS](#plg--self-serve-saas)
3. [Sales-Led / Enterprise SaaS](#sales-led--enterprise-saas)
4. [Developer Tools / API Products](#developer-tools--api-products)
5. [Content / SEO Tools](#content--seo-tools)
6. [Universal Sections Reference](#universal-sections-reference)
7. [Section Ordering Principles](#section-ordering-principles)

---

## How to Use These Blueprints

These are starting points, not rigid templates. Adapt based on the founder's situation assessment:

- **Pre-launch / Tier 1:** Use only "Essential" sections. Ship fast.
- **Post-launch / Tier 2:** Add "Important" sections. Prioritize whichever addresses your biggest conversion gap.
- **Optimizing / Tier 3:** Add "Optional" sections and test their impact.

If the founder is missing an asset needed for a section (e.g., no testimonials for a social proof section), skip the section rather than filling it with weak content. Weak sections hurt more than absent ones.

---

## PLG / Self-Serve SaaS

The page replaces the sales team. It must explain, convince, and convert in a single scroll.

| Order | Section | Priority | Purpose | Notes |
|---|---|---|---|---|
| 1 | Hero | Essential | What you do, who it's for, primary CTA | Include product screenshot or short demo gif if available |
| 2 | Logo bar | Important | Social proof — who uses this | Skip if <5 recognizable logos |
| 3 | Problem statement | Essential | Mirror the visitor's pain | 2–3 sentences. Use the customer's language, not yours. |
| 4 | Feature/benefit cards | Essential | What the product does, framed as outcomes | 3–4 cards max. Each: icon/visual + headline + 1-2 sentences |
| 5 | Product walkthrough | Important | Show the product in action | Screenshots with annotations, or short video (<90s) |
| 6 | Social proof | Important | Testimonials, metrics, case study snippets | 2–3 quotes with name, title, company. Specific outcomes. |
| 7 | How it works | Important | Reduce perceived complexity | 3 steps. "Sign up → Connect → Get insights." Keep it dead simple. |
| 8 | Pricing | Important | Remove friction, show transparency | For PLG with free tier: show it prominently. This is a competitive advantage. |
| 9 | FAQ | Optional | Handle remaining objections | 5–8 questions. Focus on friction questions: security, integration, migration, data ownership. |
| 10 | Comparison table | Optional | Win against specific competitors | Only if you genuinely win on the dimensions you compare. Don't cherry-pick. |
| 11 | Final CTA | Essential | Last conversion opportunity | Restate value prop in one line + CTA button |

### PLG architecture notes

- The hero does 60%+ of the conversion work. Invest disproportionate time here.
- Pricing on the page is strongly recommended for PLG. Visitors who can't find pricing leave and don't come back.
- "How it works" is more important when the product concept is unfamiliar. If your category is well-understood (e.g., project management), you can skip this.
- The product walkthrough section is highest-impact when the product has a visually impressive UI. If your product is a CLI tool or API with no visual interface, replace this with a code example or integration diagram.

---

## Sales-Led / Enterprise SaaS

The page generates qualified leads. It must signal credibility and authority, then make the demo request feel safe and valuable.

| Order | Section | Priority | Purpose | Notes |
|---|---|---|---|---|
| 1 | Hero | Essential | What you do, who it's for, demo CTA | Enterprise hero should emphasize outcome and scale, not features |
| 2 | Logo bar | Essential | Credibility through recognized names | Enterprise buyers need to see companies like theirs. This is near-essential. |
| 3 | Problem/stakes | Essential | Why this matters to the business | Frame the cost of the problem, not just the problem. "Teams lose X hours/week to..." |
| 4 | Solution overview | Important | What you do at a high level | Not feature bullets. A narrative: "We do X so your team can Y." |
| 5 | Feature deep-dive | Important | Specific capabilities | 3–5 features with more detail than PLG. Enterprise buyers research thoroughly. |
| 6 | Social proof | Essential | Case studies, testimonials, results | Enterprise needs deeper proof: case studies with named companies and measurable outcomes. |
| 7 | Security/compliance | Important | Trust signals | SOC 2, GDPR, SSO, SLA guarantees. List what you have. |
| 8 | Integration ecosystem | Optional | Show it fits their stack | Logo grid of integrations, or "Works with Salesforce, Slack, Jira..." |
| 9 | How it works / implementation | Important | Reduce deployment fear | Address the enterprise concern: "How hard is this to implement?" Give a timeline. |
| 10 | FAQ | Optional | Handle procurement objections | Security, data handling, contract terms, onboarding timeline |
| 11 | Final CTA | Essential | Demo request with friction reducer | "Book a 15-minute demo" — specify time to reduce perceived commitment |

### Sales-led architecture notes

- Logo bar is near-essential for enterprise. If you don't have enterprise logos, use industry language that signals you understand their world.
- Social proof needs depth, not breadth. One detailed case study outperforms five generic quotes.
- Do NOT put pricing on a sales-led page unless your pricing is simple and competitive. For enterprise, pricing is a conversation — the page should drive to that conversation.
- Security and compliance signals are table stakes for enterprise. If you have SOC 2, say so. If you don't, list what you do have (encryption at rest, role-based access, audit logs).

---

## Developer Tools / API Products

Developers are the hardest audience to market to. They distrust marketing, value technical substance, and will evaluate your docs before your landing page. Respect their intelligence.

| Order | Section | Priority | Purpose | Notes |
|---|---|---|---|---|
| 1 | Hero | Essential | What it does + code sample or API call | Show a real code snippet. "Get started in 3 lines of code" > "Easy to integrate" |
| 2 | Code example | Essential | Prove it works | A real, runnable code sample. Multiple language tabs if applicable. |
| 3 | Key capabilities | Essential | What it does, technically | Feature cards with technical specificity. "Sub-50ms p99 latency" > "Fast" |
| 4 | Architecture / how it works | Important | Technical credibility | A system diagram, data flow, or infrastructure overview. Developers want to understand the system. |
| 5 | Integration section | Important | Show it fits their stack | SDKs, libraries, frameworks supported. Link to docs. |
| 6 | Social proof | Important | Other developers use this | GitHub stars, "Used by X developers," testimonials from technical leads |
| 7 | Pricing | Important | Transparent, usage-based preferred | Developers strongly prefer pay-as-you-go or generous free tiers. Show it. |
| 8 | Docs link / quick start | Important | Let them self-serve | Prominent link to documentation. Developers want to try before they talk to anyone. |
| 9 | Comparison table | Optional | Technical differentiation | Compare on technical dimensions: latency, uptime SLA, rate limits, pricing per unit |
| 10 | Final CTA | Essential | Get API key or start building | "Get your API key" or "Start building" — action-oriented, no sales language |

### Developer tools architecture notes

- The code example IS the hero for developer tools. If your hero doesn't show code, you've lost technical credibility immediately.
- Avoid marketing speak. "Revolutionary AI-powered platform" makes developers close the tab. "Webhook delivery with automatic retries and exactly-once guarantees" makes them read more.
- Link to docs early and prominently. Developers will judge your product by your documentation quality. If your docs are good, the link is a conversion tool.
- GitHub presence matters. If you're open-source or have open-source components, show GitHub stars and contributor count. If your repo is active, link to it.

---

## Content / SEO Tools

Users arrive from search with a specific problem. They're comparing solutions. The page must validate their search intent, show how you solve their specific problem, and differentiate from the 5 other tools they've looked at today.

| Order | Section | Priority | Purpose | Notes |
|---|---|---|---|---|
| 1 | Hero | Essential | Mirror their search intent + CTA | Headline should echo the problem they searched for, not your brand positioning |
| 2 | Problem validation | Essential | "You have this problem. Here's why." | Validate the frustration that led them to search. Be specific. |
| 3 | Product demo / walkthrough | Essential | Show the tool solving their problem | Screenshots or video showing the exact workflow: input → analysis → output |
| 4 | Feature/benefit cards | Important | What the tool does | Frame each feature as a workflow improvement: "Find keyword gaps in 30 seconds, not 3 hours" |
| 5 | Social proof | Important | Other marketers/SEOs use this | Testimonials from recognizable names in the SEO/content community carry outsized weight |
| 6 | Comparison section | Important | Why you vs. alternatives | Content/SEO tool buyers comparison-shop aggressively. Address it head-on. |
| 7 | Pricing | Important | Transparent, with free trial emphasis | Emphasize the free trial. Lower the barrier. |
| 8 | Use cases | Optional | Different ways to use the tool | "For content teams," "For freelance SEOs," "For agencies" — helps visitors self-identify |
| 9 | FAQ | Optional | Handle tool-specific objections | Data freshness, accuracy, source coverage, export options |
| 10 | Final CTA | Essential | Start free trial | Repeat the core promise + CTA |

### Content / SEO tools architecture notes

- These users are research-mode buyers. They've probably looked at 3–5 alternatives before landing on your page. Your comparison section is a conversion tool, not an afterthought.
- Show the product solving a real problem with real data. Blurred or fake screenshots immediately signal "this tool doesn't actually work yet."
- Content/SEO tool buyers value data accuracy and freshness. If your data is better than competitors', prove it with a specific comparison.

---

## Universal Sections Reference

These sections work across all product types. Adapt language and emphasis to the product type.

### Hero section anatomy

Every hero needs exactly these elements, in this visual hierarchy:

1. **Headline** (biggest text on the page) — What you do, in outcome terms
2. **Subheadline** (smaller, below headline) — Who it's for and/or how it works
3. **Primary CTA** (most visually prominent element) — The action you want them to take
4. **Visual** (screenshot, illustration, or code sample) — Proof the product exists
5. **Secondary proof point** (optional) — "Trusted by 500+ teams" or "No credit card required"

Common hero mistakes: too many CTAs, no visual, headline that's a tagline instead of a description, subheadline that repeats the headline in different words.

### FAQ section guidance

FAQ is an objection-handling section disguised as a helpful resource. Structure questions around the objections that prevent conversion:

- **Friction objections:** "Do I need a credit card?" "How long does setup take?" "Can I cancel anytime?"
- **Trust objections:** "Is my data secure?" "Who else uses this?" "What happens to my data if I cancel?"
- **Fit objections:** "Does this work with [tool]?" "Is this for small teams or enterprise?" "Do you support [feature]?"
- **Value objections:** "How is this different from [competitor]?" "Why shouldn't I just use [free alternative]?"

5–8 questions is the right range. More than 10 makes the section feel like a disclaimer dump.

---

## Section Ordering Principles

When adapting these blueprints, follow these ordering rules:

1. **Hero always first.** No exceptions.
2. **Social proof as early as possible.** Logo bar directly after hero (if you have logos). Testimonials in the top half of the page (if you have strong ones).
3. **Address the biggest objection early.** If your biggest conversion barrier is "I don't understand what this does," put the product walkthrough second. If it's "I don't trust this company," put social proof second.
4. **CTA after every emotional peak.** After a testimonial that builds trust, offer the CTA. After a demo that shows value, offer the CTA. Don't wait until the end.
5. **FAQ and comparison tables go near the bottom.** These serve visitors who've already read the page and need final reassurance. Don't lead with them.
6. **Final CTA is always last.** One-line value prop restatement + CTA button. This catches the "I scrolled everything and I'm ready" visitor.
