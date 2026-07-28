# Paid Marketing Channels for SaaS

Detailed guidance for paid channels beyond Google Search Ads and Meta Ads. For those, route to `google-ads-for-saas` and `meta-ads-for-saas` respectively.

---

## Table of Contents

1. [Google Ads & Meta Ads — Quick Pointers](#google-ads--meta-ads--quick-pointers)
2. [LinkedIn Ads](#linkedin-ads)
3. [Affiliate & Referral Programs](#affiliate--referral-programs)
4. [Events & Conferences](#events--conferences)
5. [PR & Press](#pr--press)
6. [Sponsorships](#sponsorships)

---

## Google Ads & Meta Ads — Quick Pointers

These channels have dedicated skills with full implementation guides, creative specs, bidding strategies, and optimization playbooks.

**Google Search Ads** → `google-ads-for-saas`
Best when: your category has search volume, users search for solutions, you have budget for CPC of $2–$30+. Captures demand that already exists.

**Meta Ads (Facebook + Instagram)** → `meta-ads-for-saas`
Best when: broader audience, visual product, you have creative assets, and you can afford the learning phase. Creates demand by interrupting people who weren't looking.

Don't start either without conversion tracking in place. Route to `saas-data-analysis` if tracking isn't set up.

---

## LinkedIn Ads

### When LinkedIn Ads Make Sense

LinkedIn Ads are expensive — CPCs of $5–$15 are common, and CPMs regularly exceed $50. This channel only makes economic sense when your average contract value is high enough to absorb the acquisition cost.

**Good fit:**
- Enterprise or mid-market SaaS ($5,000+/year ACV)
- Products sold to specific professional roles (VP Marketing, CTO, HR Director)
- Account-based marketing (targeting specific companies)
- Products where the buyer is not the user (e.g., selling to managers who'll deploy to their team)

**Bad fit:**
- Self-serve PLG products with < $50/month price points (CAC will exceed LTV)
- Developer tools (developers are less active on LinkedIn than Twitter/HN/Reddit)
- Consumer-adjacent software
- Any product without enough budget to sustain $30–100/day per campaign

### Campaign Types

**Sponsored Content (feed ads):** Single image, carousel, or video in the LinkedIn feed. Best for awareness and lead generation. Use for promoting content (guides, reports, case studies) with a lead capture form.

**Message Ads (InMail):** Direct messages to targeted professionals. Intrusive but high open rates (30–50%). Use sparingly and only with a genuinely relevant offer. A cold InMail pitching your product to someone who's never heard of you feels like spam. An InMail inviting a VP of Engineering to a relevant webinar feels like a professional courtesy.

**Lead Gen Forms:** Native LinkedIn forms that pre-fill from the user's profile. Higher conversion rates than sending to a landing page because there's less friction. Downside: lead quality can be lower (easy to submit = less intent).

**Text Ads:** Small sidebar ads. Cheap but low engagement. Useful for retargeting and brand awareness at low cost.

### Targeting

LinkedIn's targeting is its biggest strength. You can target by:
- Job title, job function, seniority level
- Company name, company size, industry
- Skills listed on profiles
- Groups they belong to
- Education (degree, school, field of study)

**Tiered approach:**

| Level | Targeting method | Audience size |
|---|---|---|
| Good | Job titles + company size + industry. Keep audience 20K–100K. | Broad enough for data, narrow enough for relevance |
| Better | Above + exclude current customers (upload email list). Layer seniority filters. | Tighter targeting, less waste |
| Best | Account-based: upload target company list + layer job titles. Use LinkedIn's Matched Audiences for retargeting website visitors. | Precision targeting, highest cost but best conversion |

### Budget and Expectations

**Minimum viable test:** $1,500–3,000 over 4 weeks. Below this, you won't gather enough data to evaluate the channel.

**Expected metrics for B2B SaaS:**

| Metric | Typical range |
|---|---|
| CPC (Sponsored Content) | $5–$15 |
| CTR | 0.3–0.8% |
| Cost per lead (Lead Gen Form) | $30–$150 |
| Cost per demo/MQL | $100–$500 |

**The honest assessment:** LinkedIn Ads are a Tier 2–3 channel for most SaaS companies. The targeting is unmatched for B2B, but the cost means you need either high ACV or strong funnel efficiency to make the math work. Test only after you have a proven funnel and know your LTV.

---

## Affiliate & Referral Programs

### Referral Programs (Customer-to-Customer)

A referral program incentivizes existing customers to bring in new ones. This only works when you have customers who love the product — don't launch a referral program for a product people tolerate.

**Prerequisites:**
- 50+ active users minimum
- Product-market fit signal (40%+ "very disappointed" on Sean Ellis question, or strong NPS)
- A product that benefits from multiple people using it (team tools, collaboration, network effects)

**Tiered approach:**

| Level | Implementation | Expected impact |
|---|---|---|
| Good | Add "Invite a colleague" button to the UI. No reward — just make it easy. Track how many invites are sent and accepted. | 2–5% of users will invite someone organically |
| Better | Double-sided incentive: referrer gets account credit or free month, referred gets extended trial or discount. Email prompt after activation. | 5–15% of activated users will refer |
| Best | Viral mechanics built into the product (shareable reports, public dashboards, team invites as a core feature). Tiered rewards for power referrers. | Referral becomes a measurable acquisition channel |

**Implementation for technical founders:** Start with a simple invite link that tracks the referrer. Store the referrer's user ID as a property on the new signup (this also feeds your product analytics — you can measure referral cohort quality). Build the reward logic after you see organic referrals happening.

**Example — API monitoring product:**
"Share your status page" — every monitoring product has a public status page. Make it easy to share. Every viewer is a potential user. Add "Powered by [your product]" with a link. This is referral marketing without needing an explicit program.

**Example — SEO keyword research tool:**
"Share this keyword report" — let users generate shareable reports with a branded footer and signup link. Freelance SEOs share reports with clients constantly. Each shared report is a distribution event.

### Affiliate Programs (Creator/Partner-Driven)

Affiliate programs pay external partners (bloggers, YouTubers, newsletter authors, comparison sites) a commission for referred signups or sales.

**When to start:** Later than you think. You need a product worth recommending, a conversion funnel that works, and enough margin to pay 15–30% recurring commissions. Most SaaS companies under $10K MRR shouldn't run an affiliate program — the overhead exceeds the return.

**Commission structures:**

| Model | Typical rate | Best for |
|---|---|---|
| One-time per signup | $10–$100 per paid conversion | Lower-ACV products, high-volume signups |
| Recurring % of revenue | 15–30% for 12 months | Higher-ACV, subscription products |
| Tiered (increasing with volume) | Base 20%, 25% at 10+/month, 30% at 50+ | Motivating high-volume affiliates |

**Tools:** Rewardful, PartnerStack, FirstPromoter. These handle tracking, attribution, payouts, and partner dashboards. Don't build this yourself unless your engineering time is genuinely free.

**Finding affiliates:** Look for content creators who already write comparison posts or reviews in your category. Reach out with: "We noticed your article on [topic]. We have an affiliate program — would you be interested in trying the product and potentially including it?" Start with 5–10 targeted partners, not a public "anyone can join" program.

---

## Events & Conferences

### The Honest Assessment

Events are the most expensive marketing channel per dollar and per hour. A conference booth costs $5K–$50K+. Even attending without a booth costs $1K–$5K per person (travel, hotel, ticket, meals). The ROI calculation only works for high-ACV products where one deal can cover the cost of the event.

**When events are worth it:**
- Enterprise SaaS ($10K+/year ACV) where a handshake leads to a pilot
- Vertical SaaS where the industry has 2–3 must-attend events per year
- Developer tools where speaking at conferences builds community credibility
- Products where trust and relationships drive purchasing decisions

**When events are NOT worth it:**
- Self-serve PLG products with < $100/month price points
- Early stage with no product-market fit (you're spending money to learn things you could learn cheaper online)
- As a first marketing channel (events amplify momentum, they don't create it)

### Types of Events

**Tier 1 — Free or nearly free:**
- Local meetups (attend, present, or host) — $0–$50
- Virtual conferences and webinars — $0
- User group meetups you organize yourself — $100–$500 for pizza and a room
- Co-hosted events with partners — split costs

**Tier 2 — Moderate investment:**
- Conference attendance (no booth) with intentional networking — $1K–$3K
- Speaking at conferences — usually free admission, travel costs only
- Small regional events with a demo table — $1K–$5K

**Tier 3 — Major investment:**
- Conference booth — $5K–$50K+
- Conference sponsorship — $10K–$100K+
- Hosting your own event — $5K–$50K+

**Start at Tier 1.** If local meetups exist for your audience, present at them. Prepare a 10–15 minute talk that teaches something useful (not a product pitch). Have a demo ready for conversations afterward. This costs almost nothing and puts you directly in front of your audience.

### Maximizing Event ROI

Before the event: set a specific goal (5 qualified conversations, 3 demo requests, 1 partnership lead). Research attendees if the list is available. Schedule meetings in advance.

During the event: spend time in hallways and sessions, not just at your booth. The best conversations happen over coffee, not across a table covered in branded swag.

After the event: follow up within 48 hours. Personalize each follow-up with something specific from your conversation. Connect on LinkedIn. Most event leads die because follow-up is slow or generic.

---

## PR & Press

### Setting Realistic Expectations

PR is not a marketing strategy — it's a marketing amplifier. A TechCrunch mention when you have no product, no landing page, and no conversion funnel is wasted attention. PR works when you have a functioning funnel and the traffic spike can convert into actual users.

PR is also unpredictable. You can pitch 30 journalists and get zero coverage. Or you can get picked up organically by someone who stumbled on your product. Don't depend on PR as a channel — treat it as a bonus when it happens and a strategic tool when the timing is right.

### What's Actually Newsworthy

Most SaaS products are not inherently newsworthy. "We launched a new tool" is not news. Journalists get hundreds of these pitches per week.

**Newsworthy angles:**
- Remarkable data or results ("Our users reduced API downtime by 73% — here's how")
- A genuine contrarian take backed by evidence
- A significant funding round ($5M+, or notable investors)
- A notable customer win (recognizable brand name, with permission)
- Open-sourcing something valuable
- An industry trend you can provide expert commentary on

**Not newsworthy (don't pitch these):**
- Product launches without a remarkable hook
- Feature updates
- Hiring announcements (unless C-level at a notable company)
- Awards you gave yourself

### Building Media Relationships

The best PR doesn't come from cold pitches — it comes from relationships built before you need them.

**Tiered approach:**

| Level | Method | Timeline |
|---|---|---|
| Good | Identify 5–10 journalists/newsletter authors who cover your space. Follow them on social media. Engage genuinely with their content. When you have real news, you're a familiar name, not a stranger. | Ongoing, 2–3 months before you need them |
| Better | Offer value before asking: share data they can use, provide expert quotes for their stories, connect them with customers willing to be sources. Become a trusted resource. | 3–6 months of relationship building |
| Best | Retained PR agency or dedicated comms person who has existing journalist relationships. Coordinated launch campaigns with embargo, exclusives, and follow-up. | Ongoing, $3K–$15K/month |

### Press Launch Playbook

When you do have something genuinely newsworthy:

```
4 weeks before: Identify 10–20 target publications and journalists
3 weeks before: Draft press release and pitch email (short — 3 paragraphs max)
2 weeks before: Send pitch to 3–5 priority journalists with an offer of an exclusive or early access
1 week before: Follow up with remaining journalists, share embargo details if applicable
Launch day: Publish your own announcement, share across all your channels
Day 2–3: Follow up with anyone who expressed interest but didn't publish
Week 2: Send a "results" follow-up if you have impressive launch metrics to share
```

---

## Sponsorships

### Newsletter Sponsorships

Sponsoring niche newsletters is an underused paid channel for SaaS. A newsletter with 5,000 subscribers in your exact ICP can outperform a LinkedIn campaign with 100K impressions — because every reader opted in and trusts the curator.

**Finding newsletters to sponsor:** Check what newsletters your customers read (ask in interviews, or use SparkToro). Search for "[your niche] newsletter" and look for Substack, Beehiiv, and ConvertKit-based publications. Check sponsorship marketplaces (Swapstack, Paved, Sponsorgap).

**Pricing:** Typically $25–$100 per 1,000 subscribers. A 10,000-subscriber newsletter might charge $250–$1,000 per placement. Niche = higher price per subscriber but better conversion.

**What makes a good newsletter sponsorship:**
- Audience matches your ICP (obvious but often ignored for reach)
- High open rates (30%+ is good, 40%+ is excellent — ask the publisher)
- Editorial tone (curated, trusted) vs. aggregator (firehose of links — lower trust)
- Dedicated placement (solo send) vs. inline mention (section within a larger newsletter)

**Testing approach:** Start with 2–3 placements in the same newsletter to see if it converts. One placement isn't enough data. Track with unique UTM parameters or a dedicated landing page. If CAC is viable after 3 placements, negotiate a monthly deal at a discount.

### Podcast Sponsorships

Similar dynamics to newsletters — niche podcasts with small, loyal audiences often outperform broad ones.

**Pricing:** $15–$50 per 1,000 downloads (CPM). A podcast with 5,000 downloads per episode might charge $75–$250 per episode.

**Types of sponsorship:**
- Pre-roll (beginning of episode): highest listen rate, brief mention
- Mid-roll (during episode): best engagement, host reads the ad conversationally
- Post-roll (end of episode): cheapest, lowest listen-through rate

**Host-read vs. pre-produced:** Always prefer host-read. The host's endorsement is the whole point. A pre-produced ad inserted into a trusted podcast sounds like what it is — an interruption.

### Community Sponsorships

Sponsoring a Discord server, Slack community, or open-source project gives you presence in a space your audience trusts.

**What this looks like:** Logo placement, sponsored channel or role, event sponsorship within the community, or funding community resources (documentation, tutorials).

**Cost:** Highly variable — $100/month for a small Discord server to $5,000+/month for a major open-source project.

**Best for:** Developer tools and products where community credibility matters more than direct-response conversion. You're buying trust and presence, not clicks.
