---
name: saas-marketing-plan
description: >
  Strategic marketing planning for developers and technical founders building SaaS products, developer tools/APIs, and enterprise software. Use this skill for any question about marketing strategy, channel selection, marketing planning, go-to-market strategy, launch strategy, growth strategy, which channels to use, how to allocate marketing budget, what to do first, marketing roadmap, marketing priorities, competitive marketing analysis, or figuring out the right marketing approach given limited time and resources. Trigger whenever a user asks about making a marketing plan, choosing between channels, deciding where to spend money or time on marketing, planning a launch, or any strategic marketing question — even if they just say "how do I market this" or "where should I start with marketing" or "I don't have time for marketing."
---

# SaaS Marketing Plan

Audience: developers and technical founders. Explain things in engineering terms. Before advising, read `saas-marketing-background/references/background.md` and gather missing background. Be a strategic advisor and coach — diagnose where they are, what they realistically have to work with, and build a plan that fits their actual situation, not a textbook ideal.

This is the coordinator skill. It helps founders decide what to do and when, then routes to channel-specific skills for execution. Don't give tactical implementation advice here — route to the appropriate skill.

---

## Table of Contents

1. [Why Strategy Before Tactics](#why-strategy-before-tactics)
2. [Situation Assessment](#situation-assessment)
3. [Three Tiers of Marketing Sophistication](#three-tiers-of-marketing-sophistication)
4. [Channel Selection Framework](#channel-selection-framework)
5. [Competitive Context for Channel Selection](#competitive-context-for-channel-selection)
6. [Phasing and Sequencing](#phasing-and-sequencing)
7. [Budget Allocation](#budget-allocation)
8. [Routing to Channel Skills](#routing-to-channel-skills)
9. [Reference Files](#reference-files)

---

## Why Strategy Before Tactics

Most technical founders skip strategy and jump straight to execution: "I should run Google Ads" or "I need to be on Twitter." This is like writing code before understanding the requirements.

Strategy answers three questions in order:
1. **Who** are you trying to reach? (audience — informed by `saas-audience-research`)
2. **Where** can you reach them? (channels — this skill)
3. **What** do you say when you get there? (messaging — informed by audience research language)

Without answers to these, every tactical channel is a guess. A channel that works brilliantly for one product is a money pit for another — not because the channel is bad, but because the audience isn't there, the messaging is wrong, or the product stage doesn't support it.

**The resource constraint is real.** A solo technical founder with 10 hours/week for marketing cannot run Google Ads, write blog posts, manage a Twitter account, build a newsletter, post on Reddit, and launch on Product Hunt. Trying to do all of them means doing none of them well. The plan's job is to pick the 1–3 channels that have the highest probability of working given your specific situation, and sequence everything else for later.

**Example — API monitoring product:**
A solo founder with strong DevOps community ties and no marketing budget. Strategy says: community-first (Reddit, Hacker News, DevOps Slack groups) + documentation-driven SEO. Paid ads come later when there's revenue to fund them. Trying to run Meta Ads for a developer tool with no creative assets would be wasted money.

**Example — SEO keyword research tool:**
A two-person team with some budget and strong content skills. Strategy says: content/SEO (practice what you preach — rank for your own category keywords) + targeted Google Ads for high-intent searches. Meta Ads come later, if at all, because the audience searches for solutions rather than discovering them on social.

---

## Situation Assessment

This is the most important section. The plan depends entirely on what the founder actually has to work with. Don't skip this to get to the "fun" channel selection part.

### Resource Inventory

**Time available for marketing:**
- < 5 hrs/week — pick ONE channel, do it consistently
- 5–10 hrs/week — one primary channel + one supporting channel
- 10–20 hrs/week — two primary channels + one experiment
- 20+ hrs/week (or dedicated marketing person) — full multi-channel strategy

Be ruthless about this number. "I can probably do 10 hours" from a founder who's also writing code, doing support, and fundraising is really 3–5 hours. Use the lower bound.

**Budget available for marketing:**
- $0/month — organic only: content, community, social, partnerships
- $1,000–3,000/month — organic + one paid channel (minimum viable paid budget)
- $3,000–10,000/month — organic + one sustained paid channel, scaling
- $10,000+/month — consider adding a second paid channel only if the first is performing

**Skills and strengths:**
- Can you write well? (content marketing, SEO, social)
- Are you active in relevant communities already? (community marketing)
- Do you have design skills or access to a designer? (paid social, Product Hunt)
- Are you comfortable on camera? (YouTube, video content)
- Do you have existing relationships with influencers or journalists? (PR, partnerships)
- Do you have technical SEO skills? (programmatic SEO, technical content)
- Do you have data or unique insights to share? (thought leadership, original research)

**Product characteristics that affect channel selection:**

| Product trait | Channel implication |
|---|---|
| Users search for solutions (existing category) | SEO + Google Ads are high-value |
| New category (users don't know to search) | Content education + social + community |
| Visual product / easy to demo | Video, social media, paid social |
| Developer audience | Community, technical content, HN, dev-focused platforms |
| Non-technical buyer | Paid social, LinkedIn, email marketing, webinars |
| Long sales cycle / high ACV | LinkedIn, content, email nurture, events |
| PLG / self-serve | SEO, Google Ads, Product Hunt, community |
| API product | Developer communities, documentation-as-marketing, technical blogs |

**Current state:**
- Pre-launch? The plan is: get to launch. Everything else waits.
- Launched but no traction? Validate the channel, not the plan.
- Some traction, want to grow? Now a plan matters.
- Profitable, want to scale? Multi-channel sequencing and budget allocation.

---

## Three Tiers of Marketing Sophistication

### Tier 1 — One Channel, Done Consistently (Pre-launch to early, minimal resources)

Pick ONE channel. Execute on it every week. Measure whether it produces signups. That's the whole plan.

**How to pick the one channel:**
1. Where does your audience already spend time? (from audience research or your gut)
2. Which channel plays to your existing strengths?
3. Which channel has the fastest feedback loop? (you need to learn quickly)

| If your strength is... | Start with... | Feedback speed |
|---|---|---|
| Writing + technical depth | Long-form content / SEO | Slow (3–6 months for organic traffic) |
| Already active in communities | Community marketing (Reddit, HN, forums, Discord) | Fast (days to weeks) |
| Existing audience (Twitter, newsletter) | Social / email marketing | Fast (days) |
| Budget but no time | Google Ads (if category has search volume) | Fast (days) |
| Visual product + some budget | Paid social (Meta, LinkedIn) | Medium (2–4 weeks) |
| Strong network | Partnerships, co-marketing, referrals | Medium (weeks) |

**Performance note:** Tier 1 will feel painfully slow. One channel, done consistently, with a small audience, produces small numbers. That's correct. The goal is to find a channel that works at small scale — and then scale it. Spreading across five channels at this stage means you can't tell which one is working.

**When to switch channels:** If after 6–8 weeks of consistent effort you're getting zero traction (not low — zero), the channel may be wrong. But first check: are you actually reaching the right people with a compelling message? Most "channel doesn't work" problems are messaging problems.

### Tier 2 — Primary + Supporting (Some traction, modest resources)

You've found one channel that produces some results. Now add a supporting channel that compounds the primary.

**Good channel combinations:**

| Primary | Supporting | Why they compound |
|---|---|---|
| Content/SEO | Email newsletter | SEO brings visitors, email recaptures and nurtures them |
| Google Ads | Content/SEO | Ads drive immediate traffic, content builds organic over time |
| Community | Content/SEO | Community engagement surfaces content topics, content drives community growth |
| Paid social | Retargeting (Google/Meta) | Cold ads drive awareness, retargeting converts warm visitors |
| Content/SEO | Social media | Content provides material for social, social drives traffic to content |

**What you add:**
- A second channel that supports the first
- Basic measurement: which channel → which signups → which activations (use `saas-data-analysis`)
- Monthly review: is each channel producing results proportional to time/money invested?

### Tier 3 — Multi-Channel System (Growth stage, dedicated resources)

Marketing becomes a system with multiple channels working together, measured cohesively.

**What you add:**
- 3–5 active channels with clear roles (acquisition, nurture, retention, brand)
- Budget allocation across channels with performance tracking
- Channel-level CAC and LTV analysis (use `saas-data-analysis`)
- Quarterly planning and reallocation based on data
- Content and messaging consistency across channels
- Team or contractors executing channels you can't do yourself

See `references/planning.md` → Multi-Channel Coordination for frameworks and templates.

---

## Channel Selection Framework

Every channel is evaluated on five dimensions relevant to a resource-constrained technical founder. Full channel profiles with implementation guidance are in `references/channels-paid.md` (paid channels) and `references/channels-organic.md` (organic channels).

### Channel Quick Reference

| Channel | Time cost | Money cost | Time to results | Technical founder fit | Best when |
|---|---|---|---|---|---|
| **Content / SEO** | High | Low | Slow (3–6 mo) | Strong (if you write well) | Category has search volume, audience researches before buying |
| **Google Search Ads** | Medium | Medium–High | Fast (days) | Medium | Category has search volume, known intent keywords |
| **Meta Ads** | Medium | Medium–High | Medium (2–4 wks) | Low–Medium | Broad audience, visual product, proven creative |
| **LinkedIn (organic)** | Medium | Low | Medium | Medium | B2B, enterprise buyers, professional audience |
| **LinkedIn Ads** | Low–Medium | High | Medium | Medium | Enterprise, high-ACV sales, ABM |
| **Twitter/X** | Medium | Low | Medium | Strong (for dev tools) | Developer audience, thought leadership, real-time engagement |
| **Reddit / Forums** | Medium | Low | Fast (days) | Strong | Technical audience, honest discussions, niche communities |
| **Hacker News** | Low | Low | Fast (one-off spikes) | Strong | Developer/tech audience, novel products |
| **Product Hunt** | Medium (prep) | Low | Fast (one-off spike) | Medium | New launches, PLG, product with visual appeal |
| **YouTube** | High | Low–Medium | Slow (3–6 mo) | Medium (if comfortable on camera) | Products that benefit from visual demo, tutorial-driven audience |
| **Email marketing** | Medium | Low | Medium | Medium | Nurture, retention, upselling, complements any primary channel |
| **Partnerships / Co-marketing** | Medium | Low | Medium–Slow | Medium | Complementary products, shared audiences |
| **Affiliate / Referral** | Low (ongoing) | Performance-based | Slow (setup) | Strong (build it) | PLG products, clear value prop, existing happy customers |
| **Podcast (guesting)** | Low–Medium | Low | Medium | Medium | Niche audiences, thought leadership, long-form trust building |
| **Events / Conferences** | High | High | Medium | Low–Medium | Enterprise, relationship-driven sales, brand building |
| **PR / Press** | Medium | Low–High | Unpredictable | Low | Major launches, funding announcements, notable milestones |
| **Programmatic SEO** | High (upfront) | Low | Medium–Slow | Strong | Large keyword surfaces, data-driven pages, template-driven content |

### Channel Selection by Product Type

**API / Developer tool:**
1. Community (Reddit, HN, Discord, dev Slack groups) — your audience lives here
2. Content / SEO (technical blog, documentation-as-marketing) — developers search for solutions
3. Google Ads (if category has search volume) — capture existing intent
4. Twitter/X — developer community is highly active here
5. Partnerships (integrate with tools your audience already uses)

Skip (until later): Meta Ads (developers are ad-blind on social), LinkedIn Ads (too expensive for SMB dev tools), Events (too expensive for early stage).

**SEO / Marketing SaaS:**
1. Content / SEO — practice what you preach; your audience values SEO expertise
2. Google Ads — high-intent keyword searches exist for the category
3. YouTube — tutorials and teardowns perform well with SEO practitioners
4. Community (SEO-focused groups, freelancer communities)
5. Email newsletter — SEO audience subscribes to newsletters heavily

Skip (until later): Meta Ads (unless targeting non-technical SMB owners), Events, PR.

**Enterprise / Sales-led SaaS (high ACV, $10K+/year):**
1. Content / SEO — long-form thought leadership, case studies, whitepapers
2. LinkedIn (organic + ads) — decision-makers live here
3. Email outreach + nurture sequences — direct relationship building
4. Events / conferences — expensive but high-value for enterprise relationships
5. Partnerships — co-sell with adjacent enterprise tools

Skip (until later): Product Hunt (wrong audience), Reddit (enterprise buyers aren't asking Reddit for tool recommendations), Meta Ads (low intent for enterprise).

**PLG / Self-serve SaaS (low ACV, broad market):**
1. SEO / Content — cast a wide net for problem-aware searchers
2. Product Hunt — PLG products get the most value from launches here
3. Google Ads — capture bottom-of-funnel "tool" and "alternative" searches
4. Referral / Viral mechanics — build sharing into the product
5. Social media (Twitter/X, LinkedIn) — build awareness and community

Skip (until later): LinkedIn Ads (CPC too high for low-ACV), Events (cost doesn't justify at low price points).

**Vertical SaaS (specific industry — e.g., dental, real estate, logistics):**
1. Industry-specific communities and forums — these exist for every vertical
2. Google Ads — industry-specific intent keywords are often low competition
3. Partnerships with industry vendors and consultants — they already have your audience's trust
4. Trade events and local meetups — vertical audiences congregate in person
5. Email outreach — industry directories make prospect lists easy to build

Skip (until later): Generic social media, broad content/SEO (your market is narrow — go direct).

See `references/channels-paid.md` and `references/channels-organic.md` for detailed guidance on each channel.

---

## Competitive Context for Channel Selection

Before selecting channels, you need a basic understanding of your competitive landscape. Route to `saas-competitive-research` for full competitive analysis. For channel selection purposes, you need a 30-minute quick scan:

**What to look at (30 minutes):**
1. Google your category and see who shows up in ads and organic results
2. For each competitor: where do they appear? (Paid ads? Organic search? Social? Content? Communities?)
3. What's their primary messaging angle? Where are the gaps?

**Quick scan template:**

| Competitor | Channels active on | Primary message | Gap you can exploit |
|---|---|---|---|
| Competitor A | Google Ads, blog, YouTube | "Most comprehensive" | Too complex for small teams |
| Competitor B | SEO, community, social | "Developer-first" | No self-serve pricing page |
| Competitor C | Paid social, email, events | "Enterprise-grade" | Ignores SMB entirely |

**What this tells you for channel selection:**
- Competitors all bidding on the same keywords → CPC will be high, consider other channels
- No competitors active in a community your audience uses → uncontested opening
- A competitor dominates a channel → easier to win on a channel they're weak on
- No one is doing anything well → basic marketing execution will differentiate you

For deep competitive analysis — competitor profiles, pricing analysis, positioning strategy, battle cards — route to `saas-competitive-research`.

---

## Phasing and Sequencing

The biggest strategic mistake is doing the right thing at the wrong time. Content SEO is a great channel — but not when you have zero customers and haven't validated your messaging. Google Ads can scale fast — but not before you know your activation metric. Everything has a right time.

### Pre-Launch Phase (Weeks, Not Months)

The plan is to launch. Marketing is not the bottleneck — shipping is.

```
Week 1–2: Set up landing page with clear value prop + email capture
Week 2–3: Share in 2–3 communities where audience exists (validate interest)
Week 3–4: Launch. Bare minimum: Product Hunt, Hacker News, relevant communities.
```

Do NOT build a content strategy, email nurture sequence, or ad campaign before launching. You don't know your messaging yet because you don't have customers to learn from.

**What "launch" means at this stage:** Not a polished PR event. A Show HN post. A message in 3 relevant Slack communities. A Reddit post sharing what you built and why. A Product Hunt listing. A tweet thread. All in the same week. The goal isn't to go viral — it's to get 10–50 people using the product so you can learn from them.

### Post-Launch: First 90 Days

```
Month 1 — FIND ONE CHANNEL
  Week 1–2: Pick one channel from the framework above
  Week 3–4: Execute consistently (2–3 activities per week minimum)
  Week 4: Evaluate — any signal at all? (signups, engagement, conversations)

Month 2 — DOUBLE DOWN OR PIVOT
  If signal: increase effort on the channel. Start measuring quality (activation, not just signups)
  If no signal: check messaging first. If messaging is fine, try a different channel.

Month 3 — ADD MEASUREMENT + SECOND CHANNEL
  Set up basic analytics (route to `saas-data-analysis`)
  Add one supporting channel that complements the primary
  Start monthly review cadence
```

**The "signal" threshold:** At this stage, signal doesn't mean "profitable CAC." Signal means: people are responding. They're clicking, signing up, asking questions, giving feedback. If you're getting 5 signups/week from a channel, that's signal — you can optimize from there. Zero signups after 50 Reddit posts is not signal — something is fundamentally off.

**Common month-1 mistakes:**
- Changing channels every week (no channel works in one week)
- Optimizing before you have enough data (premature optimization is the root of wasted time)
- Spending all time on marketing instead of talking to early users (first 10–50 users need conversations, not funnels)

### Growth Phase: Quarterly Planning

Once you have a working channel, planning becomes quarterly cycles:

```
Review (week 1):
  - What's each channel's CAC and conversion quality?
  - What percentage of time/budget goes to each channel?
  - What's working that we should scale? What's not working that we should cut?

Plan (week 2):
  - Set channel-level goals for the quarter
  - Allocate time and budget proportionally to performance
  - Pick ONE experiment for the quarter (new channel, new approach)

Execute (weeks 3–12):
  - Run the plan
  - Monthly check-ins: on track or need adjustment?
```

**When to add a new channel:** Only when your existing channels are either (a) performing well and you want to diversify, or (b) hitting a ceiling where more investment produces diminishing returns. Adding a channel because you're bored with the current one is not a strategy — it's a distraction.

**When to kill a channel:** If a channel has had 3+ months of consistent execution with proper measurement and the unit economics don't work (CAC > LTV, or conversion quality is fundamentally low), cut it. Redirect the time and budget to what works. Killing underperformers is as important as scaling winners.

See `references/planning.md` → Planning Templates for structured planning frameworks.

---

## Budget Allocation

### Zero Budget — Time Is the Currency

At $0, you're spending time instead of money. The same prioritization rules apply — focus beats spread.

| Time budget | Allocation |
|---|---|
| < 5 hrs/week | 100% on one channel |
| 5–10 hrs/week | 70% primary channel, 30% supporting channel |
| 10–20 hrs/week | 50% primary, 30% secondary, 20% experimental |

### With Budget — Start Concentrated, Expand with Data

| Monthly budget | Allocation approach |
|---|---|
| $1,000–3,000 | 100% on one paid channel to validate. Don't split. |
| $3,000–10,000 | 100% on the proven paid channel — scale it, don't diversify yet |
| $10,000+ | Now consider a second paid channel, but only if the first is performing well OR hitting diminishing returns |

**The single-channel rule for paid:** Do not add a second paid channel until your first paid channel is spending $10,000+/month or its performance is clearly slowing (CPA rising, audience saturating, frequency too high). Splitting $3,000 across two paid channels means neither gets enough data to optimize. Concentrate your budget, prove the channel, then expand.

**The testing rule:** Budget at least $1,000 to test a new paid channel — anything less doesn't produce enough data to evaluate. If $1,000 on Google Ads produces zero conversions, the problem isn't budget — it's targeting, messaging, or channel fit. Diagnose before scaling.

**Example — API monitoring product, $2,000/month:**
Put it all on Google Ads targeting "API monitoring tool," "uptime monitoring," "endpoint alerting." Run for 4–6 weeks. If CPA is viable, keep scaling this single channel toward $10K. If not, pause paid entirely — switch to $0 community approach and save the budget until you've fixed messaging or found better keywords.

**Example — SEO keyword research tool, $3,000/month:**
$3,000 on Google Ads (high-intent keywords: "keyword research tool," "find low competition keywords"). Don't split with Meta or content freelancers yet. Prove Google Ads works first. Once you're at $10K/month on Google and performance is stable, then consider allocating budget to a second paid channel or content investment.

---

## Routing to Channel Skills

This skill decides **what** to do. The channel skills explain **how** to do it.

| Decision | Route to |
|---|---|
| Need to understand your audience first | `saas-audience-research` |
| Need competitive analysis or competitor profiles | `saas-competitive-research` |
| Need analytics to measure channels | `saas-data-analysis` |
| Ready to launch a product or feature | `saas-product-launches` |
| Running or planning Google Ads / paid search | `saas-google-ads` |
| Running or planning Meta (Facebook/Instagram) Ads | `saas-meta-ads` |
| Need a content strategy, editorial calendar, or content roadmap | `saas-content-strategy` |
| Need to write, brief, edit, or repurpose content | `saas-content-production` |
| Need website copy, email sequences, ad copy, or any marketing copy | `saas-copywriting` |
| Need to improve or audit organic search / SEO | `saas-seo-audit` |
| Need keyword research or competitive SEO analysis | `saas-seo-research` |
| Need to understand buyer psychology or improve conversion | `saas-customer-psychology` |
| Building or improving a landing page or marketing site | `saas-landing-pages` |
| Improving signup flow, activation, or trial conversion | `saas-onboarding` |
| Channel doesn't have a dedicated skill | See `references/channels-paid.md` or `references/channels-organic.md` |

---

## Reference Files

- `saas-marketing-background/references/background.md` — shared intake questions; read before advising
- `references/channels-organic.md` — organic channel deep dives: content/SEO, programmatic SEO, email, social media, community, Product Hunt, YouTube, partnerships, podcast guesting
- `references/channels-paid.md` — paid channel deep dives: LinkedIn Ads, affiliate/referral programs, events/conferences, PR/press, sponsorships (Google Ads and Meta Ads route to their own skills)
- `references/planning.md` — planning templates (one-page, quarterly, 6-month), funnel projection model with channel-specific conversion ranges and spreadsheet instructions, phasing frameworks, multi-channel coordination, content repurposing, review cadence
- `references/resource-planning.md` — budget allocation frameworks, resource planning (time estimates, hire-vs-DIY, freelancer budgets, first marketing hire). For competitive analysis, route to `saas-competitive-research`.
