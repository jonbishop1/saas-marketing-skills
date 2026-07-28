# In-App Onboarding Patterns Guide

Complete guide to in-app onboarding patterns for SaaS products. Each pattern includes: what it is, when to use it, design principles, implementation guidance, and examples for PingForge (API monitoring) and KeyScope (SEO keyword research).

---

## Table of Contents

1. [Welcome Screens](#welcome-screens)
2. [Signup Surveys (Personalization)](#signup-surveys)
3. [Onboarding Checklists](#onboarding-checklists)
4. [Empty States](#empty-states)
5. [Tooltips and Hotspots](#tooltips-and-hotspots)
6. [Guided Tours](#guided-tours)
7. [Setup Wizards](#setup-wizards)
8. [Progress Indicators](#progress-indicators)
9. [Success Celebrations](#success-celebrations)
10. [Progressive Disclosure](#progressive-disclosure)
11. [Sample Data and Sandbox Environments](#sample-data-and-sandbox-environments)
12. [Upgrade Prompts During Trial](#upgrade-prompts-during-trial)
13. [Pattern Selection by Product Complexity](#pattern-selection-by-product-complexity)

---

## Welcome Screens

### What it is
The first screen a user sees after signup. Sets expectations and drives the first action.

### When to use
Always. Every product needs a welcome screen. The only question is how complex it should be.

### Design principles
- **One primary CTA.** Not three options. One thing you want them to do next.
- **Explain the value, not the product.** "Monitor your first API endpoint" not "Welcome to PingForge's monitoring dashboard."
- **If you ask questions (personalization), limit to 1–2.** Each question reduces completion rate by 10–20%.
- **Make it dismissable.** Power users and returning evaluators will want to skip.

### Tier 1: Simple welcome

```
┌──────────────────────────────────────┐
│                                      │
│  Welcome to [Product]!               │
│                                      │
│  [One sentence: what to do first]    │
│                                      │
│  ┌────────────────────┐              │
│  │  [Primary CTA]     │              │
│  └────────────────────┘              │
│                                      │
│  Skip for now                        │
└──────────────────────────────────────┘
```

**PingForge Tier 1:**
"Welcome to PingForge! Add your first API endpoint to start monitoring. It takes about 30 seconds."
CTA: "Add your first endpoint"

**KeyScope Tier 1:**
"Welcome to KeyScope! Run your first keyword gap analysis — paste your domain and a competitor's to see what keywords you're missing."
CTA: "Run your first analysis"

### Tier 2: Welcome + personalization

```
┌──────────────────────────────────────┐
│                                      │
│  Welcome! Let's set things up        │
│  for you.                            │
│                                      │
│  What's your primary goal?           │
│  ○ Monitor API uptime                │
│  ○ Track latency performance         │
│  ○ Set up team alerting              │
│                                      │
│  ┌────────────────────┐              │
│  │  Get started        │              │
│  └────────────────────┘              │
└──────────────────────────────────────┘
```

The selected goal personalizes what they see next: different checklist items, different empty state messaging, different email sequence.

### Tier 3: Multi-step welcome with role detection

For products with multiple user types (admin vs. member, technical vs. non-technical), add a second screen that adjusts the experience. Keep it to 2 screens maximum — anything more is a setup wizard, not a welcome screen.

### Implementation
- **Custom code:** A modal component triggered on first login (check a `has_completed_welcome` flag on the user record). React/Vue modal, 2–4 hours to build.
- **Tool:** Any onboarding tool handles this. Appcues, Userflow, and Product Fruits all support welcome modals with branching.

---

## Signup Surveys

### What it is
1–3 questions asked during or immediately after signup to personalize the onboarding experience.

### When to use
When you have meaningfully different user segments that need different onboarding paths. Don't add a survey if every user gets the same experience regardless of answers.

### Questions that earn their place

| Question | Why it's worth asking | What it changes |
|---|---|---|
| **What's your role?** | Developer vs. manager need different first actions | Feature emphasis, complexity level |
| **What's your primary goal?** | Monitoring uptime vs. tracking latency suggests different starting paths | Checklist items, example data |
| **Team size?** | Solo vs. team changes collaboration features shown | Invite prompt timing, plan suggestions |
| **How did you hear about us?** | Marketing attribution | Nothing in onboarding — ask this via analytics, not the user |

**The test:** If the answer doesn't change the onboarding experience, don't ask the question. "How did you hear about us?" fails this test — it's for your analytics, not the user's benefit. Capture it via UTM parameters instead.

### Implementation
- Add fields to the signup form (simplest but adds friction to signup), or
- Show as a modal immediately after signup (preferred — doesn't block signup), or
- Embed in the welcome screen (combines two steps into one)

Store responses on the user record and use them to branch the checklist, tooltips, and email sequence.

---

## Onboarding Checklists

### What it is
A visible list of 3–7 steps the user needs to complete to be fully set up. The single most effective onboarding pattern after the welcome screen.

### When to use
When activation requires multiple steps. If activation is a single action (paste a URL, click "go"), you don't need a checklist — just drive that one action.

### Design principles
- **3–5 items for most products. 7 absolute maximum.** More than 7 feels overwhelming and users won't start.
- **First item should be pre-completed or trivially easy.** "Create your account ✓" gives a sense of progress immediately. Behavioral psychology: people are more likely to complete a list that's already partially done (endowed progress effect).
- **Each item should have a clear outcome, not just a task name.** "Set up your first monitor" not "Configure monitoring settings."
- **Persistent but not intrusive.** Visible in a sidebar, banner, or collapsible widget — not a blocking modal on every page load.
- **Link each item directly to the action.** Clicking the checklist item should navigate to the right place and ideally pre-fill or scaffold what's needed.

### PingForge checklist example

```
Get started with PingForge (2 of 5 complete)

✅ Create your account
✅ Add your first endpoint
○  Set up Slack alerts
○  Invite your team (optional)
○  Configure latency thresholds
```

Note: "Invite your team" is marked optional. Not every step needs to be required. Optional steps reduce perceived burden while still nudging toward higher activation.

### KeyScope checklist example

```
Set up KeyScope (1 of 4 complete)

✅ Create your account
○  Add your domain
○  Run your first competitor gap analysis
○  Review your keyword opportunities
```

Note: This checklist is shorter because KeyScope's value requires fewer setup steps. Don't pad the checklist to make it look thorough — keep it honest.

### Implementation
- **Custom code:** A checklist component that reads completion status from your database. Track each step as a boolean on the user record. 4–8 hours to build a basic version (collapsible sidebar widget with checkmarks and links).
- **Tool:** All major onboarding tools support checklists. This is their core feature.
- **Open-source:** React onboarding checklist components exist (e.g., `react-joyride` for tours, or build a simple checklist with state management).

### Tracking
Track checklist completion rates per step. If step 3 has a 60% drop from step 2, that's your biggest onboarding leak. Fix step 3 before optimizing anything else.

---

## Empty States

### What it is
What the user sees when a screen has no data yet. The most underutilized onboarding surface in SaaS.

### When to use
Every screen that can be empty should have a designed empty state. Dashboards, lists, reports, settings — if it can be blank, it needs a plan for blank.

### Design principles
- **Never show a truly empty screen.** A blank dashboard with column headers and no data is demoralizing. It tells the user they've done nothing and offers no guidance.
- **Answer two questions:** "What will this show when it has data?" and "What should I do to get data here?"
- **Include a CTA that creates the first item.** Empty monitor list → "Add your first endpoint." Empty analysis list → "Run your first gap analysis."
- **Consider sample data.** For complex visualizations, showing a sample dataset lets the user understand what they'll get before investing effort.

### PingForge empty state example

**Dashboard (no monitors configured):**
```
┌─────────────────────────────────────────────────┐
│                                                   │
│  📊 Your monitoring dashboard                     │
│                                                   │
│  This is where you'll see uptime, latency, and    │
│  alert history for your API endpoints.             │
│                                                   │
│  [illustration: sample dashboard with data]        │
│                                                   │
│  Add your first endpoint to start monitoring.      │
│  It takes about 30 seconds.                        │
│                                                   │
│  ┌───────────────────────┐                        │
│  │  Add first endpoint    │                        │
│  └───────────────────────┘                        │
│                                                   │
│  Or try a sample endpoint to see how it works →    │
└─────────────────────────────────────────────────┘
```

The "try a sample endpoint" link is powerful — it lets the user see the product's value before doing any real setup.

### KeyScope empty state example

**Gap analysis view (no analyses run):**
```
┌─────────────────────────────────────────────────┐
│                                                   │
│  🔍 Keyword gap analysis                          │
│                                                   │
│  See every keyword your competitors rank for       │
│  that you don't — scored by opportunity.            │
│                                                   │
│  [illustration: sample gap analysis with data]     │
│                                                   │
│  ┌───────────────────────────────────────┐        │
│  │  Your domain: [_____________.com]      │        │
│  │  Competitor:  [_____________.com]      │        │
│  │  ┌──────────────┐                     │        │
│  │  │  Run analysis  │                    │        │
│  │  └──────────────┘                     │        │
│  └───────────────────────────────────────┘        │
│                                                   │
│  Or see a sample analysis for example.com →        │
└─────────────────────────────────────────────────┘
```

Note: The empty state includes the input form directly — no extra navigation step needed. The user can start their analysis right from the empty state.

### Implementation
- Custom code for every product. Empty states are product-specific — no generic tool handles these well.
- Design time: 30–60 minutes per screen to write the copy and design the layout.
- Development: 1–2 hours per screen (conditional render based on data presence).

---

## Tooltips and Hotspots

### What it is
Small contextual hints attached to specific UI elements. Hotspots are pulsing dots that draw attention; tooltips appear on hover or click.

### When to use
To highlight features that users might miss, or to explain non-obvious UI elements. Best for discrete, contextual guidance — not for sequential instruction (use guided tours or checklists for that).

### Design principles
- **One at a time.** Multiple simultaneous tooltips create visual noise and confuse priority.
- **Dismiss permanently after interaction.** A tooltip the user has seen and dismissed should not appear again.
- **Contextual, not arbitrary.** Show a tooltip when the user is in the right context to use that feature, not on their first visit regardless of what they're doing.
- **Brief.** 1–2 sentences maximum. If you need more than that, the feature itself may need redesign.

### When tooltips work
- Highlighting a new feature for returning users
- Explaining a metric or label ("What does 'opportunity score' mean?")
- Nudging a specific action when the user is in the right context

### When tooltips fail
- As a substitute for clear UI design (if you need a tooltip to explain what a button does, rename the button)
- As a multi-step tutorial (use a checklist or setup wizard instead)
- When shown to every user regardless of need (segment — show only to users who haven't used the feature)

### Implementation
- **Tool:** This is where onboarding tools shine. Appcues, Userflow, and others let you create tooltips pointed at CSS selectors without code changes. Ideal for iteration.
- **Custom code:** Use a tooltip library (Tippy.js, Floating UI) with a user-state flag to show/dismiss. More work but more control.

---

## Guided Tours

### What it is
A sequential walkthrough that highlights multiple UI elements in order, advancing step by step.

### When to use
Sparingly. Guided tours have the lowest completion rate of any onboarding pattern — 20–30% of users complete a tour longer than 4 steps. Use only when the product has a non-obvious workflow that can't be discovered through exploration.

### Design principles
- **4 steps maximum.** Every additional step reduces completion by ~15%.
- **Let users exit at any step.** A tour that blocks the UI until completion is a prison, not a guide.
- **Interactive, not just informational.** The best tours ask the user to do something at each step ("Click here to add your first endpoint") rather than just pointing at features ("This is where your endpoints will appear").
- **Trigger contextually, not on first login.** A tour of the analytics dashboard should trigger when the user first visits the analytics dashboard, not during their first login when they have no data.

### PingForge guided tour (3 steps, triggered on first dashboard visit with data)

```
Step 1: [points to uptime chart]
"This is your uptime history for the last 24 hours. Green means all checks
passed. Red indicates a detected issue."
→ Next

Step 2: [points to latency graph]
"Your latency metrics update in real-time. The dotted line is your alert
threshold — we'll notify you when latency exceeds it."
→ Next

Step 3: [points to alert bell icon]
"All your alerts live here. Click to see the full history and configure
notification channels."
→ Got it!
```

### Implementation
- **Tool:** Guided tours are the signature feature of onboarding tools. Use one if you need tours.
- **Custom code:** Libraries like `react-joyride`, `shepherd.js`, or `intro.js` provide tour functionality. 4–8 hours to implement a basic tour.

---

## Setup Wizards

### What it is
A multi-step form that walks the user through required configuration. Different from a guided tour — a wizard is a doing flow, not a showing flow.

### When to use
When the product requires multiple configuration steps before it can deliver value, and those steps have a natural sequence.

### Design principles
- **Show progress.** Step 2 of 4, with a visual progress bar. Users need to know how much effort remains.
- **Allow saving and returning.** If the wizard takes more than 5 minutes, users will leave partway through. Let them resume where they left off.
- **Validate as you go.** Don't let users reach step 4 only to discover step 2 had an error.
- **Show value at the earliest possible step.** If step 3 produces a preview of results, show that preview before requiring step 4.

### PingForge setup wizard (not needed — too simple)

PingForge's setup is a single action (paste a URL). A wizard would over-engineer this. Use the empty state with an inline form instead.

### KeyScope setup wizard (optional — for multi-domain setup)

```
Step 1: Add your domain
[domain input field]
"We'll use this to find keywords you already rank for."
→ Next

Step 2: Add 1-3 competitors
[competitor domain fields]
"We'll compare their keyword rankings against yours."
→ Next

Step 3: Review and run
[summary of domains entered]
"We'll analyze keyword gaps across these domains. This usually takes 1-2 minutes."
→ Run analysis

[Loading state with progress indicator]
```

### Implementation
- Almost always custom code, because wizards interact with your product's actual configuration.
- Use a multi-step form pattern with state management. Most UI frameworks have step/wizard components.
- Track completion rate per step to identify where users drop off.

---

## Progress Indicators

### What it is
Visual feedback showing how far the user has progressed through setup or toward activation.

### Implementations
- **Checklist with completion count** — "3 of 5 steps complete"
- **Progress bar** — visual bar filling as steps complete
- **Percentage** — "Your account is 60% set up"
- **Milestone markers** — visual markers on a journey map

### Design principles
- Start above 0%. Even "create account" as a pre-completed step gets the bar to 20%. This leverages endowed progress.
- Make progress visible without being intrusive. A persistent banner or sidebar section works. A blocking modal does not.
- Celebrate milestones — see Success Celebrations below.

---

## Success Celebrations

### What it is
Positive feedback when the user completes an important action, especially the activation action.

### Design principles
- **Celebrate the outcome, not the action.** "Your first monitor is live! You'll get alerts within 30 seconds of any issue." not "You created a monitor."
- **Brief and non-blocking.** A toast notification, a confetti animation, or a subtle success state. Not a modal that requires dismissal.
- **Include the next step.** "Your first monitor is live! Next: set up Slack alerts so your team gets notified." Turn every celebration into a nudge toward the next action.
- **Don't overdo it.** Celebrate the activation moment and maybe 1–2 key milestones. Celebrating every minor action feels patronizing.

---

## Progressive Disclosure

### What it is
Showing only the features and complexity the user needs right now, and revealing more as they mature.

### When to use
Products with broad feature sets where showing everything on day 1 would overwhelm new users.

### Implementation patterns

**Feature gating by experience:**
- New users see a simplified dashboard with core features
- After activation milestone, reveal secondary features
- After power-user milestone, unlock advanced features

**Contextual feature introduction:**
- Surface a feature when the user's behavior suggests they need it
- PingForge: Show "Team alerting" features only when a user has 5+ monitors (suggests team use)
- KeyScope: Show "Bulk keyword import" only after the user has run 3+ manual analyses

**Menu/navigation evolution:**
- Day 1: Show 4 core navigation items
- Week 2 (post-activation): Reveal 2 additional items with a "New" badge
- Month 2: Full navigation visible

---

## Sample Data and Sandbox Environments

### What it is
Pre-loaded data or a demo environment that shows the product's value before the user invests setup effort.

### When to use
When the product's value is hard to understand without data, and the setup to get real data takes time.

### Patterns

**Pre-loaded sample data:**
- PingForge: A "demo endpoint" that's pre-configured and already has 24 hours of monitoring data. The user sees a working dashboard immediately.
- KeyScope: A sample gap analysis for "example.com vs competitor.com" with real-looking (but clearly labeled as sample) data.

**Interactive sandbox:**
- A fully functional demo environment the user can explore without setting up real data.
- Clearly labeled as sample data to avoid confusion.
- CTA to "Use your own data" when the user is ready.

**"Try it" inline:**
- A simplified version of the core action available without full account setup.
- KeyScope: A free, limited gap analysis on the landing page that produces real results, prompting signup for full access.

### Implementation
- Sample data: Pre-seed the user's account with demo data. Flag it as sample data in the UI. Allow dismissal/deletion when the user adds real data.
- Sandbox: More complex — requires a demo data layer that doesn't interfere with real usage. Usually a feature flag that swaps data sources.

---

## Upgrade Prompts During Trial

### What it is
Contextual nudges that remind trial users of the paid value, timed to moments when they're experiencing value or hitting limits.

### Design principles
- **Trigger on usage, not time.** An upgrade prompt after the user hits a usage limit is 10× more effective than one on day 7.
- **Show value gained, not features locked.** "You've monitored 47 endpoints and caught 3 incidents. Keep your monitoring active — upgrade before your trial ends." not "Your trial expires in 5 days."
- **Non-blocking.** Upgrade prompts should never prevent the user from continuing to use the product during the trial. Blocking prompts create resentment, not conversions.
- **Acknowledge the path.** "You've completed 4 of 5 setup steps — you're getting real value from KeyScope. Plans start at $49/month to keep your data and continue finding keyword opportunities."

---

## Pattern Selection by Product Complexity

### Low complexity (PingForge-type: 1–2 steps to value)

**Use:**
- Welcome screen (Tier 1: simple, one CTA)
- Empty state with inline action form
- Success celebration on activation
- Trial expiry emails

**Skip:**
- Checklist (unnecessary — there's only one step)
- Guided tour (nothing to tour before data exists)
- Setup wizard (one action doesn't need a wizard)

### Medium complexity (KeyScope-type: 3–5 steps to value)

**Use:**
- Welcome screen (Tier 2: with 1 personalization question)
- Onboarding checklist (3–5 items)
- Empty states on all key screens
- Tooltips on 2–3 non-obvious features
- Success celebrations at activation + key milestones
- Full email sequence

**Consider:**
- Sample data / demo analysis (high impact, medium effort)
- Setup wizard (if the steps have a strict sequence)
- Progressive disclosure (if feature set is broad)

### High complexity (enterprise tools: many steps, team involvement)

**Use:**
- Welcome screen (Tier 2–3: role detection + personalization)
- Onboarding checklist (5–7 items, with optional items marked)
- Setup wizard for initial configuration
- Empty states on all screens
- Guided tour of the main workflow (contextual, not on first login)
- Progressive disclosure
- Full email sequence with behavioral triggers
- Human check-in triggers for sales-assist

**Consider:**
- Sandbox environment
- Video walkthroughs embedded in empty states
- Team onboarding flow (admin sets up, then invites team with role-appropriate onboarding)
