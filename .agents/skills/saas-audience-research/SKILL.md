---
name: saas-audience-research
description: >
  Comprehensive audience research guide for developers and technical founders building web-first software products — SaaS, developer tools/APIs, and enterprise software. Use this skill for any question about understanding customers, audience research, customer interviews, user surveys, community research, Reddit research, forum mining, identifying influencers, media landscape mapping, ICP definition, persona building, voice-of-customer data, Jobs to Be Done, competitive audience analysis, or figuring out who to build for and how to reach them. Trigger whenever a user asks about understanding their target market, finding where their audience hangs out, learning what customers want, conducting user research, analyzing communities, or any pre-marketing research for a software product — even if they just say "I don't know who my customer is" or "how do I figure out my market."
---
 
# Audience Research for Software Products
 
Audience: developers and technical founders. Explain things in engineering terms. Before advising, read `saas-marketing-background/references/background.md` and gather missing background. Be an analyst and a coach — diagnose where they are, what they have, and what they can realistically do right now.
 
---
 
## Table of Contents
 
1. [Why This Matters](#why-audience-research-matters)
2. [Situation Assessment](#situation-assessment)
3. [Three Tiers of Research](#three-tiers-of-research)
4. [First-Party Research](#first-party-research-your-own-data)
5. [Third-Party Research](#third-party-research-the-outside-world)
6. [Synthesizing Research into Action](#synthesizing-research-into-action)
7. [Research by Product Stage](#research-by-product-stage)
8. [Reference Files](#reference-files)
 
---
 
## Why Audience Research Matters
 
Most technical founders skip audience research or treat it as a checkbox. They build what they think is needed, then try to find customers afterward. This inverts the process. Audience research is not a marketing exercise — it's a product-risk reduction mechanism.
 
What audience research actually produces:
- **Language**: the exact words your customers use to describe their problem, which becomes your ad copy, landing page headlines, and SEO keywords
- **Channels**: where they already spend attention, which determines where your marketing dollars go
- **Objections**: what stops them from buying, which shapes your pricing page and sales process
- **Priorities**: what they care about most, which determines your feature roadmap and positioning
 
You don't need all of this at once. You need the right slice at the right time.
 
**Example — API monitoring product:**
A founder assumes devops engineers want "comprehensive observability." Research reveals they actually search for "why is my API slow" and "endpoint latency alerts." The product is the same. The positioning changes completely.
 
**Example — SEO keyword research tool:**
A founder positions against enterprise competitors. Research in SEO communities reveals most buyers are freelancers and small agency owners searching "find low competition keywords" and "keyword difficulty checker." The ICP shifts from enterprise to SMB.
 
---
 
## Situation Assessment
 
Before recommending any research approach, assess the founder's actual situation. Don't prescribe a sophisticated research program to someone who launched last week and has zero customers. Don't tell someone with 500 customers to "go talk to people on Reddit."
 
### Questions to Evaluate
 
**Experience with research:**
- Have you done any customer research before? (interviews, surveys, community lurking)
- Do you have any existing customer data? (emails, usage data, support tickets, NPS scores)
- Do you have access to customers who will talk to you?
 
**Resources available:**
- Time: How many hours/week can you dedicate to research? (Be honest — 2 hours is fine)
- Budget: Any budget for tools or incentives? ($0 is fine at Tier 1)
- Team: Just you, or do you have someone who can help run interviews/surveys?
 
**Product stage:**
- Pre-launch with an idea
- Pre-launch with a prototype/beta
- Launched with < 50 customers
- Launched with 50–500 customers
- Launched with 500+ customers
 
**Urgency:**
- Are you pre-launch and need to validate before building?
- Are you launched and trying to figure out why growth is flat?
- Are you profitable and trying to expand into new segments?
 
### Stage-Based Routing
 
| Stage | Primary research | Secondary research | Skip for now |
|---|---|---|---|
| Pre-launch, idea only | Community mining, competitor audience analysis | 5–10 problem interviews | Surveys, influencer mapping |
| Pre-launch, prototype | Problem interviews (5–10), community validation | Competitor audience, early Reddit/forum posts | Large-scale surveys, media mapping |
| Launched, < 50 customers | Customer interviews (all of them), support ticket analysis | Community research, basic influencer ID | Formal surveys, media landscape |
| Launched, 50–500 | Structured interviews (15–20), targeted surveys | Community monitoring, influencer + media mapping | Nothing — you need all channels |
| Launched, 500+ | Segmented surveys, data-driven persona refinement | Influencer partnerships, media relationships | Basic community lurking (automate it) |
 
The table above is a priority guide, not a gate. If you're pre-launch and you happen to know a journalist who covers your space, talk to them. The point is: don't build a research program you can't sustain. Do the highest-leverage activity for your stage first.
 
---
 
## Three Tiers of Research
 
These tiers are cumulative. Tier 2 includes Tier 1. Tier 3 includes both. Start where you are, not where you wish you were.
 
### Tier 1 — Scrappy (Pre-launch or early, $0 budget, 2–5 hrs/week)
 
You have no customers or very few. You're trying to validate that the problem exists and learn how people describe it.
 
**What you do:**
- Lurk in 3–5 relevant communities (subreddits, forums, Discord servers, Slack groups)
- Read 50–100 posts/comments about the problem you're solving — screenshot or copy the exact language
- Do 5–10 informal conversations (DMs, coffee chats, founder networks) about the problem (not your solution)
- Search Twitter/X, LinkedIn, and YouTube for people talking about the problem publicly
- Read competitor reviews (G2, Capterra, Product Hunt, app stores) for language and complaints
 
**What you get:**
- A rough vocabulary list of how people describe the problem
- 3–5 communities where your audience congregates
- An initial sense of whether the problem is real and how painful it is
- Competitor weaknesses in the audience's own words
 
**What you don't get (and that's fine for now):**
- Statistical confidence in anything
- Detailed segmentation
- Influencer relationships
- Formal personas
 
**Performance note:** Tier 1 research gives you directionally correct information. It's biased toward vocal community members, which skews toward power users and the technically sophisticated. It misses the silent majority who have the problem but don't post about it. This is OK for early validation — but don't mistake community sentiment for market sentiment.
 
**Example — API monitoring product at Tier 1:**
Lurk in r/devops, r/sre, Hacker News "Ask HN" threads, and the Grafana community forum. Search for "API monitoring," "endpoint alerts," "uptime monitoring." Collect 50+ posts. Note recurring phrases: "I just want to know when my API is slow," "Datadog is overkill for what I need," "PagerDuty alert fatigue." These become your first landing page headlines and ad copy hypotheses.
 
**Example — SEO keyword research tool at Tier 1:**
Lurk in r/SEO, r/bigseo, SEO-focused Facebook groups, and the Ahrefs community forum. Search for "keyword research tool," "keyword difficulty," "find easy keywords." Note: "I'm a freelancer and can't afford Ahrefs," "Semrush is confusing," "I just need keyword difficulty and search volume." First positioning hypothesis: affordable simplicity.
 
---
 
### Tier 2 — Structured (Launched, some customers, small budget, 5–10 hrs/week)
 
You have customers. You can talk to them. You should.
 
**What you add to Tier 1:**
- 10–20 structured customer interviews using a consistent script (see `references/interview-guide.md`)
- Post-onboarding and post-churn micro-surveys (3–5 questions max)
- Support ticket and feature request categorization
- Systematic community monitoring (set up alerts, track threads weekly)
- Identify 10–20 influencers and content creators in your space
- Map 5–10 publications/newsletters/podcasts your audience reads
 
**What you get:**
- Validated problem language from actual paying customers
- Churn reasons and activation blockers — directly from the source
- A repeatable interview process you can run monthly
- A media and influencer landscape you can act on
- Early segmentation: who are your best customers vs. average ones?
 
**What you don't get:**
- Statistically significant survey data (need more volume)
- Predictive persona models
- Automated research pipelines
 
**Performance note:** Tier 2 gives you high-confidence qualitative data. Ten good interviews surface 80% of the insights you'd find in fifty. But you still don't have quantitative validation — "7 out of 10 interviewees said X" is directional, not statistically valid. That's fine. You're making better decisions than guessing, which is the bar.
 
---
 
### Tier 3 — Systematic (Growth stage, budget available, 10+ hrs/week or dedicated person)
 
You have enough customers to do real analysis. Research becomes an ongoing program, not a one-time project.
 
**What you add to Tier 2:**
- Quarterly segmented surveys with 100+ responses
- Cohort analysis: what do your best customers have in common vs. churned customers?
- Automated community monitoring with alerting
- Influencer relationship development (not just identification)
- Media relationship building (pitching, guest posts, podcast appearances)
- Jobs to Be Done research framework
- Competitive audience intelligence (track competitor community engagement, review sentiment, content performance)
 
**What you get:**
- Quantitatively validated personas and segments
- A predictive model for who your best customers will be
- An owned distribution channel through influencer and media relationships
- A continuous feedback loop between research and product/marketing decisions
 
**Performance note:** Tier 3 is the full research program. Most software companies under $5M ARR don't need all of this — they need the right parts of it. Don't build the full program because it seems professional. Build the parts that answer the questions blocking your growth right now.
 
---
 
## First-Party Research: Your Own Data
 
First-party research means data you collect directly from your customers, users, and prospects. It's the highest-quality audience data you can get because it's specific to your product and situation.
 
### Customer Interviews
 
The most underused and highest-ROI research method for software founders. Five good interviews will teach you more than a month of analytics dashboards.
 
**When to interview:**
- You have at least 1 customer (or prospect who evaluated you)
- You're trying to understand why people buy, churn, or don't activate
- You're entering a new segment or market
- Your messaging isn't landing and you don't know why
 
**Who to interview (in priority order):**
 
| Segment | Why | Minimum |
|---|---|---|
| Recent buyers (< 30 days) | Purchase decision is fresh | 5 |
| Power users | Understand your best-case customer | 3–5 |
| Churned users | Understand failure modes | 3–5 |
| Prospects who evaluated but didn't buy | Understand objections | 3–5 |
| Users in a new target segment | Validate expansion hypothesis | 5 |
 
**How many interviews:**
- 5 interviews: enough to spot obvious patterns. Good enough for Tier 1.
- 10–15: patterns stabilize. Diminishing returns start here for most questions.
- 20+: needed only for segmentation or when early interviews are contradictory.
 
If you're hearing the same things by interview 8, you have enough signal. Move to action.
 
**Getting people to say yes:**
- Email subject: "Quick question about your experience with [product]" (not "Can I interview you?")
- Offer: 15–20 minutes of their time, $25 gift card or account credit, or early access to a feature
- Scheduling: send a Calendly link. Reduce friction to zero.
- For churned users: "We're trying to improve — your honest feedback helps" (genuine, not manipulative)
 
**Conducting the interview:**
 
Follow the detailed scripts in `references/interview-guide.md`. Core principles:
 
1. Ask about their behavior, not their preferences. "Tell me about the last time you dealt with [problem]" — not "Would you use a tool that does X?"
2. Shut up after asking. Let silence do the work. Most founders fill pauses with leading questions.
3. Follow the energy. When they get animated or frustrated, that's the signal. Go deeper there.
4. Record (with permission) and take notes. You'll forget the nuance otherwise.
5. Never pitch during an interview. The moment you start selling, the honest feedback stops.
 
**What to extract from every interview:**
- The exact words they use to describe the problem
- What they were doing before they found you (or what they're doing instead)
- What almost stopped them from signing up / buying
- What triggered the search for a solution (the "switching trigger")
- Who else they considered and why
 
See `references/interview-guide.md` for complete interview scripts, question banks, and analysis templates.
 
### Surveys
 
Surveys are for validation at scale, not discovery. Don't survey until you've done at least 5–10 interviews — you won't know the right questions to ask.
 
**When to survey:**
- You have interview hypotheses you want to quantify ("70% of interviewees said X — is that true at scale?")
- You have 200+ users/customers (below this, response volume is too low for meaningful data)
- You want to segment your audience by need, behavior, or willingness to pay
 
**When NOT to survey:**
- You have fewer than 50 customers (interview them instead — all of them)
- You don't have a specific hypothesis to test
- You're trying to discover problems (use interviews for discovery)
 
**Survey design — tiered by what you can pull off:**
 
| Level | Tool | Questions | Response target | Cost |
|---|---|---|---|---|
| Good | Google Forms / Typeform free | 3–5 questions | 30+ responses | $0 |
| Better | Typeform / SurveyMonkey paid | 5–10 questions, logic branching | 100+ responses | $30–100/mo |
| Best | Typeform + incentive + segmentation | 10–15 questions, multi-path | 200+ responses | $200–500/mo |
 
**Survey placement by response rate (highest to lowest):**
1. In-app prompt after key action (20–40% response rate)
2. Post-onboarding email, day 3–7 (10–20%)
3. Email to active users (5–15%)
4. Email to churned users (2–5%)
 
**Three surveys every SaaS should run:**
 
1. **Post-signup (day 1–3):** "What's the #1 thing you're hoping [product] helps you with?" (open text, one question)
2. **Post-activation or day 14:** Sean Ellis test — "How would you feel if you could no longer use [product]?" (Very disappointed / Somewhat disappointed / Not disappointed). If 40%+ say "very disappointed," you have product-market fit signal.
3. **Post-churn:** "What's the main reason you stopped using [product]?" (multiple choice + open text)
 
See `references/guide.md` for detailed survey templates and analysis methods.
 
---
 
## Third-Party Research: The Outside World
 
Third-party research means studying your audience where they already are — communities, influencers they follow, and media they consume. This data is less specific than first-party but covers your total addressable market, not just existing customers.
 
### Community Research (Reddit, Forums, Discord, Slack)
 
Communities are where your audience talks honestly. They're not performing for followers or colleagues. They're asking genuine questions and sharing real frustrations. This makes community data the closest thing to unfiltered voice-of-customer you can get without doing interviews.
 
**Finding the right communities:**
 
| Source | How to find | What to look for |
|---|---|---|
| Reddit | Search your problem terms, check related subreddits sidebar | Subreddits with 10K–500K members, active daily posts, question threads |
| Forums | Google "[topic] forum," check product-specific forums | Active threads in the last 30 days, question-answer patterns |
| Discord | Disboard.org, search product/topic names | Servers with 1K+ members, active general/help channels |
| Slack | slofile.com, community lists, product Slack groups | Active workspaces, channels with recent messages |
| Facebook Groups | Search groups by topic | Groups with 5K+ members, active moderation, daily posts |
 
**What to collect from communities — the research extraction framework:**
 
For each community, track:
1. **Problem language:** How do they describe the pain? Copy exact phrases.
2. **Solution language:** How do they describe what they want? ("I wish there was a tool that...")
3. **Current alternatives:** What are they using now? What do they like/hate about it?
4. **Buying triggers:** What makes them start looking for a solution?
5. **Objections:** What stops them from trying new tools?
6. **Power users vs. newbies:** What's the skill distribution? This affects your onboarding.
 
**Tiered approach:**
 
| Level | Effort | Method | Output |
|---|---|---|---|
| Good | 2 hrs/week | Manual browsing, screenshot interesting posts | Unstructured notes, a feel for the landscape |
| Better | 4 hrs/week | Systematic weekly review, spreadsheet tracking, keyword alerts (Google Alerts, Reddit search) | Categorized themes, tracked over time |
| Best | 1 hr/week + tools | GummySearch, SparkToro, Syften, or custom Reddit API scripts for automated monitoring | Automated trend tracking, sentiment shifts, competitive mentions |
 
**Performance difference:** "Good" gives you 60–70% of the insight at 30% of the effort. You miss trends over time and subtle shifts, but you catch the big patterns. This is fine for Tier 1 and early Tier 2.
 
**Example — API monitoring product, community research:**
In r/devops, the top complaints about existing monitoring: "too many dashboards," "alert fatigue is killing us," "I spend more time configuring Prometheus than using it." Competitor sentiment: "Datadog pricing is insane once you scale," "New Relic's UI got worse." Opportunity signal: simplicity + predictable pricing.
 
**Example — SEO keyword research tool, community research:**
In r/SEO, recurring threads: "What's the best free keyword tool?", "Ahrefs vs Semrush for a small agency?", "How accurate is keyword difficulty?" Key insight: the audience segments by budget — freelancers want free/cheap, agencies want accuracy, enterprises want integrations. Each segment uses different language.
 
### Influencer Identification
 
"Influencer" in software means anyone whose opinion your target audience trusts and seeks out. This includes: YouTubers, newsletter authors, podcast hosts, Twitter/X personalities, open-source maintainers, conference speakers, bloggers, and community moderators.
 
**Why this matters:** Influencers are distribution shortcuts. One mention from a trusted voice in your niche can generate more qualified traffic than months of SEO or thousands of dollars in paid ads. But only if it's the right influencer for your audience.
 
**Finding influencers — tiered:**
 
| Level | Method | Output |
|---|---|---|
| Good | Search YouTube, Twitter, LinkedIn for your topic keywords. Note who creates content your audience engages with. | List of 10–20 names, rough sense of reach |
| Better | Use SparkToro (freemium) to find who your audience follows. Cross-reference with community mentions. Check podcast directories for niche shows. | Prioritized list of 20–50 influencers with reach estimates and content style |
| Best | SparkToro + manual relationship mapping + engagement analysis. Track who drives actual signups (UTM-tagged links, referral codes). | ROI-ranked influencer database with relationship status and conversion data |
 
**Evaluating influencer fit:**
 
| Factor | What to check | Red flag |
|---|---|---|
| Audience match | Do their followers match your ICP? | Large following but wrong audience (e.g., beginner tutorials when you sell enterprise tools) |
| Engagement quality | Comments showing real questions and discussion? | High follower count, low engagement, or bot-like comments |
| Content alignment | Do they cover adjacent topics credibly? | They cover everything superficially |
| Commercial history | Have they done sponsorships? How did the audience react? | Audience backlash on sponsored content |
| Reach vs. relevance | A 5K-follower niche expert may outperform a 500K generalist | Pure reach without relevance — vanity metric |
 
**Example — API monitoring product:**
Target influencers: DevOps YouTubers (Techno Tim, NetworkChuck for broader reach; smaller SRE-focused channels for precision), SRE newsletter authors, Kubernetes community maintainers, hosts of podcasts like "Software Engineering Daily" or "The Changelog."
 
**Example — SEO keyword research tool:**
Target influencers: SEO YouTubers (Matt Diggity, Income School, Ahrefs' own channel — study what works), newsletter authors (Detailed.com, Search Engine Roundtable), Twitter SEO community (check who gets engagement on SEO threads).
 
### Media & Publication Mapping
 
"Media" means any publication, newsletter, podcast, or content platform your audience consumes regularly. This shapes both your content strategy and your PR/outreach.
 
**Mapping the landscape — tiered:**
 
| Level | Method | Output |
|---|---|---|
| Good | Ask in interviews: "What do you read/listen to about [topic]?" Google "[topic] newsletter," "[topic] podcast." | 5–10 publications and podcasts your audience mentions |
| Better | SparkToro audience intelligence, cross-reference interview data, check Similarweb for competitor referral sources | 15–30 ranked publications with audience size estimates |
| Best | Full media database with editorial contacts, content calendars, pitch history, and tracked referral traffic | Ongoing media relationship program |
 
**What to track for each publication:**
 
- Name and URL
- Audience size (subscribers, traffic, downloads)
- Content format (articles, reviews, tutorials, news, opinion)
- How they cover products like yours (reviews? sponsored content? earned editorial?)
- Key editorial contacts
- How competitors appear there (ads? guest posts? reviews?)
 
---
 
## Synthesizing Research into Action
 
Research without action is a procrastination tool. Every research activity should answer a specific question that unblocks a specific decision.
 
### The Research → Action Map
 
| Research type | Answers this question | Feeds this decision |
|---|---|---|
| Customer interviews | Why do people buy, churn, or not activate? | Positioning, onboarding, pricing |
| Surveys | How common are the patterns we found in interviews? | Prioritization, segmentation |
| Community mining | What language does the market use? Where do they congregate? | Ad copy, SEO keywords, channel selection |
| Influencer mapping | Who does the audience trust? | Partnership and outreach strategy |
| Media mapping | Where does the audience consume content? | Content strategy, PR, distribution |
 
### Building an ICP from Research
 
After completing research at any tier, synthesize into an ICP (Ideal Customer Profile). The ICP is not a persona — it's a decision-making filter.
 
**Minimum viable ICP (Tier 1):**
```
Who: [role/title] at [company type/size]
Problem: [in their words, from research]
Current solution: [what they use today]
Buying trigger: [what makes them start looking]
Where they hang out: [top 3 communities/channels]
```
 
**Example — API monitoring product, minimum ICP:**
```
Who: Backend developer or SRE at 10–100 person startup
Problem: "I need to know when my API is slow before customers notice"
Current solution: Homegrown Prometheus + Grafana, or overpriced Datadog
Buying trigger: Customer complaint about downtime or latency
Where they hang out: r/devops, Hacker News, SRE Slack communities
```
 
**Example — SEO keyword research tool, minimum ICP:**
```
Who: Freelance SEO consultant or small agency owner (1–5 person team)
Problem: "I need to find low-competition keywords without paying $99/mo"
Current solution: Free tier of Ubersuggest, manual Google searches, spreadsheets
Buying trigger: Taking on a new client and needing keyword data
Where they hang out: r/SEO, Facebook SEO groups, SEO YouTube channels
```
 
**Expanded ICP (Tier 2+):** Add to the minimum: objections to buying, willingness to pay data, activation milestones, best-fit indicators (company size, tech stack, use case), and anti-personas (who looks like a customer but isn't).
 
### Prioritizing What to Research Next
 
Always ask: "What decision am I trying to make, and what information would change that decision?"
 
If the answer is "I don't know who my customer is" — do community research + 5 interviews.
If the answer is "I know who they are but can't reach them" — do influencer + media mapping.
If the answer is "I'm reaching them but they don't convert" — do interview deep-dives on objections and switching triggers.
If the answer is "I need to expand to a new segment" — do community research + interviews in the new segment.
 
Don't research everything. Research the bottleneck.
 
---
 
## Research by Product Stage
 
### Pre-Launch: Speed Matters Most
 
If you haven't launched, the #1 priority is getting to launch with enough conviction that you're building something people want. Research serves launch — it doesn't delay it.
 
**Pre-launch research budget: 2–4 weeks, not 2–4 months.**
 
Week 1–2: Community mining (identify 3–5 communities, read 100+ posts, extract problem language and current alternatives).
Week 2–3: 5–10 problem interviews (not solution interviews — you're validating the problem, not pitching your product).
Week 3–4: Synthesize into minimum ICP + initial positioning hypothesis. Launch.
 
Everything else — surveys, influencer outreach, media mapping — happens after you have real users giving you real data. Don't perfect your understanding of the market before entering it. Enter it with a directionally correct hypothesis and refine with first-party data.
 
**What "good enough to launch" looks like:**
- You can describe the problem in 1 sentence using the audience's language
- You know 3+ places where the audience congregates online
- At least 3 people (not friends/family) have confirmed the problem is real and they'd try a solution
- You have a landing page that speaks to the problem in the audience's words
 
### Post-Launch: Shift to First-Party
 
Once you have users, first-party research becomes primary. Community research shifts from "discovery" to "monitoring."
 
The post-launch research loop:
```
Interview customers → Identify patterns → Validate with survey → Adjust positioning/product → Repeat quarterly
```
 
Monitor communities weekly for: new competitor mentions, shifting sentiment, emerging problems, and language changes. This takes 1–2 hours/week and compounds over time.
 
---
 
## Reference Files
 
- `saas-marketing-background/references/background.md` — shared intake questions; read before advising (shared across Google Ads, Meta Ads, and Audience Research skills)
- `references/guide.md` — complete reference: community mining techniques, survey templates, influencer evaluation, media outreach, tools and automation, analysis frameworks
- `references/interview-guide.md` — customer interview scripts, question banks, analysis templates, and frameworks for different interview types (problem discovery, churn investigation, segment exploration)
 
**Source:** `references/interview-guide.md` incorporates frameworks from the Obsaased Easy Insights Toolkit (planning, candidate selection, bias avoidance, data processing) alongside software-founder-specific interview scripts and question banks.
