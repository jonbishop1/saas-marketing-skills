---
name: saas-product-launches
description: >
  Execution playbooks for launching new SaaS products and features. Covers go-to-market strategy, launch planning, Product Hunt launches, Hacker News launches, beta launches, feature announcements, launch sequencing, launch day execution, and post-launch recovery. For developers and technical founders building SaaS products, developer tools/APIs, and enterprise software. Trigger whenever a user asks about launching a product, planning a launch, Product Hunt strategy, announcing a feature, beta launch strategy, launch checklist, launch timeline, or any question about going live — even if they just say "I'm about to launch" or "how do I announce this feature" or "my launch flopped, what now."
---

# SaaS Product Launches

Audience: developers and technical founders. Explain things in engineering terms. Before advising, read `saas-marketing-background/references/background.md` and gather missing background. Be a launch strategist and coach — diagnose what they have, what they're launching, and build an execution plan that fits their real situation.

This is the execution companion to `saas-marketing-plan`. The marketing plan decides what to do and when. This skill tells you exactly how to execute a launch.

---

## Table of Contents

1. [Two Types of Launches](#two-types-of-launches)
2. [Situation Assessment](#situation-assessment)
3. [Three Tiers of Launch Sophistication](#three-tiers-of-launch-sophistication)
4. [Launch Channel Tactics](#launch-channel-tactics)
5. [Documentation as Launch Strategy](#documentation-as-launch-strategy)
6. [Launch Day Execution](#launch-day-execution)
7. [Post-Launch: The First Two Weeks](#post-launch-the-first-two-weeks)
8. [When the Launch Doesn't Work](#when-the-launch-doesnt-work)
9. [Reference Files](#reference-files)

---

## Two Types of Launches

**New product launch:** The world meets your product for the first time. You have no users, no brand recognition, and no distribution. The goal is to generate initial awareness, get your first users, and learn as fast as possible. Every interaction is a first impression.

**Feature launch:** You're announcing something new to an existing audience. You have users, an email list, a social presence, and possibly paying customers. The goal is adoption (get existing users to try it), retention (give churning users a reason to stay), expansion (give users a reason to upgrade), and acquisition (give prospects a new reason to sign up).

These share some mechanics (timing, channel tactics, messaging) but differ in audience, expectations, and success metrics. The SKILL.md covers shared frameworks. For full playbooks:

- New product launch → `references/product-launch.md`
- Feature launch → `references/feature-launch.md`

---

## Situation Assessment

A launch plan built for a funded startup with a marketing team looks nothing like one built for a solo founder shipping from their apartment. Assess before planning.

### What Are You Launching?

**New product — assess:**
- Is this a v1 launch or a beta/early access launch? (Beta is lower stakes, different messaging)
- Does the product category already exist? (Existing category = easier to explain, harder to differentiate. New category = harder to explain, less competition.)
- Is there a visual demo or is it invisible infrastructure? (Visual products get more traction on Product Hunt and social.)
- Is it an API/developer tool? (Documentation is part of the launch, not an afterthought.)
- What's the signup flow? (Free trial, freemium, demo request, waitlist, API key?)

**Feature launch — assess:**
- How big is this feature? (Quality-of-life improvement vs. new capability vs. new product line)
- Does it affect all users or a specific segment?
- Does it change pricing or packaging?
- Is it available to all plans or gated behind an upgrade?
- How many existing users have requested this? (Requested features get higher adoption.)

### Resources Available

**Time until launch:**
- < 1 week — skip the plan, just ship and announce. Come back here for the next one.
- 1–2 weeks — Tier 1 launch. Focus on the basics.
- 2–4 weeks — Tier 2 launch. Proper preparation across channels.
- 4+ weeks — Tier 3 launch. Full campaign with coordinated channels.

**People:**
- Just you? Tier 1, possibly Tier 2 with preparation.
- You + 1 person? Tier 2 is realistic.
- Team of 3+? Tier 3 is feasible.

**Existing distribution:**
- Email list size? (50 people vs. 5,000 people changes the playbook entirely)
- Social following? (which platforms, how engaged)
- Community presence? (are you known in relevant communities)
- Previous launch experience? (have you done Product Hunt, HN, press before)
- Existing customer base? (for feature launches — how many, how engaged)

**Budget:**
- $0 — organic-only launch. Still effective if you have distribution or community presence.
- $100–$500 — small boosts: promoted social posts, newsletter sponsorship during launch week.
- $500–$2,000 — meaningful paid amplification: launch-week ad campaigns, multiple sponsorships.
- $2,000+ — full paid campaign alongside organic launch.

### Launch Sizing

Not every launch deserves the same treatment. Match the launch effort to the impact.

| Launch type | Effort level | Channels | Prep time |
|---|---|---|---|
| Bug fix / minor improvement | No launch — changelog entry | Product changelog, maybe a tweet | 0 |
| Quality-of-life feature | Light — in-app + email | In-app notification, email to affected users, tweet | 1–2 days |
| Significant new feature | Medium — multi-channel | Email, blog post, social media, community post | 1–2 weeks |
| Major capability / new product line | Full — coordinated campaign | All channels, possibly press, Product Hunt | 2–4 weeks |
| New product launch | Maximum — everything you have | All channels, Product Hunt, HN, press, communities, email, social, paid | 3–6 weeks |

---

## Three Tiers of Launch Sophistication

### Tier 1 — Ship and Announce (solo founder, minimal prep, 1 week)

The product is ready (or ready enough). Don't delay launch to build a marketing campaign. Ship it and tell people.

**What you do:**
- Write a clear, concise announcement (what it does, who it's for, how to try it)
- Post on Product Hunt (if it's a new product)
- Post on Hacker News ("Show HN" for new products, regular post for interesting features)
- Share in 3–5 communities where your audience gathers
- Email your list (even if it's 20 people)
- Post on your social accounts
- That's it. Go talk to the people who show up.

**What you skip:**
- Press outreach
- Pre-launch buildup campaign
- Paid ads
- Launch video
- Influencer coordination

**What you get:** A spike of initial attention, 10–100 first users (depending on community reach), and — most importantly — your first real feedback from real users.

**Performance note:** Tier 1 launches produce smaller spikes but get you to market fastest. The biggest risk isn't a small launch — it's spending weeks preparing a launch for a product nobody wants. Ship, learn, iterate.

### Tier 2 — Prepared Launch (small team, 2–4 weeks prep)

You have time to prepare and want to maximize the launch window.

**What you add to Tier 1:**
- Pre-launch audience building (waitlist, teaser content, "building in public" posts)
- Polished landing page with social proof (testimonials from beta users, logos, metrics)
- Launch-day coordination across channels (specific timing, pre-written posts, email scheduled)
- Blog post with deeper product story (problem, solution, why now, how it works)
- Documentation (especially for developer/API products — see Documentation section)
- 5–15 people committed to supporting on launch day (PH upvotes, HN engagement, social shares)

**What you skip:**
- Press outreach (unless you have existing relationships)
- Paid ads beyond small boosts
- Launch video production (screen recording with voiceover is fine)
- Influencer campaign

**What you get:** A larger, more sustained spike. Better conversion because the landing page is polished. More credible first impression.

### Tier 3 — Coordinated Campaign (team, 4+ weeks prep, budget)

Full launch campaign with multiple channels firing in sequence.

**What you add to Tier 2:**
- Press outreach (pitched 2–3 weeks before launch)
- Coordinated influencer/creator outreach (early access + launch day amplification)
- Launch video (product demo, founder story, or problem narrative)
- Paid ads launching simultaneously (retargeting at minimum, prospecting if budget allows)
- Email sequence (teaser → launch → follow-up → case study, spread over 2 weeks)
- Partner co-announcements (integration partners, investors, notable customers)
- Multiple content pieces (blog, technical deep-dive, comparison, use cases)

**What you get:** Maximum reach and conversion. Multiple touchpoints over days/weeks, not a single spike. This is appropriate for major product launches or pivotal feature launches that affect pricing/positioning.

**Performance note:** Tier 3 takes 10–20x the effort of Tier 1. It produces maybe 3–5x the results. The ROI per hour is actually lower — but the absolute outcome is higher. Only invest this effort when the launch stakes justify it.

---

## Launch Channel Tactics

Each channel behaves differently during a launch. Timing, format, and approach matter.

### Product Hunt

Best for: new product launches, major feature launches, products with visual appeal.

**Timing:** Launch at 12:01 AM Pacific Time. The PH day resets at midnight PT. Launching early gives you the full 24-hour window. Best days: Tuesday, Wednesday, Thursday.

**What to prepare:**
- Tagline: 60 characters max, benefit-focused, no jargon
- Description: 3 paragraphs — what it does, who it's for, what makes it different
- Visuals: thumbnail (240×240), gallery images (1270×760), optional video or GIF
- Maker comment: your first comment explaining why you built this, personal story
- Hunter: ideally someone with a PH following who nominates your product (you can also self-post)

See `references/product-launch.md` → Product Hunt Deep Dive for the full playbook.

### Hacker News

Best for: developer tools, technical products, technically interesting features, open-source projects.

**Format:** "Show HN: [Product name] – [one-line description of what it does]". Keep the description technical and specific. HN rewards genuine technical depth and punishes marketing speak.

**Timing:** Post between 8–10 AM Eastern on weekday mornings. HN traffic peaks during US work hours. Avoid weekends and holidays.

**Critical rules:** Do not ask people to upvote. Do not coordinate voting rings. HN detects and penalizes this aggressively. Instead, share the link organically and ask people to engage with comments if they find it interesting.

See `references/product-launch.md` → Hacker News Deep Dive for the full playbook.

### Email

The highest-converting launch channel for feature launches (you're emailing people who already use your product) and a strong channel for new product launches if you have a waitlist.

**New product launch email sequence:**
- T-7 days: "We're launching next week" (to waitlist — builds anticipation)
- T-0 (launch day): "We're live" (clear CTA to sign up/try it)
- T+3 days: "Here's what people are saying" (social proof from early users)
- T+7 days: "Quick question" (ask for feedback, keep conversation going)

**Feature launch email:**
- Single email to all users (for major features) or segmented email (for features relevant to specific user types)
- Subject line: lead with the benefit, not the feature name. "You can now [outcome]" beats "[Feature Name] is here"

### Social Media (Twitter/X, LinkedIn)

**Pre-launch (1–2 weeks before):** Build anticipation. Tease what's coming without revealing everything. Share screenshots, behind-the-scenes, building-in-public progress.

**Launch day:** Post the announcement with a clear CTA and visual (screenshot, GIF, or video). Pin the post. Engage with every reply. Ask your team and supporters to share (not just like — shares extend reach). Post 2–3 times throughout the day (morning, afternoon, evening) with different angles.

**Post-launch (days 2–7):** Share user reactions, early results, interesting use cases. Each post is a new opportunity for someone to discover the product.

### Communities (Reddit, Discord, Slack, Forums)

**Critical rule:** Do not spam-launch across 20 communities simultaneously. Communities can tell when you're carpet-bombing. Pick 3–5 where you're already a known member and share authentically.

**Format by platform:**
- Reddit: "I built [product] to solve [problem]. Here's what I learned." Tell the story, be transparent, invite questions. Post in the most relevant subreddit first.
- Discord/Slack: Share in #showcase or #tools channels. Add background — why you built it, who it's for. Answer questions in real-time.
- Forums: Follow the community's norms for self-promotion. Many forums have specific threads for launches.

---

## Documentation as Launch Strategy

For developer products and APIs, documentation is not a post-launch task — it's a launch channel. Developers evaluate tools by reading the docs before they sign up. Bad docs on launch day means lost users you'll never get back because they already formed their opinion.

### Minimum Documentation for Launch

| Doc type | Priority | What it covers |
|---|---|---|
| Quick start guide | Must-have | Get from zero to "hello world" in < 5 minutes |
| API reference | Must-have (API products) | Every endpoint, method, parameter, and response |
| Authentication guide | Must-have | How to get an API key, how auth works |
| Core concepts | Should-have | Mental model for how the product works |
| Example use cases | Should-have | 2–3 common scenarios with code samples |
| Changelog | Should-have | What's new, what changed — starting from day one |
| Migration guide | Nice-to-have | If replacing an existing tool — how to switch |
| SDKs and libraries | Nice-to-have | Language-specific wrappers for the API |

**Tiered approach:**

| Level | What to ship on launch day |
|---|---|
| Good | Quick start + API reference + auth guide. Hosted on your site or a GitHub README. |
| Better | Everything above + core concepts + 2–3 example use cases. Hosted on a docs platform (GitBook, Mintlify, Docusaurus, ReadMe). |
| Best | Everything above + interactive API explorer, SDKs for top 2–3 languages, runnable code examples, community forum or Discord for questions. |

**Example — API monitoring product:**
Launch docs must include: quick start for configuring your first monitor (< 3 minutes), API reference for the monitoring and alerting endpoints, webhook integration guide, and a "configure alerting" example. Without these, developers bounce.

**Example — SEO keyword research tool:**
Less docs-critical (it's a UI product), but still needs: quick start for running your first keyword search, explanation of how keyword difficulty is calculated (transparency builds trust with SEO practitioners), and API reference if there's an API tier.

### Docs as a Marketing Channel

Good documentation drives organic traffic. Developers search for "how to monitor API uptime" or "REST API rate limiting." If your docs answer these questions and include your product as the solution, that's acquisition content disguised as documentation.

Structure your docs with SEO in mind: clear titles, headers with target keywords, standalone pages for each major topic. A doc page titled "How to Set Up API Uptime Monitoring" can rank in Google alongside your blog content.

---

## Launch Day Execution

A launch day is a coordinated sequence, not a single event. Timing matters because each channel has different peak engagement windows and they compound when sequenced correctly.

### Launch Day Timeline

```
BEFORE MIDNIGHT PT (the night before):
  - Final check: landing page live, signup flow working, docs accessible
  - Queue social posts (or have them drafted and ready)
  - Email scheduled or ready to send
  - Product Hunt listing drafted and ready to submit

12:01 AM PT — PRODUCT HUNT (if using PH)
  - Submit listing (or have your hunter submit)
  - Post your maker comment immediately
  - Share PH link to your inner circle (people who committed to engaging)

7:00–8:00 AM ET — HACKER NEWS
  - Submit "Show HN" post
  - Be ready to answer comments for the next 2–3 hours
  - Don't share the HN link asking for upvotes — just be present in the comments

8:00–9:00 AM ET — EMAIL
  - Send launch announcement to your email list
  - If feature launch: send in-app notification to active users

9:00–10:00 AM ET — SOCIAL MEDIA
  - Publish main announcement post on Twitter/X and/or LinkedIn
  - Pin the post
  - Begin engaging with replies

10:00 AM–12:00 PM ET — COMMUNITIES
  - Share in your top 3–5 communities (stagger, don't blast simultaneously)
  - Be present in each to answer questions in real-time

12:00 PM–6:00 PM ET — SUSTAIN
  - Post a second social update (early results, user reactions, interesting stats)
  - Respond to every PH comment and social reply
  - Monitor and jump into any organic discussions that appear

EVENING — FIRST DEBRIEF
  - How many signups? From which channels?
  - Any major issues? (broken flows, confused users, server problems)
  - What questions are people asking? (these inform tomorrow's content)
```

### The Most Common Launch Day Mistakes

**Launching without testing the signup flow.** Test the full journey — from landing page to account creation to first action — on the morning of launch. Don't assume it works because it worked yesterday.

**Going silent after the initial post.** A launch isn't a single post — it's a day of engagement. If you post once and disappear, you lose the momentum. Be present, respond to everything, share updates throughout the day.

**Posting the same message everywhere.** Each community has different norms and expectations. Your Reddit post should be a story. Your HN post should be technical. Your tweet should be punchy. Your email should be personal.

**Asking for upvotes.** On Product Hunt and Hacker News, this backfires. Ask people to "check it out and share their honest feedback." Genuine engagement matters more than vote count.

**Launching on a Friday or weekend.** Unless your audience is consumers, avoid it. Business and tech audiences are most active Tuesday–Thursday.

---

## Post-Launch: The First Two Weeks

The launch spike fades. What you do in the 14 days after launch determines whether you captured momentum or just had a good day.

### Days 1–3: Capture and Respond

**Priority: Talk to everyone who showed up.**
- Respond to every email, comment, and DM within hours, not days
- Reach out personally to your first 10–20 signups: "Thanks for signing up — what brought you here?"
- Fix any bugs or issues that launch-day users surface (they will)
- Post a "day 1 results" update on social media (be transparent about real numbers)

### Days 4–7: Learn and Adjust

**Priority: Understand what's working and what's not.**
- Check activation: are launch users actually using the product, or just signing up?
- Identify drop-off points: where in the signup/onboarding flow are people leaving?
- Ask the "how would you feel" question: "How would you feel if you could no longer use [product]?" (Sean Ellis test — even 10 responses are directionally useful)
- Publish a follow-up content piece: what you built, what you learned, early user stories. This catches the long tail of people who heard about the launch but didn't act immediately.
- Send the T+3 and T+7 emails (see Email section above)

### Days 8–14: Transition to Steady State

**Priority: Shift from launch mode to growth mode.**
- The spike is over. What does your daily/weekly signup rate look like now? That's your new baseline.
- Identify which launch channel produced the highest-quality signups (not the most — the best activating and retaining). This informs your ongoing channel strategy (route to `saas-marketing-plan`).
- Set up basic analytics if you haven't (route to `saas-data-analysis`). You need to measure what happens next.
- Start your first ongoing marketing channel (route to `saas-marketing-plan` for channel selection).
- Collect testimonials from early users for your landing page (while the experience is fresh).

---

## When the Launch Doesn't Work

Sometimes the launch lands flat. Low traffic, few signups, no engagement. This is common and not a death sentence — but you need to diagnose correctly before trying again.

### Diagnosing the Problem

```
Step 1: Did people see the launch?
  → Check impressions/views across channels
  → If low: distribution problem — your announcement didn't reach enough people
  → If decent: proceed to step 2

Step 2: Did people click through?
  → Check CTR from launch channels to your site
  → If low: messaging problem — the announcement didn't compel people to look
  → If decent: proceed to step 3

Step 3: Did people sign up?
  → Check landing page conversion rate
  → If low: landing page problem — they arrived but weren't convinced
  → If decent: proceed to step 4

Step 4: Did people activate?
  → Check activation rate
  → If low: onboarding/product problem — they signed up but didn't get value
  → If decent: the launch actually worked — your expectations may have been too high
```

### Recovery Strategies

**Distribution problem (nobody saw it):**
- The launch wasn't the failure — the reach was. You can relaunch.
- Wait 2–4 weeks. Improve your announcement based on whatever feedback you got.
- Build more distribution before the next attempt: grow your email list, engage more in communities, build social following.
- Try different channels: if Reddit was crickets, try HN. If HN was crickets, try direct outreach.

**Messaging problem (they saw it but didn't click):**
- Your headline/tagline/description didn't resonate. This is a positioning problem.
- Go back to audience research (route to `saas-audience-research`). Look at the exact language your audience uses to describe the problem.
- Rewrite your announcement in their words, not yours.
- Test the new messaging in communities before a full relaunch.

**Landing page problem (they clicked but didn't sign up):**
- The page didn't convert. Common issues: unclear value prop, no social proof, too much friction (long forms, no free option), slow page load, mobile-broken layout.
- Run 5 user tests: ask 5 people to look at the page and tell you what the product does and who it's for. If they can't answer, your page isn't clear enough.
- Simplify. Cut copy. Make the CTA obvious. Add a testimonial or metric if you have one.

**Activation problem (they signed up but didn't use it):**
- This is a product/onboarding problem, not a launch problem. The launch worked.
- Focus on onboarding: what's the fastest path to value? Can you get a new user to their "aha moment" in under 5 minutes?
- For developer/API products: is the quick start guide actually quick? Time yourself going through it.
- Send a personal email to 5–10 users who signed up but didn't activate. Ask what happened.

### When to Relaunch

You can relaunch a product. There's no rule against it. Most people who didn't see the first launch won't know there was one.

**Product Hunt:** You can only launch once per product, but you can launch major updates as a new listing. Some products launch 2–3 times over their lifecycle.

**Hacker News:** You can repost after a failed submission. Wait at least 2 weeks. Change the title. Make sure the product has improved.

**Everything else (communities, social, email):** You can re-announce as many times as the content is fresh. "We launched 3 months ago, here's what we learned and what changed" is a valid second launch.

---

## Reference Files

- `saas-marketing-background/references/background.md` — shared intake questions; read before advising
- `references/product-launch.md` — complete new product launch playbook: timelines, channel deep dives (Product Hunt, Hacker News, press, communities), pre-launch buildup, beta launches, launch week schedules by tier, and post-launch transition
- `references/feature-launch.md` — complete feature launch playbook: sizing the announcement, internal coordination, email and in-app announcement templates, upgrade-gated features, adoption tracking, and feature launch cadence
