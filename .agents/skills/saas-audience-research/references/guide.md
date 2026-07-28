# Audience Research: Complete Reference Guide
 
---
 
## Table of Contents
 
1. [Community Mining — Deep Dive](#community-mining--deep-dive)
2. [Survey Design & Templates](#survey-design--templates)
3. [Influencer Evaluation & Outreach](#influencer-evaluation--outreach)
4. [Media & Publication Mapping](#media--publication-mapping)
5. [Competitive Audience Intelligence](#competitive-audience-intelligence)
6. [Tools & Automation](#tools--automation)
7. [Analysis Frameworks](#analysis-frameworks)
8. [Research Cadence by Stage](#research-cadence-by-stage)
 
---
 
## Community Mining — Deep Dive
 
### Reddit Research Method
 
Reddit is the richest source of unfiltered audience data for most software categories. Users are anonymous, so they're honest. The structure (subreddits, threads, upvotes) gives you natural signal about what resonates.
 
**Step 1: Identify target subreddits**
 
Search Reddit for your problem terms, not your product category. People searching for solutions don't use category language — they describe symptoms.
 
```
API monitoring product:
  Search: "API slow," "endpoint down," "uptime monitoring," "alert fatigue"
  Find: r/devops, r/sre, r/kubernetes, r/sysadmin, r/webdev
 
SEO keyword research tool:
  Search: "keyword research," "find easy keywords," "SEO tool recommendation"
  Find: r/SEO, r/bigseo, r/juststart, r/Entrepreneur, r/SaaS
```
 
**Step 2: Mine the archives**
 
Use Reddit's search within each subreddit. Filter by top posts of the past year. Look for:
- "What tool do you use for...?" threads (competitor intelligence)
- "How do you handle...?" threads (problem language)
- "I built a tool that..." threads (see audience reaction to similar products)
- "Frustrated with..." threads (pain points and switching triggers)
 
**Step 3: Extract and categorize**
 
For each relevant thread, capture:
 
| Data point | Where to find it | What it tells you |
|---|---|---|
| Problem phrasing | Thread title, opening paragraph | Headline and ad copy language |
| Emotional intensity | Upvotes, comment count, frustration language | Severity of the problem |
| Current alternatives | "I currently use..." comments | Competitive landscape from user perspective |
| Desired features | "I wish it could..." comments | Feature roadmap signals |
| Objections | "I tried X but..." comments | Sales objections and onboarding friction |
| Willingness to pay | "I'd pay for..." or "too expensive" comments | Pricing signals |
 
**Step 4: Track over time**
 
Set up recurring searches. What the community talks about shifts — new competitors emerge, sentiment changes, new problems arise. Weekly 30-minute check-ins catch these shifts.
 
### Forum Research Method
 
Product-specific and industry forums (Discourse instances, Stack Overflow, specialized communities) have different dynamics than Reddit. Users are often more experienced, discussions are more technical, and the signal-to-noise ratio is higher for niche topics.
 
**Where to look:**
- Product communities: Grafana forums, Elastic Discuss, Vercel community, Next.js Discord
- Industry forums: Indie Hackers, Hacker News (use Algolia HN search for archives), Stack Overflow
- Slack/Discord communities: search Slofile, Disboard, or community directories for your niche
 
**Extraction method is identical to Reddit.** The same categorization framework applies. The difference is reach — forums are smaller but conversations are deeper and more technical.
 
### Discord & Slack Community Research
 
Closed communities (invite-only Slacks, Discord servers) contain higher-quality signal because the barrier to entry filters out casual noise. The downside: they're harder to search and archive.
 
**Approach:**
1. Join 3–5 relevant communities
2. Lurk for 2 weeks before engaging (understand the norms)
3. Monitor the #general, #help, #tools, and #jobs channels
4. Note recurring questions — these are the real problems
5. Engage authentically (answer questions, share knowledge) before any self-promotion
 
**What to extract:**
- Questions that get asked repeatedly (FAQ = real pain points)
- Tools and workflows people share
- Complaints about existing solutions
- Language patterns specific to this subculture
 
---
 
## Survey Design & Templates
 
### Three Core Surveys for SaaS
 
**1. Post-Signup Survey (day 1–3)**
 
Trigger: email or in-app, 24–72 hours after account creation.
 
```
Question 1: What's the #1 thing you're hoping [product] helps you with?
  Type: Open text
  Why: Captures intent in the user's own words
 
Question 2: How did you hear about us?
  Type: Multiple choice + other
  Options: Google search / Reddit or forum / Friend or colleague / 
           Twitter/X / YouTube / Newsletter / Podcast / Other
  Why: Attribution data; identifies which channels drive signups
 
Question 3: What are you currently using to solve this problem?
  Type: Open text
  Why: Competitive intelligence from actual switchers
```
 
**2. Product-Market Fit Survey (day 14–30)**
 
The Sean Ellis test plus context questions.
 
```
Question 1: How would you feel if you could no longer use [product]?
  Type: Single choice
  Options: Very disappointed / Somewhat disappointed / Not disappointed
  Why: PMF signal — 40%+ "Very disappointed" = strong PMF
 
Question 2 (if "Very disappointed"): What is the main benefit you get from [product]?
  Type: Open text
  Why: Identifies your real value prop from the user's perspective
 
Question 3 (if "Not disappointed"): What would you use instead?
  Type: Open text
  Why: Identifies real competitive alternatives
 
Question 4: What type of person do you think would benefit most from [product]?
  Type: Open text
  Why: Reveals how users see your ICP — often more accurate than your own definition
 
Question 5: How can we improve [product] for you?
  Type: Open text
  Why: Feature prioritization from engaged users
```
 
**3. Churn Survey (triggered on cancellation or inactivity)**
 
```
Question 1: What's the main reason you stopped using [product]?
  Type: Multiple choice + other
  Options: Too expensive / Missing features I need / Too complicated / 
           Found a better alternative / No longer need this type of tool / 
           Other
  Why: Categorize churn reasons at scale
 
Question 2: What would have changed your mind?
  Type: Open text
  Why: Retention opportunities
 
Question 3: What are you switching to? (optional)
  Type: Open text
  Why: Competitive intelligence on churn destinations
```
 
### Survey Distribution & Response Rates
 
| Method | Expected response rate | Best for | Cost |
|---|---|---|---|
| In-app modal (post-action) | 20–40% | Post-signup, PMF | $0 (build it) or $20/mo (Formbricks, Refiner) |
| Email (to active users) | 5–15% | PMF, NPS, feature research | Email tool cost only |
| Email (to churned users) | 2–5% | Churn analysis | Email tool cost only |
| Incentivized email | 10–25% | When you need volume | $5–25 per response |
| Link in app UI | 3–10% | Passive feedback collection | $0 |
 
**Improving response rates:**
- Keep surveys short. 3 questions gets 3x the response rate of 10 questions.
- Personalize the ask: "Hey [name], quick 2-minute survey" beats "Dear user, please complete our feedback form."
- Show progress: "Question 2 of 3" reduces abandonment.
- Close the loop: "Based on your feedback, we built [feature]" encourages future participation.
- Time it right: post-signup day 1–3 for intent; day 14–30 for PMF; within 24 hours for churn.
 
### Survey Analysis
 
**For open-text responses:**
1. Read every response (yes, all of them, until you have 200+)
2. Tag each response with 1–3 theme codes (create codes as you go; expect 8–15 themes)
3. Count frequency of each theme
4. Pull representative quotes for the top 5 themes — these become marketing copy and product priorities
 
**For multiple-choice responses:**
1. Calculate percentages per option
2. Cross-tabulate against user segments if you have them (plan type, company size, role)
3. Look for segments where answers diverge — that's where differentiation opportunities live
 
**Minimum sample sizes for confidence:**
 
| What you're measuring | Minimum responses | Why |
|---|---|---|
| Directional signal ("most people say X") | 30 | Patterns emerge but aren't statistically rigorous |
| PMF test (40% threshold) | 100 | ±10% margin of error at 95% confidence |
| Segment comparison ("Enterprise vs. SMB") | 50 per segment | Enough to compare groups directionally |
| Pricing research | 200+ | Price sensitivity data needs volume |
 
---
 
## Influencer Evaluation & Outreach
 
### Building an Influencer Database
 
Track these fields for each potential influencer:
 
```
Name:
Platform(s):
Follower/subscriber count:
Content focus:
Audience overlap with your ICP (high/medium/low):
Engagement rate:
Content style (review, tutorial, opinion, news):
Has done sponsored content? Y/N:
Audience reaction to sponsored content:
Contact method:
Relationship status (unknown / aware / engaged / partner):
Notes:
```
 
### Evaluating Engagement Quality
 
Follower count is a vanity metric. Engagement quality determines whether an influencer can actually drive action.
 
**Real engagement signals:**
- Comment threads with genuine questions and discussion
- Viewers/readers who reference this creator's opinion when making decisions
- Community members who tag or quote the creator
- Content that gets shared in the target communities you've identified
 
**Fake engagement signals:**
- High follower count, low comments
- Generic comments ("Great post!" "So helpful!" with no specifics)
- Engagement spikes that don't correlate with content quality
- Audience demographics that don't match the content topic
 
### Outreach Approach by Tier
 
**Tier 1 — No budget, just building awareness:**
- Engage genuinely with their content (thoughtful comments, not "great post")
- Share their content with your audience (even if small)
- Mention them in your own content where genuinely relevant
- Build familiarity over 4–8 weeks before making any ask
- Ask: "Would you be open to trying [product] and sharing honest feedback?" (not paid — genuine evaluation)
 
**Tier 2 — Small budget, targeted outreach:**
- Everything from Tier 1, plus:
- Offer free product access (lifetime deal or extended trial)
- Propose content collaboration: guest post, joint webinar, podcast interview
- Provide exclusive data or research they can use in their content
- Small sponsorship of specific content pieces ($200–$2,000 depending on reach)
 
**Tier 3 — Budget for partnerships:**
- Everything from Tiers 1 and 2, plus:
- Ongoing sponsorship arrangements ($1,000–$10,000/month for top-tier niche creators)
- Affiliate partnerships with tracked revenue share
- Co-created content series or product integrations
- Event sponsorships where they're speaking
- Track CAC per influencer — treat as a measured channel
 
**Performance expectations by tier:**
 
| Tier | Expected reach | Conversion expectation | Timeline to results |
|---|---|---|---|
| 1 | 100–1,000 impressions | A few signups; mainly brand awareness | 2–3 months |
| 2 | 1,000–10,000 impressions | Measurable signups, can calculate rough CAC | 1–2 months |
| 3 | 10,000–100,000+ impressions | Trackable revenue, optimizable CAC | 2–4 weeks per campaign |
 
---
 
## Media & Publication Mapping
 
### Building a Media Database
 
For each publication/newsletter/podcast:
 
```
Name:
Type (newsletter / blog / podcast / YouTube / print):
URL:
Audience size (subscribers, traffic, downloads):
Publish frequency:
Content focus:
How they cover products (reviews / sponsored / editorial / guest posts):
Key editorial contacts:
Competitor coverage (what have they written about competitors?):
Submission/pitch process:
Relationship status:
Notes:
```
 
### Finding Publications Your Audience Reads
 
**Method 1 — Ask in interviews (highest quality):**
"What newsletters, blogs, or podcasts do you follow about [topic]?" This is the most reliable signal because it comes from actual target customers.
 
**Method 2 — SparkToro or similar tools:**
Enter a target audience description or domain and see which publications the audience follows, shares, and engages with.
 
**Method 3 — Competitive backlink analysis:**
Use Ahrefs, Moz, or similar to find which publications have linked to competitors. These publications cover your space and have editorial interest in products like yours.
 
**Method 4 — Search and discover:**
- Google: "[topic] newsletter," "[topic] podcast," "best [topic] blogs"
- Newsletter directories: Substack explore, Newsletter Stack
- Podcast directories: search Apple Podcasts, Spotify, Listen Notes
- YouTube: search topic keywords, sort by view count
 
### Outreach Prioritization
 
Rank publications by: (audience match × audience size × accessibility).
 
**Accessibility tiers:**
- High: Accepts guest posts, has a submission form, responds to pitches, covers early-stage products
- Medium: Occasionally covers new products, requires warm intro or strong hook
- Low: Only covers established players, no guest content, requires PR agency or strong relationship
 
**Start with high-accessibility, high-match publications** even if audience size is smaller. A 5,000-subscriber niche newsletter that perfectly matches your ICP will outperform a 500,000-subscriber generalist publication.
 
---
 
## Competitive Audience Intelligence
 
Understanding how competitors serve (and fail to serve) their audience gives you positioning opportunities.
 
### What to Track About Competitor Audiences
 
| Data source | What it reveals | How to access |
|---|---|---|
| G2 / Capterra reviews | What users love and hate; switching reasons; job titles of reviewers | Public; free to read |
| Product Hunt launches | Early adopter reactions, feature requests, enthusiasm level | Public |
| Competitor community/forum | Feature requests, complaints, workarounds | Public or join |
| Competitor blog/content | What topics they think their audience cares about | Public |
| Competitor social media | What content gets engagement; who follows them | Public |
| SimilarWeb / Semrush | Traffic sources, keyword overlap, audience demographics | Freemium tools |
| App store reviews | Mobile-specific feedback; often more emotional/honest | Public |
 
### Competitor Review Mining
 
G2 and Capterra reviews are structured competitive intelligence. The review format (pros, cons, recommendations, use case) gives you pre-categorized data.
 
**What to extract from competitor reviews:**
 
1. **"I switched from X to Y because..."** — switching triggers, directly usable in your marketing
2. **Most-mentioned pros** — table stakes features you must match
3. **Most-mentioned cons** — positioning opportunities: if the #1 complaint about the market leader is complexity, your positioning is simplicity
4. **Reviewer job titles** — actual ICP data for the category
5. **Company sizes** — market segmentation by competitor
6. **"I wish it had..."** — feature gap opportunities
 
**Tiered approach:**
 
| Level | Effort | Method |
|---|---|---|
| Good | 2 hours once | Read 30–50 reviews of top 3 competitors; note patterns manually |
| Better | 4 hours quarterly | Read 100+ reviews; spreadsheet with categorized themes; track over time |
| Best | Automated | Export reviews via API or scraping tool; run sentiment analysis; track quarterly |
 
---
 
## Tools & Automation
 
### Tool Recommendations by Tier and Purpose
 
**Community monitoring:**
 
| Tool | Tier | Cost | What it does |
|---|---|---|---|
| Google Alerts | 1 | Free | Email alerts for keyword mentions across the web |
| Reddit search (manual) | 1 | Free | Manual subreddit-by-subreddit search |
| GummySearch | 2 | $48/mo | Reddit audience research; theme extraction; alerts |
| Syften | 2 | $19/mo | Reddit, HN, and forum monitoring with alerts |
| SparkToro | 2–3 | Free tier + $50/mo | Audience intelligence — who they follow, what they read |
| Brandwatch / Mention | 3 | $100+/mo | Enterprise social listening across all platforms |
 
**Survey tools:**
 
| Tool | Tier | Cost | Best for |
|---|---|---|---|
| Google Forms | 1 | Free | Basic surveys, no frills |
| Tally | 1 | Free tier | Better UX than Google Forms, still free |
| Typeform | 2 | $29/mo | Beautiful surveys, logic branching, higher completion rates |
| SurveyMonkey | 2 | $32/mo | Established, integrations, analysis features |
| Formbricks | 2 | Open source | In-app surveys, self-hosted option |
| Refiner | 2–3 | $79/mo | In-app micro-surveys, segmentation, NPS |
 
**Influencer & media research:**
 
| Tool | Tier | Cost | What it does |
|---|---|---|---|
| Manual search | 1 | Free | YouTube, Twitter, LinkedIn search |
| SparkToro | 2 | Free tier + $50/mo | Audience intelligence — who influences your audience |
| BuzzSumo | 2–3 | $99/mo | Content research, influencer identification by topic |
| Podchaser | 2 | Free tier | Podcast and host discovery |
| Hunter.io | 2 | Free tier | Find email addresses for outreach |
 
**Competitive intelligence:**
 
| Tool | Tier | Cost | What it does |
|---|---|---|---|
| G2 / Capterra | 1 | Free to read | Competitor reviews, categorized |
| SimilarWeb | 1–2 | Free tier | Traffic estimates, audience overlap |
| BuiltWith | 1 | Free tier | Technology detection on competitor sites |
| Semrush / Ahrefs | 2–3 | $99–130/mo | Keyword overlap, backlink analysis, content gaps |
 
### Automation Playbook
 
**What to automate (and when):**
 
| Automation | When to add | How |
|---|---|---|
| Weekly community keyword alerts | Tier 1+ | Google Alerts or Syften — 15 min setup |
| Post-signup survey trigger | Tier 2+ | Email automation (Loops, Customer.io) or in-app (Formbricks) |
| Churn survey trigger | Tier 2+ | Trigger on cancellation event |
| Competitor review alerts | Tier 2+ | G2 RSS feeds or manual quarterly check |
| Influencer mention tracking | Tier 3 | SparkToro alerts or social listening tool |
| Monthly research summary | Tier 3 | Notion or spreadsheet template, assigned to a person |
 
---
 
## Analysis Frameworks
 
### Jobs to Be Done (JTBD) Framework
 
JTBD is a way to organize research findings around the outcomes customers are trying to achieve, not the features they're requesting.
 
**The core question:** "When [situation], I want to [motivation], so I can [expected outcome]."
 
**How to extract JTBD from interviews:**
 
Listen for:
- "I was trying to..." (the job)
- "I was frustrated because..." (the struggling moment)
- "I started looking for..." (the switching trigger)
- "I chose [product] because..." (the hiring criteria)
- "I stopped using [product] because..." (the firing criteria)
 
**Example — API monitoring product JTBD:**
"When my API goes down at 3am, I want to get alerted immediately with context on what broke, so I can fix it before customers notice."
 
**Example — SEO keyword research tool JTBD:**
"When I take on a new client, I want to quickly find keywords they can realistically rank for, so I can show results in the first 90 days and keep the contract."
 
### Audience Segmentation Methods
 
After collecting data across all research channels, segment your audience by:
 
**Behavioral segmentation (most useful for SaaS):**
- How they discovered you (channel)
- What they do first in the product (intent signal)
- How frequently they use the product (engagement)
- Which features they use (use case)
- Whether they upgrade, stay, or churn (value fit)
 
**Needs-based segmentation:**
- Primary job to be done
- Severity of the problem (nice-to-have vs. hair-on-fire)
- Budget and willingness to pay
- Technical sophistication
- Decision-making authority (end user vs. buyer vs. both)
 
**Demographic segmentation (least useful, but still relevant):**
- Company size
- Industry
- Job title/role
- Geography
 
**Best approach: start with needs-based, then validate with behavioral data.** Demographics are useful for targeting ads and filtering lists, but they don't explain why people buy.
 
### Research Synthesis Template
 
After completing a research cycle, synthesize into this format:
 
```
## Research Synthesis — [Date]
 
### Key Findings
1. [Finding]: Supported by [evidence from X source]
2. [Finding]: Supported by [evidence from Y source]
3. [Finding]: Contradicted by [evidence from Z source] — needs further investigation
 
### Audience Segments Identified
- Segment A: [description, size estimate, primary need]
- Segment B: [description, size estimate, primary need]
 
### Language Bank (exact phrases from research)
- Problem language: "[phrase 1]", "[phrase 2]", "[phrase 3]"
- Solution language: "[phrase 1]", "[phrase 2]"
- Objection language: "[phrase 1]", "[phrase 2]"
 
### Channel Map
- Community: [top 3 communities by relevance]
- Influencers: [top 5 by ICP match]
- Media: [top 5 publications by audience overlap]
 
### Recommended Actions
1. [Action]: Because [finding] — expected impact: [low/medium/high]
2. [Action]: Because [finding] — expected impact: [low/medium/high]
 
### Open Questions (next research cycle)
1. [Question]: Why it matters — [decision it would unblock]
```
 
---
 
## Research Cadence by Stage
 
### Pre-Launch (weeks, not months)
 
| Week | Activity | Output |
|---|---|---|
| 1 | Identify communities, start mining | 50+ posts read, problem language list |
| 2 | Continue mining, start interviews (5) | Interview notes, pattern list |
| 3 | Complete interviews, synthesize | Minimum ICP, positioning hypothesis |
| 4 | Validate positioning against community language | Launch-ready messaging |
 
### Post-Launch, Pre-PMF (monthly cycles)
 
| Week | Activity | Output |
|---|---|---|
| 1 | 3–5 customer interviews | Updated patterns, new quotes |
| 2 | Community monitoring + survey analysis | Quantified themes, channel performance |
| 3 | Competitive review check + influencer outreach | Updated competitive landscape |
| 4 | Synthesis + action planning | Updated ICP, next month's priorities |
 
### Growth Stage (quarterly deep dives + continuous monitoring)
 
| Cadence | Activity |
|---|---|
| Weekly | Community monitoring (1–2 hrs), survey response review |
| Monthly | 3–5 customer interviews, influencer engagement, metric review |
| Quarterly | Full research synthesis, segmented survey, competitive deep-dive, ICP refinement |
| Annually | Full media landscape review, influencer audit, research program evaluation |
 
---
 
## Quick-Reference: Research Method Selection
 
When unsure which method to use, consult this decision tree:
 
```
"I don't know who my customer is"
  → Community mining (1 week) + 5 problem interviews
 
"I know who they are but not what they want"
  → 10 customer interviews + post-signup survey
 
"I know what they want but can't reach them"
  → Influencer mapping + media mapping + community identification
 
"I'm reaching them but they don't convert"
  → Churn interviews + objection-focused interviews + competitive review mining
 
"I need to expand into a new segment"
  → Community mining in new segment + 5–10 interviews in new segment
 
"My messaging isn't landing"
  → Community language extraction + interview language analysis + A/B test with new language
 
"I want to understand my competitors' audience"
  → Competitor review mining + competitive content analysis + SimilarWeb/SparkToro
```
