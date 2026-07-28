# Trial Strategy Guide

Trial model decision framework, trial length optimization, feature gating strategy, freemium design, upgrade trigger patterns, and detailed onboarding tool comparisons.

---

## Table of Contents

1. [Choosing Your Trial Model](#choosing-your-trial-model)
2. [Trial Length Optimization](#trial-length-optimization)
3. [Credit Card Required vs. Not](#credit-card-required-vs-not)
4. [Freemium Design](#freemium-design)
5. [Feature Gating Strategy](#feature-gating-strategy)
6. [The Reverse Trial](#the-reverse-trial)
7. [Upgrade Trigger Patterns](#upgrade-trigger-patterns)
8. [Trial Expiry Experience](#trial-expiry-experience)
9. [Onboarding Tool Comparison](#onboarding-tool-comparison)
10. [Email Tool Comparison for Onboarding](#email-tool-comparison-for-onboarding)

---

## Choosing Your Trial Model

### Decision framework

The right trial model depends on product complexity, ACV, and GTM motion. Use this matrix:

| If your product is... | And your ACV is... | Consider... |
|---|---|---|
| Simple, value in minutes | < $50/mo | Freemium (free tier + paid upsell) |
| Simple, value in minutes | $50–200/mo | Free trial, no CC, 7–14 days |
| Medium complexity, value in hours | $50–200/mo | Free trial, no CC, 14 days |
| Medium complexity, value in hours | $200–500/mo | Free trial, 14 days; consider CC required |
| Complex, value takes days/team | $500+/mo | Free trial, 14–30 days, with sales assist |
| Complex, enterprise | $1,000+/mo | Demo-first, guided trial, sales-led |

### PingForge trial model analysis

PingForge is low complexity (value in 30 seconds), mid-range ACV ($29–149/mo). Best model: **freemium with usage limits.**

- Free tier: 5 endpoints, 5-minute check intervals, email alerts only
- Paid tiers: More endpoints, 30-second checks, Slack/PagerDuty alerts, team features
- Why freemium: The product delivers real value at the free tier. Users become dependent on the monitoring, then upgrade when they need more endpoints or faster checks. The free tier is the best possible sales pitch — it's the product itself.

### KeyScope trial model analysis

KeyScope is medium complexity (value in 5 minutes, full value requires exploring results), mid-range ACV ($49–199/mo). Best model: **14-day free trial, no CC required.**

- Trial: Full access to all features for 14 days
- Why free trial over freemium: Keyword gap analysis requires access to full data to evaluate. A freemium tier with limited keywords would prevent users from understanding the product's value. The trial lets them experience everything, then the conversion happens based on experienced value.
- Why no CC: PLG motion, self-serve signup. CC requirement would reduce signups 40–60% without a corresponding increase in trial quality at this ACV.

---

## Trial Length Optimization

### How to think about trial length

Trial length = time-to-value + evaluation buffer

| Component | Description |
|---|---|
| **Time-to-value** | How long it takes to set up and experience the core value. PingForge: 2 minutes. KeyScope: 10 minutes. Enterprise CRM: 3–5 days. |
| **Evaluation buffer** | Time to use the product enough to make a buying decision. Typically 2–5× the time-to-value, depending on decision complexity. |

### Common trial lengths and when they work

| Length | Works for | Doesn't work for |
|---|---|---|
| **7 days** | Simple tools with instant value. Creates urgency. | Anything requiring team buy-in or multi-day evaluation. |
| **14 days** | Most SaaS products. Standard expectation. Enough time for setup + meaningful use. | Complex enterprise tools requiring implementation. |
| **30 days** | Products requiring integration, data migration, or team onboarding. | Simple products — 30 days with a simple tool means no urgency. |

### Signals your trial is too long
- Most conversions happen in the first 5 days (the remaining trial days are wasted)
- Users who haven't activated by day 3 almost never convert (trial length isn't helping them)
- Trial extension requests are extremely rare (users have enough time)

### Signals your trial is too short
- High trial-to-paid conversion but many users requesting extensions
- Activation happens late in the trial (users are still setting up when the trial ends)
- Complex setup steps that legitimately take time (integrations, data import)

---

## Credit Card Required vs. Not

### The tradeoff

| Metric | No CC required | CC required |
|---|---|---|
| Signup volume | Higher (3–5× more signups) | Lower |
| Lead quality | Mixed (many tire-kickers) | Higher intent |
| Activation rate | Lower (20–35%) | Higher (40–60%) |
| Trial-to-paid conversion | Lower (2–5%) | Higher (15–25%) |
| Total conversions | Usually higher despite lower rate | Usually lower despite higher rate |
| Support burden | Higher (more unqualified users) | Lower |

### Decision guide

**Require CC when:**
- ACV > $200/month (higher commitment justified)
- Sales-assisted model (leads are already qualified)
- Support costs for free users are significant
- Product requires meaningful setup investment (filters serious evaluators)

**Don't require CC when:**
- PLG, self-serve motion
- ACV < $200/month
- Product value is experienced quickly (users convert based on experience, not commitment)
- You're optimizing for top-of-funnel volume (early stage, building a user base)

**The math:** If no-CC generates 1,000 signups/month at 3% conversion (30 customers) and CC-required generates 250 signups/month at 20% conversion (50 customers), CC-required wins on customers. But the 1,000 no-CC signups also generate brand awareness, word-of-mouth, and a larger pool for future re-engagement. The right choice depends on your growth stage and goals.

---

## Freemium Design

### The freemium decision

Freemium works when the product has a natural, valuable free tier that:
1. Delivers real value (not a crippled demo)
2. Creates a habit or dependency (users come back regularly)
3. Has a clear upgrade trigger (the user hits a limit that matches a paid feature)
4. Doesn't cannibalize paid signups (the free tier isn't "good enough" for serious use)

### What to gate (feature vs. usage limits)

| Gating type | How it works | Best for |
|---|---|---|
| **Usage limits** | Free tier has a cap (5 endpoints, 100 keyword searches, 3 projects) | Products where more usage = more value |
| **Feature limits** | Free tier lacks specific features (team collaboration, integrations, advanced analytics) | Products where specific features serve different market segments |
| **Capacity limits** | Free tier has lower performance (5-min check intervals vs 30-sec, limited data retention) | Products where performance tiers map to customer segments |
| **Support limits** | Free tier gets community support; paid gets direct support | Products where support is a significant cost |

### PingForge freemium structure

```
Free:     5 endpoints, 5-min checks, email alerts, 24h data retention
Starter:  25 endpoints, 1-min checks, Slack/email alerts, 30d retention   — $29/mo
Pro:      100 endpoints, 30-sec checks, all integrations, 90d retention   — $79/mo
Team:     Unlimited, 30-sec, all integrations, 1yr retention, team features — $149/mo
```

The upgrade triggers are natural: a developer starts with 5 endpoints, their project grows, they need more endpoints and faster checks. The upgrade happens because the user's needs grew, not because of artificial limitation.

### Freemium mistakes to avoid
- **The "too-good" free tier:** If 80% of users never need to upgrade, the free tier is too generous. It should serve individual/light use, not full production use.
- **The "too-crippled" free tier:** If free users can't experience enough value to understand the product, they'll never upgrade. The free tier must deliver real value.
- **Feature gating that prevents evaluation:** Don't gate the feature that demonstrates your differentiation. KeyScope's differentiation is opportunity scoring — gating that from free users prevents them from understanding why KeyScope is special.

---

## Feature Gating Strategy

### Rules for what to gate

1. **Never gate the activation action.** If running a keyword gap analysis is the activation metric, every user must be able to do it.
2. **Gate features that serve mature use cases.** Team collaboration, advanced analytics, API access, integrations — these serve users who already understand the value.
3. **Gate scale, not capability.** Let users do everything the product does, just at smaller scale. Then upgrade for more.
4. **Make the gate visible before they hit it.** Show the feature with a "Pro" badge. Let them see what they'd get. Don't hide paid features entirely — that prevents aspiration.

### Displaying gated features

**Good:** Feature is visible, clickable, and shows a preview or explanation of what it does with a clear upgrade path. "Team alerting is available on the Pro plan. See how it works →"

**Bad:** Feature is completely hidden from free users. They never know it exists, never aspire to it, never upgrade for it.

**Worst:** Feature appears to work but fails with an error message. "This feature is not available on your plan." Frustrating and feels deceptive.

---

## The Reverse Trial

### What it is
Users start with full paid features for a limited time (7–14 days), then downgrade to a free tier. They experience everything, then decide whether the premium features are worth paying for.

### When it works
- You have both a viable free tier and premium features worth experiencing
- The premium features take time to appreciate (users wouldn't know to upgrade if they never tried them)
- The switch from premium to free is noticeable (features they'll miss)

### Implementation
- Grant full access for N days after signup
- Show subtle "Premium" badges on features that will be gated after the trial
- As the trial nears end, highlight features they've used that are premium-only: "You've used Team Alerting 12 times. This feature is included on the Pro plan."
- After expiry, downgrade to free. Don't delete data — let them see their premium-generated data but not create new premium actions.

### PingForge reverse trial

14-day reverse trial: user gets Pro features (30-sec checks, all integrations, 90-day retention). After 14 days, downgrade to Free (5 endpoints, 5-min checks, 24h retention).

This is particularly effective for PingForge because: the user configures 30-second checks and Slack alerts during the trial. When downgraded to 5-minute checks and email-only alerts, the degradation is immediately noticeable — and the value of upgrading is visceral.

---

## Upgrade Trigger Patterns

### When to prompt for upgrade

| Trigger | Example | Why it works |
|---|---|---|
| **Usage limit approaching** | "You're using 4 of 5 free endpoints" | User is getting value and is about to need more |
| **Premium feature attempted** | User clicks a gated feature | They've identified a need — perfect moment to show value |
| **Value milestone reached** | "PingForge caught 3 incidents this week" | User has experienced and can quantify value |
| **Trial countdown** | "5 days left in your trial" | Creates time-based urgency |
| **Team expansion signal** | User invites a second team member | Team use = higher stickiness = higher willingness to pay |
| **Export/integration attempt** | User tries to export data or set up an integration | Signal of deeper commitment to the tool |

### Prompt design principles
- **Lead with value received, not value at risk.** "You've monitored 23 endpoints with 99.97% uptime tracking" beats "Your trial expires in 3 days."
- **Show the specific plan that fits.** Don't show all 4 plans — show the one that matches their usage. "Based on your 23 endpoints, the Pro plan ($79/mo) fits your usage."
- **Make it easy to dismiss.** Non-blocking. "Maybe later" should be prominent. Pushy upgrade prompts erode trust.

---

## Trial Expiry Experience

### What happens when the trial ends

The trial expiry experience determines whether borderline users convert or leave. Design it deliberately.

**Before expiry:**
- 7 days before: Email highlighting value received and features used
- 3 days before: In-app banner with countdown and upgrade CTA
- 1 day before: Email with urgency + offer help if they're stuck
- Day of: Email with clear "last chance" + what happens next

**At expiry (several options):**

| Approach | When to use |
|---|---|
| **Hard cutoff** | Access revoked immediately. Works for CC-required trials where the user committed upfront. |
| **Grace period** (3–7 days) | Access continues in read-only mode. User can see their data but not create new items. Gives them time to upgrade without losing work. |
| **Downgrade to free** | If freemium model, seamlessly transition to the free tier. No data loss, just reduced capability. |
| **Feature freeze** | Stop new functionality but let existing configurations continue running. PingForge: monitors keep running but user can't add new ones or change settings. |

**The worst possible experience:** Hard cutoff with data deletion. Never delete user data at trial expiry. They may come back in a month.

**After expiry (if they don't convert):**
- Day 1 post-expiry: "Your trial has ended. Your data is safe. Upgrade anytime to pick up where you left off."
- Day 7 post-expiry: "Still thinking about it? Here's what you accomplished during your trial: [specific value metrics]."
- Day 30 post-expiry: Last win-back attempt, possibly with a discount or extended trial offer.

---

## Onboarding Tool Comparison

Detailed comparison for technical founders evaluating onboarding tools.

### Appcues

**Best for:** PLG companies with non-technical team members managing onboarding flows.

- Strengths: Polished UI builder, good analytics, strong targeting/segmentation, no-code flow builder
- Weaknesses: Expensive for early-stage ($249+/mo), can feel like an overlay on top of the product rather than integrated
- Technical: Script tag + CSS selectors. Works with any frontend framework. SDK available for more control.
- Best at: Checklists, modals, tooltips, and announcements

### Userflow

**Best for:** Developer-friendly teams who want control without building from scratch.

- Strengths: Good developer experience, custom CSS support, clean default styling, reasonable pricing
- Weaknesses: Smaller ecosystem than Appcues, fewer integrations
- Technical: Script tag + CSS selectors. Good React/Vue support. Decent API.
- Best at: Checklists and resource centers

### CommandBar

**Best for:** Developer tools and technical products where a command palette adds value beyond onboarding.

- Strengths: Command palette (cmd+k) that doubles as search, help, and onboarding. Natural for developer audiences.
- Weaknesses: More expensive, onboarding is one feature among many
- Technical: React SDK, deep integration model
- Best at: Developer-focused products, in-app search + contextual help

### Chameleon

**Best for:** Companies needing advanced targeting and segmentation for onboarding.

- Strengths: Deep segmentation, A/B testing built in, micro-surveys, strong analytics
- Weaknesses: More complex setup, higher price
- Technical: Script tag + CSS selectors. Good API and webhook support.
- Best at: Segmented onboarding for multiple personas or use cases

### Product Fruits

**Best for:** Budget-conscious teams wanting solid basics.

- Strengths: Most affordable option with good coverage of core patterns, easy setup
- Weaknesses: Less polished UI, fewer integrations, smaller community
- Technical: Script tag. Simple integration.
- Best at: Basic checklists, tours, and hints at a reasonable price

### Custom build

**Best for:** Products with unique onboarding needs deeply integrated with the product experience.

- Strengths: Full control, deep product integration, no ongoing tool cost, no external dependency
- Weaknesses: Slower to iterate, requires dev time for every change, no built-in analytics
- Technical: You own it. React/Vue components, state management, event tracking — all custom.
- Best at: Setup wizards, empty states, product-integrated flows that tools can't replicate

### Recommendation by tier

| Tier | Recommendation |
|---|---|
| **Tier 1 (no budget)** | Custom build: welcome screen + empty states + basic checklist component. 1–2 days of dev time. |
| **Tier 2 ($100–250/mo)** | Product Fruits or Userflow for checklists and tooltips. Custom build for empty states and setup wizard. |
| **Tier 3 ($250+/mo)** | Appcues or Chameleon for the overlay layer. Custom build for product-integrated flows. Integrate with email tool for behavioral triggers. |

---

## Email Tool Comparison for Onboarding

### For time-based sequences (Tier 1–2)

| Tool | Price | Strengths | Best for |
|---|---|---|---|
| **Loops** | Free → $49+/mo | Built for SaaS, clean UX, easy sequences | SaaS startups, simple to medium flows |
| **Resend** | Free → $20+/mo | Developer-friendly, API-first, transactional + marketing | Technical founders who want API control |
| **Mailchimp** | Free → $13+/mo | Widely known, easy to start | Very basic sequences, non-technical users |
| **ConvertKit** | Free → $29+/mo | Creator-focused but works for simple SaaS onboarding | Simple sequences, newsletter-first approach |

### For behavioral sequences (Tier 3)

| Tool | Price | Strengths | Best for |
|---|---|---|---|
| **Customer.io** | $100+/mo | Event-driven workflows, powerful segmentation, developer-friendly | PLG companies with event tracking infrastructure |
| **Intercom** | $74+/mo | Email + in-app messaging + chat in one tool | Companies wanting a unified messaging platform |
| **Braze** | Enterprise pricing | Advanced behavioral triggers, cross-channel | Scale-stage companies with dedicated marketing ops |

**For most founders starting out:** Loops or Resend for time-based sequences. Upgrade to Customer.io when you have the event tracking infrastructure for behavioral triggers and enough volume for meaningful segments (500+ signups/month).
