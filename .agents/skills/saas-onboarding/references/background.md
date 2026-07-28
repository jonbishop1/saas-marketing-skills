# Background: Onboarding Intake Questions

Read this before advising. Gather missing background rather than giving generic recommendations. Many questions have safe defaults for software — noted below so you don't ask for information the user doesn't have yet.

---

## Questions to Ask

**Product & value**
- What does the product do in one sentence?
- What's the core action a user must take to experience value? (This becomes the activation metric candidate)
- How long does it typically take a new user to get to that action? (Minutes, hours, days?)
- What setup is required before the core action is possible? (Account config, data import, integration, team invite?)

**Current onboarding state**
- What happens after a user signs up right now? Walk me through it step by step.
- Do you have any onboarding in place? (Welcome screen, checklist, email sequence, tooltip tour, nothing?)
- Do you know where users drop off? *(Safe default: they don't know — help them figure it out)*
- What's your rough signup-to-activation rate? *(Okay if unknown — even a guess helps)*
- What's your trial-to-paid conversion rate? *(Safe default: unknown)*

**Trial & pricing model**
- What's the current model? (Free trial, freemium, reverse trial, paid only, demo-first?)
- If free trial: how long? Credit card required? *(Safe default: 14 days, no CC)*
- If freemium: what's gated? (Features, usage limits, team size, integrations?)
- Have they considered changing their model? What are their concerns?

**GTM motion**
- How do users typically sign up? (Self-serve from website, after a demo, from a sales conversation, invitation?)
- Is there any human involvement in onboarding currently? (Sales, CS, founder doing onboarding calls?)
- For team products: does one person sign up and invite others, or does the team join together?

**User types**
- Who are the primary users? (Developers, marketers, managers, executives?)
- Are there multiple user types with different needs? *(If yes: does everyone go through the same onboarding?)*
- Technical vs. non-technical users? *(Affects complexity tolerance and guidance style)*

**Resources & tools**
- What's the tech stack for the frontend? (React, Vue, Angular, etc. — affects implementation options)
- Any onboarding tools currently in use? (Appcues, Userflow, Intercom tours, etc.)
- Email tool? (Sendgrid, Customer.io, Intercom, Mailchimp, etc.)
- Analytics tool? (Mixpanel, Amplitude, PostHog, GA4, none?) *(Reference `saas-data-analysis` if they need analytics setup)*
- How much time can they dedicate to building/improving onboarding?
- Budget for onboarding tools?

**Competitive landscape**
- Have they signed up for competitors' products? What's the onboarding experience like?
- What do competitors do well in onboarding?
- What do competitors do poorly?

---

## Safe Defaults (don't ask, just apply)

| Parameter | Default |
|---|---|
| Trial model | 14-day free trial, no CC required |
| Activation metric | Best guess from product intuition; validate with data later |
| Onboarding tool | Custom code for Tier 1; tool for Tier 2+ |
| Email sequence | Welcome + trial expiry as minimum |
| Segmentation | None until 500+ signups/month |
| A/B testing | Not until 200+ signups/month |
| Analytics | Basic event tracking on signup + activation action |

---

## Routing After Intake

| Situation | Where to go |
|---|---|
| Pre-launch, no users | SKILL.md → Pre-Launch: Speed to Ship. Stop there. |
| No onboarding exists | SKILL.md → Situation Assessment → Journey Map → Tiered Execution Plan |
| Onboarding exists, underperforms | SKILL.md → Diagnosing Onboarding Failures → fix the specific leak |
| Wants to choose/change trial model | SKILL.md → Trial Model Strategy → references/trial-strategy-guide.md |
| Wants to build in-app flows | SKILL.md → PLG Onboarding → references/in-app-patterns-guide.md |
| Needs email sequence design | SKILL.md → Onboarding Emails → reference `saas-copywriting` for copy |
| Needs activation metric help | SKILL.md → Defining Activation Metric → reference `saas-data-analysis` |
| Sales-led onboarding | SKILL.md → Sales-Assisted Onboarding section |
| Wants to evaluate/buy a tool | SKILL.md → Implementation → references/trial-strategy-guide.md tool section |
