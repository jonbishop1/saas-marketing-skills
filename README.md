# SaaS Marketing Skills for Claude

**Turn Claude Code into a world-class growth marketer**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]() [![Built by SaaS Growth Pros](https://img.shields.io/badge/Built%20by-SaaS%20Growth%20Pros-black)]()

Hi, I'm Jon and I built this set of skills from my deep experience marketing SaaS products. It's designed specifically for technical founders and has 16 skills covering everything from audience research to content production and ads. These skills encode the frameworks and processes I've used into conversational AI modules that give structured, opinionated strategy customized to your situation.

If you'd prefer a [human marketer](https://saasgrowthpros.com), whether it's for coaching, building out custom marketing skills, or having someone hands-on with your marketing, reach out at [SaaS Growth Pros](https://saasgrowthpros.com).

---

## How Skills Work Together

Skills reference a shared background module (`saas-marketing-background`) that builds cumulative understanding of your product, audience, and goals across a session.

Skills chain naturally:

```
Audience Research → Copywriting → Landing Page → Google Ads → Analytics
         ↘ Content Strategy → SEO Research → Content Production ↗
```

Start anywhere. Claude routes to the right skill based on your question. Ask about your homepage copy and it pulls from the copywriting skill. Ask why your trial conversion is low and it activates onboarding and customer psychology together.

---

## Who This Is For

- **Technical founders** who need marketing leverage
- **Small dev teams** shipping product without a dedicated marketing hire
- **Indie hackers and bootstrappers** who want structured strategy and tactical expertise
- **Agencies building on Claude** who want plug-and-play marketing strategy for their clients

---

## What's Included

| Skill | What it does |
|-------|-------------|
| [saas-audience-research](.agents/skills/saas-audience-research) | Identify your ideal buyers, their pain points, and where they hang out online. Grounds every other skill. |
| [saas-competitive-research](.agents/skills/saas-competitive-research) | Map competitors, analyze positioning and pricing, find gaps you can exploit. |
| [saas-seo-research](.agents/skills/saas-seo-research) | Keyword discovery, topic clusters, SERP analysis, and competitive keyword gaps. |
| [saas-customer-psychology](.agents/skills/saas-customer-psychology) | Jobs-to-Be-Done, buyer motivation, cognitive biases applied to SaaS conversion and retention. |
| [saas-marketing-plan](.agents/skills/saas-marketing-plan) | Prioritized channel strategy based on your stage, budget, and capacity. Where to spend your first dollar and your first hour. |
| [saas-content-strategy](.agents/skills/saas-content-strategy) | Editorial planning, channel selection, content-market fit, and topic prioritization. |
| [saas-seo-audit](.agents/skills/saas-seo-audit) | Technical SEO, content gaps, link profile health, and a prioritized fix list. |
| [saas-landing-pages](.agents/skills/saas-landing-pages) | Page structure, section ordering, hero messaging, CTA optimization, and conversion teardowns. |
| [saas-product-launches](.agents/skills/saas-product-launches) | Launch planning, channel sequencing, pre-launch hype, and post-launch iteration. |
| [saas-google-ads](.agents/skills/saas-google-ads) | Campaign structure, keyword strategy, bidding, conversion tracking, and scaling for SaaS paid search. |
| [saas-meta-ads](.agents/skills/saas-meta-ads) | Creative strategy, audience building, Pixel/CAPI setup, retargeting, and demand gen for paid social. |
| [saas-copywriting](.agents/skills/saas-copywriting) | Homepage, pricing pages, ad copy, email sequences, sales collateral, and value proposition development. |
| [saas-content-production](.agents/skills/saas-content-production) | Blog posts, guides, comparisons, content briefs, editing, and cross-channel repurposing. |
| [saas-onboarding](.agents/skills/saas-onboarding) | Signup flow design, activation strategy, trial optimization, and in-app onboarding flows. |
| [saas-data-analysis](.agents/skills/saas-data-analysis) | Event tracking, funnel analysis, cohort retention, attribution, KPI definition, and tool selection. |
| [saas-marketing-background](.agents/skills/saas-marketing-background) | Shared intake background referenced by all other skills. Stores your product, audience, and positioning so every skill starts informed. |

---

## Install

```
/plugin marketplace add jonbishop1/saas-marketing-skills
/plugin install saas-marketing-skills@saas-growth-pros
/reload-plugins
```

Then try this:

> "I'm building a developer tool that does [X]. I have no marketing hire and $500/month for ads. Help me build a marketing plan."

Claude will activate the `saas-marketing-plan` skill and walk you through a structured channel strategy in minutes.

---

## License

MIT — use it, fork it, build on it.
