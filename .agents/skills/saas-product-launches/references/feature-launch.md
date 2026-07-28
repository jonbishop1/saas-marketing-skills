# Feature Launch Playbook

Complete execution guide for announcing new features, capabilities, and product updates to an existing audience. Covers everything from sizing the announcement to measuring adoption.

---

## Table of Contents

1. [Sizing the Announcement](#sizing-the-announcement)
2. [Feature Launch Templates by Size](#feature-launch-templates-by-size)
3. [Email Announcements](#email-announcements)
4. [In-App Announcements](#in-app-announcements)
5. [Social & Blog Announcements](#social--blog-announcements)
6. [Upgrade-Gated Features](#upgrade-gated-features)
7. [Documentation Updates for Feature Launches](#documentation-updates-for-feature-launches)
8. [Adoption Tracking](#adoption-tracking)
9. [Feature Launch Cadence](#feature-launch-cadence)

---

## Sizing the Announcement

Not every feature gets a blog post and email campaign. Mismatching announcement size to feature importance either exhausts your audience (too many big announcements for small changes) or undersells meaningful improvements.

### The Feature Impact Matrix

| | Few users affected | Most users affected |
|---|---|---|
| **Small improvement** (faster, smoother, bug fix) | Silent fix. Changelog only. | Changelog + tweet. Maybe in-app notice. |
| **Meaningful feature** (new capability, new integration) | Targeted email to affected segment + in-app. | Blog post + email to all users + social + in-app. |
| **Major capability** (new product area, pricing-affecting) | Targeted email + blog + social + community. | Full launch campaign (treat like a small product launch). |

### Determining Feature Size

Ask yourself:
1. **How many users asked for this?** (high demand = bigger announcement)
2. **Does this change what the product can do, or just how well it does it?** (new capability > improvement)
3. **Does this affect pricing or packaging?** (any pricing change = major announcement)
4. **Would a prospect care about this?** (if yes, it's an acquisition tool, not just a retention tool)
5. **Does this create a story worth telling?** (interesting technical approach, notable customer need, industry trend)

**Example — API monitoring product:**
- Adding support for TCP monitors alongside HTTP: meaningful feature, affects users who need non-HTTP monitoring. Targeted email + blog post + in-app notification.
- Adding Slack integration for alerts: meaningful feature, most users want this. Blog post + email to all users + prominent in-app announcement.
- Adding distributed monitoring from 10 global regions: major capability, changes the product category. Full launch campaign.

**Example — SEO keyword research tool:**
- Improving keyword difficulty calculation accuracy: small improvement but affects all users. Changelog + tweet explaining what changed. In-app notice.
- Adding "content gap analysis" feature: meaningful new capability. Blog post + email + social + in-app.
- Launching an API tier for agency automation: major capability, new audience segment, pricing change. Full launch campaign.

---

## Feature Launch Templates by Size

### Small: Changelog + Tweet (30 minutes)

```
CHANGELOG ENTRY:
  - Feature name: [name]
  - What changed: [1–2 sentences]
  - How to use it: [1 sentence or link to docs]

TWEET/SOCIAL POST:
  "[Product] update: [benefit in one line]. [Screenshot or GIF]"
```

This is appropriate for bug fixes, performance improvements, UI tweaks, and minor enhancements. Don't overthink it — ship and note it.

### Medium: Email + Blog + In-App (half day)

```
PRE-LAUNCH (day before):
  - Write blog post (500–1,000 words): problem, solution, how it works, how to try it
  - Draft email announcement
  - Prepare in-app notification or banner
  - Update documentation

LAUNCH DAY:
  - Publish blog post
  - Send email (morning, your users' timezone)
  - Activate in-app announcement
  - Post on social with screenshot/GIF
  - Share in 1–2 relevant communities if appropriate

DAY AFTER:
  - Check adoption: how many users tried the feature in the first 24 hours?
  - Respond to feedback
```

### Large: Multi-Channel Campaign (1–2 weeks)

```
WEEK -1:
  Mon: Teaser on social: "Something big coming to [product] next week"
  Wed: Blog post draft + email draft + landing page (if it warrants one)
  Thu: Reach out to select users for early access and testimonials
  Fri: Finalize all launch assets

LAUNCH WEEK:
  Mon: Launch day — blog post + email + in-app + social + communities
  Tue: Share early adoption metrics or user reactions on social
  Wed: Technical deep-dive post or video walkthrough
  Thu: Follow-up email to users who haven't tried it yet
  Fri: Week 1 adoption review

If the feature changes pricing or adds a new plan tier, treat this as a product launch — see references/product-launch.md.
```

---

## Email Announcements

### Writing Feature Announcement Emails

**Subject line principles:**
- Lead with the benefit, not the feature name
- "You can now [do something valuable]" beats "[Feature Name] is here"
- Be specific: "Track API latency by region" beats "New monitoring features"
- Keep under 50 characters for mobile readability

**Subject line examples:**

| Feature | Bad subject | Good subject |
|---|---|---|
| Slack integration | "Slack Integration Launched" | "Get alerts in Slack instantly" |
| Multi-region monitoring | "New: Global Monitoring" | "Monitor from 10 regions worldwide" |
| Content gap analysis | "Content Gap Analysis Feature" | "Find keywords your competitors rank for" |
| API access | "API Now Available" | "Automate your keyword research with our API" |

**Email body structure:**

```
[1 sentence: what's new and why it matters to you]

[Screenshot or GIF showing the feature in action]

[2-3 sentences: what you can do with it, specific use cases]

[CTA button: "Try it now" / "See how it works" / "Explore the new feature"]

[1 sentence: link to docs or blog post for more detail]
```

Keep it short. Feature emails should be scannable in 15 seconds. The goal is to get the user to try the feature, not to explain every detail in the email.

### Segmentation

Not every user should get every feature email. Segment when:
- The feature only applies to certain plans (don't email free users about a paid-only feature, unless you're using it to drive upgrades — see Upgrade-Gated Features section)
- The feature solves a specific use case (email users who've shown interest in that use case)
- The feature is technical (email API users about API improvements, not UI-only users)

**What to track in every feature email:**
- Open rate (is the subject line working?)
- Click rate (is the feature compelling?)
- Feature adoption within 48 hours of email open (did the email drive action?)

---

## In-App Announcements

In-app announcements reach users at the moment they're most receptive — they're already using the product. But overuse trains users to dismiss them.

### Announcement Types

| Type | Intrusiveness | Best for |
|---|---|---|
| **Changelog widget** (corner popup listing recent changes) | Low | All feature sizes. Always-on, user-initiated. |
| **Banner** (top of page, dismissible) | Low–Medium | Medium features. Visible but not blocking. |
| **Tooltip / hotspot** (small indicator on a new UI element) | Low | New buttons, menus, or options. Guides discovery. |
| **Modal** (centered popup) | High | Major features only. Use sparingly — users hate modals. |
| **Guided tour** (step-by-step walkthrough) | High | Complex features that need onboarding. Use only for major capabilities. |

**The modal rule:** Use a modal for a feature announcement no more than once per quarter. If every feature gets a modal, users start closing them without reading. Reserve modals for genuinely major announcements.

### Implementation

**Tier 1 (no in-app messaging tool):**
Add a dismissible banner to the top of your app. Store the dismissed state in the user's profile or local storage. Simple HTML/CSS — no tools needed.

**Tier 2 (lightweight tool):**
Use a changelog widget like Beamer, Headway, or Canny's changelog. These show a "what's new" badge users can click to see recent updates. Low-effort to maintain.

**Tier 3 (full in-app messaging):**
Use Pendo, Intercom, or Appcues for targeted in-app messages. These let you segment by user properties, trigger based on behavior, and A/B test message formats.

---

## Social & Blog Announcements

### Blog Post for Feature Launches

Not every feature needs a blog post. Write one when the feature is medium or large, or when the post can serve as acquisition content (someone searching for the capability might find it).

**Blog post structure for features:**

```
Title: "[Benefit-focused headline] — Now in [Product]"
  Example: "Monitor Your API from 10 Global Regions — Now in Pingwatch"
  Example: "Find Content Gaps in Seconds — New in KeywordScout"

Opening paragraph: What the feature does and why it matters. Lead with the customer problem.

Section 1: The problem this solves (1–2 paragraphs). Empathize with the frustration.

Section 2: How it works (2–3 paragraphs with screenshots or GIFs). Be specific and visual.

Section 3: Use cases (2–3 short examples). Help users imagine using it in their context.

CTA: "Try it now" link, link to docs, link to upgrade (if feature is plan-gated).

Closing: What's coming next (optional — builds anticipation for the next launch).
```

**SEO opportunity:** Feature blog posts can rank for feature-specific searches. "API monitoring by region," "keyword content gap analysis," "SEO tool with API access." Title and structure with search in mind.

### Social Media Announcements

**Post format that works for features:**

```
[1 line: what's new — benefit focused]

[Screenshot, GIF, or short video]

[2-3 lines: why it matters, specific use case]

[Link to blog post or product]
```

**Platform-specific notes:**
- **Twitter/X:** GIFs outperform static images for feature announcements. Keep the text punchy. Thread format works for larger features (tweet 1: the headline, tweets 2–4: use cases and details).
- **LinkedIn:** Longer posts work. Frame the feature in terms of the business problem it solves. Tag any beta testers or customers who contributed to the feature's development.

**Posting schedule for feature launches:**
- Day 0: Main announcement
- Day 1: Share a specific use case or user reaction
- Day 3: Technical detail or behind-the-scenes of how you built it
- Day 7: Results update ("X users tried it in the first week, here's what we learned")

---

## Upgrade-Gated Features

When a new feature is only available on a higher plan tier, the announcement becomes both a feature launch and a sales motion.

### How to Announce Plan-Gated Features

**To users on the qualifying plan:** Standard feature announcement. They get it — celebrate with them.

**To users on lower plans:** This is delicate. You want to drive upgrades without making free/lower-tier users feel punished.

**Good approach:**
- Announce the feature to everyone. Explain what it does and why it's valuable.
- Be transparent: "This feature is available on the [Plan] and above."
- Offer a way to try it: 7-day trial of the higher plan, or limited free usage.
- Don't be apologetic or salesy. State the value, state the availability, let users decide.

**Bad approach:**
- Announcing only to qualifying users and letting lower-tier users discover it locked (feels like a bait-and-switch)
- Aggressive "upgrade now!!!" messaging
- Making the feature visible in the UI but non-functional without an upgrade (frustrating UX)

### Email Template for Gated Features

```
Subject: [Benefit] — now on [Product] [Plan] plans

[Name],

We just shipped [feature]: [one sentence explaining what it does].

[Screenshot or GIF]

[2 sentences on the use case — how it helps]

[Feature] is available on [Plan] plans. Want to try it?
[CTA: "Start a 7-day trial of [Plan]" or "See pricing"]

Already on [Plan]? [CTA: "Try it now"]

— [Your name]
```

---

## Documentation Updates for Feature Launches

### For All Products

Every feature launch should update:
- **Changelog:** Date, feature name, 1–2 sentence description, link to docs
- **Relevant help docs:** Update any existing doc pages that now include the new feature
- **New doc page (if warranted):** Features with their own workflow deserve their own doc page

### For Developer / API Products

Documentation updates are mandatory, not optional. Developers will check the docs before trying the feature.

**What to update:**
- API reference: new endpoints, parameters, response formats
- Code examples: working sample code showing the new feature
- SDK/library updates: if you have language-specific SDKs, update and version them
- Migration guide (if the feature changes existing behavior): what's different, how to adapt

**Timing:** Documentation should be live before or simultaneously with the feature announcement. Never after. A blog post announcing a new API endpoint with no documentation for it wastes the announcement — developers will try the endpoint, fail to find docs, and leave.

**Example — API monitoring product, new multi-region monitoring:**
- New API docs page: "Multi-Region Monitoring" with endpoint reference
- Updated quick start: mention region selection during setup
- Code example: configuring a monitor with multiple check regions
- Blog post links to the docs page as the detailed reference

---

## Adoption Tracking

A feature launch isn't successful because you announced it. It's successful when users adopt it. Track adoption the same way you track product metrics (route to `saas-data-analysis`).

### Metrics to Track

| Metric | What it tells you | Timeframe |
|---|---|---|
| **Feature awareness** | % of users who saw the announcement (email open + in-app impression) | First 48 hours |
| **Feature trial** | % of users who tried the feature at least once | First 7 days |
| **Feature adoption** | % of users who use the feature regularly (weekly or appropriate cadence) | First 30 days |
| **Feature retention** | % of users who tried it and continue using it | 30–90 days |
| **Impact on core metrics** | Did the feature move retention, activation, or expansion revenue? | 60–90 days |

### Adoption Benchmarks

| Feature size | Expected awareness (7-day) | Expected trial (7-day) | Expected adoption (30-day) |
|---|---|---|---|
| Small improvement | 20–40% | 10–20% | Absorbed into normal usage |
| Meaningful feature | 40–60% | 15–30% | 10–20% of active users |
| Major capability | 60–80% | 20–40% | 15–30% of active users |

If trial is high but adoption is low, the feature is interesting but not sticky — investigate why users try it once and don't come back (usability, value, or discoverability issue).

If awareness is high but trial is low, users know about it but aren't compelled to try it — the announcement didn't convey the value clearly enough, or the feature doesn't solve a real problem.

### When to Re-Announce

If adoption is below expectations after 2 weeks:

1. **Reposition the feature.** Maybe the original announcement didn't frame the value correctly. Try a different angle: instead of "we added content gap analysis," try "find the keywords your competitors rank for that you're missing."

2. **Surface it contextually.** Instead of another email blast, show the feature via tooltip or banner at the moment in the product where it's most relevant. A user looking at their keyword list gets a tooltip: "New: see which keywords your competitors rank for that you don't."

3. **Create a use case post.** Write a blog post or email showing how a specific user or use case benefits from the feature. "How [Customer] uses multi-region monitoring to guarantee 99.99% uptime globally."

4. **Improve the onboarding to the feature.** Maybe users tried it but got confused. Simplify the flow, add a guided tour, or improve the in-feature help.

---

## Feature Launch Cadence

### How Often to Announce

**The quiet product problem:** If you ship improvements silently, users don't perceive progress. They see the same product they signed up for. Churn increases because they don't feel the product is getting better.

**The noisy product problem:** If every small change gets a big announcement, users tune out. When you do ship something major, the announcement has no signal — it's lost in the noise.

**Recommended cadence:**

| Announcement type | Frequency |
|---|---|
| Changelog update | Every release (weekly or biweekly) |
| Small email/social announcement | 1–2 per month |
| Medium blog + email campaign | 1 per month |
| Large multi-channel launch | 1 per quarter at most |

### Building a Feature Launch Calendar

Plan feature announcements alongside the product roadmap. When the engineering team plans a sprint, the launch plan for each feature should be scoped at the same time.

```
SPRINT PLANNING ADDITION:
  For each feature in the sprint:
    - Size the announcement (see Feature Impact Matrix)
    - Assign launch owner (who writes the announcement, prepares assets)
    - Set launch date (may differ from ship date — don't announce on Friday afternoon)
    - List required assets (email, blog post, in-app message, docs update, social)
```

This prevents the common pattern where features ship on Friday, nobody writes an announcement, and by Monday the team has moved on to the next sprint. Features should be announced, not just deployed.

### The "Shipped" vs. "Launched" Distinction

Shipping = the code is deployed and the feature is accessible.
Launching = users know about the feature and can find and use it.

Many SaaS products ship features that never get launched. They're in the product, they work, but nobody knows they exist. This is wasted engineering effort. If a feature was worth building, it's worth announcing.

A feature that's shipped but not launched is invisible. A feature that's launched but poorly adopted needs investigation. A feature that's adopted is a success — tell the story and build on it.
