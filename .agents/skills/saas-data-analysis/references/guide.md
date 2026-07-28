# SaaS Product & Marketing Analytics: Complete Reference Guide

---

## Table of Contents

1. [GA4 Setup & Configuration](#ga4-setup--configuration)
2. [Google Tag Manager (GTM)](#google-tag-manager-gtm)
3. [Product Analytics Tools — Deep Dive](#product-analytics-tools--deep-dive)
4. [Event Taxonomy Design](#event-taxonomy-design)
5. [Marketing-Product Connection — Implementation](#marketing-product-connection--implementation)
6. [Metric Definitions & Benchmarks](#metric-definitions--benchmarks)
7. [Dashboard Templates](#dashboard-templates)
8. [Session Recording Tools](#session-recording-tools)
9. [Data Infrastructure (Tier 3)](#data-infrastructure-tier-3)
10. [Analysis Techniques](#analysis-techniques)

---

## GA4 Setup & Configuration

### Tier 1 — Basic Install (15 minutes)

**Step 1: Create GA4 property**
Google Analytics → Admin → Create Property. Choose "Web" as the platform. You'll get a Measurement ID (format: G-XXXXXXXXXX).

**Step 2: Install the tag**
For most SaaS marketing sites and apps, add the gtag.js snippet to your `<head>`:

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

For SPAs (React, Next.js, Vue), you'll need to send page_view events manually on route changes. Most frameworks have a GA4 integration or wrapper for this.

**Step 3: Set up 3–5 conversion events**
Go to Admin → Events → Mark as conversion. Start with:
- `sign_up` (use GA4's recommended event name)
- Your activation event (custom event)
- `purchase` or upgrade event (custom event)

**Step 4: Set data retention to 14 months**
Admin → Data Settings → Data Retention → change from 2 months to 14 months. Without this, you lose detailed data after 2 months.

**Step 5: Enable Google Signals**
Admin → Data Settings → Data Collection → turn on Google Signals. This enables cross-device tracking and demographic data.

### Tier 2 — GTM-Managed GA4

At Tier 2, move GA4 event management into GTM (see GTM section below). This means:
- Remove the hardcoded gtag.js snippet
- Install GA4 via GTM's GA4 Configuration tag
- Define events as GTM triggers → GA4 Event tags
- Use the data layer for structured event data

### Tier 3 — GA4 + BigQuery

Enable BigQuery export for raw event data. This gives you SQL access to every event, enabling analysis that GA4's UI can't do.

Admin → BigQuery Linking → Link to your GCP project. Events stream to BigQuery daily (free export) or in near-real-time (streaming export, costs money).

**When BigQuery export is worth it:**
- GA4's UI can't answer your questions (complex segmentation, custom attribution)
- You want to join analytics data with your product database
- You need data retention beyond 14 months
- You want to build custom dashboards in a BI tool

**When it's not worth it:**
- You don't have someone comfortable writing SQL
- You have < 1,000 users (not enough data to justify the infrastructure)
- GA4's built-in reports answer your questions adequately

### GA4 Custom Events

GA4 events have a name and up to 25 custom parameters. Use recommended event names where they fit (Google's documentation lists these), and custom events for product-specific actions.

```javascript
// Recommended event — sign up
gtag('event', 'sign_up', {
  method: 'email'  // or 'google', 'github', etc.
});

// Custom event — activation action
gtag('event', 'first_monitor_configured', {
  monitor_type: 'http',
  setup_time_seconds: 120
});

// Custom event — upgrade
gtag('event', 'purchase', {
  value: 49.00,
  currency: 'USD',
  plan: 'pro_monthly'
});
```

**Important limitation:** GA4 custom dimensions must be registered in Admin → Custom Definitions before they appear in reports. You get 50 event-scoped and 25 user-scoped custom dimensions on the free tier. Plan your taxonomy before you instrument — changing event structures later is painful.

### UTM Parameter Standards

Every link you control should have UTM parameters. Without them, GA4 lumps traffic into "(direct)" or "(not set)."

```
https://yourapp.com/?utm_source=reddit&utm_medium=social&utm_campaign=devops_post_march
https://yourapp.com/?utm_source=google&utm_medium=cpc&utm_campaign=api_monitoring_brand
https://yourapp.com/?utm_source=newsletter&utm_medium=email&utm_campaign=weekly_digest_42
```

**Standard UTM parameters:**

| Parameter | Required | Purpose | Example values |
|---|---|---|---|
| utm_source | Yes | Where the traffic comes from | google, reddit, twitter, newsletter, producthunt |
| utm_medium | Yes | How it gets to you | cpc, social, email, referral, organic |
| utm_campaign | Yes | Which specific effort | brand_search, devops_post_q1, welcome_sequence |
| utm_content | Optional | Differentiate creatives or links | hero_cta, sidebar_link, footer_banner |
| utm_term | Optional | Paid keyword (usually auto-tagged) | api_monitoring_tool |

**Naming conventions matter.** `Reddit` and `reddit` are different sources in GA4. Pick a convention (lowercase, underscores, no spaces) and enforce it. Document it in a shared spreadsheet if anyone else creates links.

---

## Google Tag Manager (GTM)

### When to Introduce GTM

**Don't use GTM at Tier 1.** Direct gtag.js or SDK installation is simpler and faster when you have fewer than 10 events and no ad platform pixels.

**Introduce GTM at Tier 2 when:**
- You're adding multiple tools (GA4 + product analytics + ad pixels)
- You have 10+ events to manage
- You want to modify tracking without code deploys
- Multiple people need to configure tracking

### Core GTM Concepts

```
Container       → a JavaScript snippet installed on your site
Tags            → code that fires (GA4 event, Mixpanel track call, ad pixel)
Triggers        → conditions that cause tags to fire (page load, click, custom event)
Variables       → dynamic values used in tags/triggers (page URL, click text, data layer values)
Data Layer      → a JavaScript object where your app pushes structured data for GTM to read
```

### Implementation Pattern for SaaS

**Step 1: Install the GTM container snippet**
Add the container code to every page (two snippets — one in `<head>`, one after `<body>`).

**Step 2: Set up the data layer**
Your app pushes events to the data layer. GTM reads them and routes to the appropriate tools.

```javascript
// Your app code pushes events to the data layer
window.dataLayer = window.dataLayer || [];

// On signup
dataLayer.push({
  event: 'user_signed_up',
  user_id: 'user_123',
  signup_method: 'email',
  utm_source: getUtmSource(),
  utm_medium: getUtmMedium()
});

// On activation
dataLayer.push({
  event: 'first_monitor_configured',
  monitor_type: 'http',
  time_to_activate_hours: 2.5
});
```

**Step 3: Create tags for each destination**
In GTM, create a GA4 Event tag triggered by the `user_signed_up` data layer event. Create a separate tag for Mixpanel/Amplitude/PostHog if you're sending the same event to multiple tools.

**Step 4: Preview and debug**
GTM's Preview mode shows exactly which tags fired on each page, with which data. Use this before publishing — broken tracking is worse than no tracking.

### GTM for SPA (Single Page Applications)

SPAs don't have traditional page loads. You need to push virtual pageview events to the data layer on route changes.

```javascript
// React Router example
useEffect(() => {
  dataLayer.push({
    event: 'virtual_pageview',
    page_path: location.pathname,
    page_title: document.title
  });
}, [location]);
```

Create a GTM trigger on the `virtual_pageview` data layer event, and use it to fire your GA4 page_view tag.

---

## Product Analytics Tools — Deep Dive

### PostHog

**Best for:** Early-stage startups wanting an all-in-one tool (analytics + session recording + feature flags), teams that want to self-host, privacy-conscious products.

**Free tier:** 1 million events/month, 5,000 session recordings/month (cloud). Unlimited on self-hosted.

**Key setup:**

```javascript
// Install
import posthog from 'posthog-js';
posthog.init('YOUR_PROJECT_KEY', { api_host: 'https://app.posthog.com' });

// Identify user (critical for marketing-product connection)
posthog.identify(userId, {
  email: user.email,
  plan: user.plan,
  signup_source: getUtmSource(),
  company_size: user.companySize
});

// Track event
posthog.capture('first_monitor_configured', {
  monitor_type: 'http',
  setup_time_seconds: 120
});
```

**Strengths:** Open source, generous free tier, session recording included, feature flags included, self-hostable for compliance requirements, autocapture available (but manual events are better).

**Weaknesses:** Retention and funnel analysis UI not as polished as Mixpanel. Autocapture data can be noisy. Self-hosting requires infrastructure maintenance.

**Tiered approach:**

| Level | PostHog setup |
|---|---|
| Good | Cloud free tier, 5–10 manual events, basic funnels | 
| Better | Add user identification + properties, session recording on key flows, custom dashboards |
| Best | Self-hosted for compliance, server-side SDK, group analytics for B2B accounts |

### Mixpanel

**Best for:** Event-driven SaaS products with clear user flows, teams that want the best funnel and retention analysis UI.

**Free tier:** 20 million events/month. Extremely generous — most startups never outgrow it.

**Key setup:**

```javascript
// Install
import mixpanel from 'mixpanel-browser';
mixpanel.init('YOUR_PROJECT_TOKEN');

// Identify user
mixpanel.identify(userId);
mixpanel.people.set({
  $email: user.email,
  plan: user.plan,
  signup_source: getUtmSource(),
  company_size: user.companySize,
  created_at: user.createdAt
});

// Track event
mixpanel.track('First Monitor Configured', {
  monitor_type: 'http',
  setup_time_seconds: 120
});
```

**Strengths:** Best-in-class funnel analysis (conversion rates, time between steps, drop-off analysis). Excellent retention analysis (any event as starting/returning event). Generous free tier. JQL for custom queries.

**Weaknesses:** No session recording (need a separate tool). No feature flags. Hosted only — can't self-host. Data governance tools are paid-tier features.

**Tiered approach:**

| Level | Mixpanel setup |
|---|---|
| Good | Free tier, 5–10 events, basic funnel report |
| Better | User identification + properties, retention analysis, saved reports |
| Best | Group analytics (B2B account-level analysis), custom formulas, data pipelines |

### Amplitude

**Best for:** Products needing behavioral cohorts and segmentation, larger teams with multiple analysts, companies building sophisticated user journey analysis.

**Free tier:** 50,000 Monthly Tracked Users (MTUs). Note: this counts unique users, not events — a user sending 500 events counts as 1 MTU.

**Key setup:**

```javascript
// Install
import * as amplitude from '@amplitude/analytics-browser';
amplitude.init('YOUR_API_KEY');

// Identify user
const identifyEvent = new amplitude.Identify();
identifyEvent.set('plan', user.plan);
identifyEvent.set('signup_source', getUtmSource());
identifyEvent.set('company_size', user.companySize);
amplitude.identify(identifyEvent);
amplitude.setUserId(userId);

// Track event
amplitude.track('First Monitor Configured', {
  monitor_type: 'http',
  setup_time_seconds: 120
});
```

**Strengths:** Strong behavioral cohort builder (find users who did X but not Y within Z days). Good for segmentation-heavy analysis. Notebooks feature for combining analysis with documentation. North Star Metric framework built into the product.

**Weaknesses:** Free tier is MTU-based — can get expensive faster than Mixpanel's event-based pricing. UI has a steeper learning curve. Some powerful features (behavioral cohorts, predictions) are paid-tier only.

**Tiered approach:**

| Level | Amplitude setup |
|---|---|
| Good | Free tier, 5–10 events, basic charts and funnels |
| Better | User properties, behavioral cohorts, taxonomy planning |
| Best | Amplitude CDP for identity, group analytics, Amplitude Experiment for A/B testing |

### Heap

**Best for:** Teams that want analytics without manual instrumentation, products where retroactive analysis is valuable.

**Free tier:** 10,000 sessions/month.

**Key concept:** Heap auto-captures every click, form submission, page view, and field change. You then define events retroactively by pointing at elements in the UI ("this button click = 'Signed Up'").

**Strengths:** Near-zero instrumentation effort. Retroactive event definition — you can define events today that apply to data captured last month. Good for teams without engineering bandwidth for instrumentation.

**Weaknesses:** Auto-captured data is noisy and less structured than deliberately instrumented events. Event definitions can break when the UI changes (button text, CSS classes). Not ideal for API-heavy products where important actions happen server-side. Free tier is small.

**When Heap makes sense vs. manual instrumentation:**

| Situation | Heap | Manual instrumentation |
|---|---|---|
| Solo founder, no time for tracking code | Better — get data now, clean up later | Worse — tracking code delays launch |
| API product where key events are server-side | Worse — Heap can't auto-capture backend events | Better — instrument server-side events directly |
| Rapidly changing UI | Worse — event definitions break on UI changes | Better — events tied to business logic, not UI elements |
| Need retroactive analysis | Better — data already captured | Worse — can't analyze events you didn't track |

### Pendo

**Best for:** Product-led growth teams that want analytics and in-app guides in one tool. B2B SaaS with onboarding flows that need guidance.

**Free tier:** Up to 500 monthly active users.

**Key concept:** Pendo combines product analytics with in-app messaging (tooltips, guides, walkthroughs, announcements). It auto-captures feature usage and page views, and lets you build guided tours without code.

**When Pendo makes sense:**
- You're losing users in onboarding and want to build guided flows
- You want to combine "what users do" with "let's guide them to do the right thing"
- You're B2B and need account-level analytics + NPS surveys

**When it doesn't:**
- You just need analytics (Mixpanel/PostHog are better for pure analytics)
- You have > 500 MAUs and no budget (paid tiers are enterprise-priced)
- You need deep funnel/retention analysis (Pendo's analytics are competent but not best-in-class)

---

## Event Taxonomy Design

A clean event taxonomy is the difference between analytics you use and analytics you abandon. Define naming conventions before you instrument.

### Naming Conventions

**Event names — use Object + Action format:**
```
monitor_created        (not "created_monitor" or "Create Monitor" or "createMonitor")
keyword_searched       (not "search" or "did_search" or "Search Performed")
alert_configured
report_exported
plan_upgraded
team_member_invited
```

**Why Object + Action:** It groups naturally. All monitor events start with `monitor_`. All alert events start with `alert_`. This makes filtering, searching, and building funnels intuitive.

**Property names — use snake_case, be specific:**
```
monitor_type: "http"           (not "type" — too generic)
search_query_length: 3         (not "length")  
plan_name: "pro_monthly"       (not "plan" — is it the name, the price, the ID?)
time_to_activate_hours: 2.5
```

### Event Schema Template

For each event, document:

```
Event: monitor_created
Description: User creates a new monitor for an endpoint
When it fires: After successful monitor creation (not on form open)
Properties:
  - monitor_type (string): "http", "tcp", "dns", "heartbeat"
  - endpoint_url (string): the monitored URL (hash if sensitive)
  - check_interval_minutes (integer): 1, 5, 15, 30, 60
  - is_first_monitor (boolean): true if this is the user's first monitor
Sent to: PostHog, GA4 (as custom event)
Added in: v1.0
```

### Common Mistakes in Event Design

**Tracking UI interactions instead of business outcomes.** `button_clicked` with a property of `button_name: "save"` is almost useless. `keyword_list_saved` with `keyword_count: 15` is actionable.

**Too many events too early.** 50 events with no one analyzing them is worse than 10 events that you check weekly. Start with 5–10 events that map to your AARRR funnel stages.

**Inconsistent naming.** `SignUp`, `sign_up`, `signed_up`, `user_signup` — if these coexist in your data, your funnels break. Pick a convention, document it, enforce it.

**Not including context properties.** `plan_upgraded` is useful. `plan_upgraded` with `old_plan: "free"`, `new_plan: "pro"`, `upgrade_trigger: "limit_reached"` is 10x more useful. Plan properties up front.

---

## Marketing-Product Connection — Implementation

### Tier 1 — Cookie-Based UTM Capture

The simplest approach: capture UTM parameters on landing and persist them to signup.

```javascript
// utm-capture.js — include on every page

function captureUtmParams() {
  const params = new URLSearchParams(window.location.search);
  const utmKeys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'];
  
  utmKeys.forEach(key => {
    const value = params.get(key);
    if (value) {
      // Store as first-touch (don't overwrite if already set)
      if (!getCookie(`first_${key}`)) {
        setCookie(`first_${key}`, value, 90); // 90-day expiry
      }
      // Always update last-touch
      setCookie(`last_${key}`, value, 30); // 30-day expiry
    }
  });
  
  // Also capture landing page
  if (!getCookie('first_landing_page')) {
    setCookie('first_landing_page', window.location.pathname, 90);
  }
}

function getAttributionData() {
  return {
    first_touch_source: getCookie('first_utm_source') || 'direct',
    first_touch_medium: getCookie('first_utm_medium') || 'none',
    first_touch_campaign: getCookie('first_utm_campaign') || 'none',
    first_landing_page: getCookie('first_landing_page') || '/',
    last_touch_source: getCookie('last_utm_source') || 'direct',
    last_touch_medium: getCookie('last_utm_medium') || 'none',
    last_touch_campaign: getCookie('last_utm_campaign') || 'none',
  };
}

// Call on every page load
captureUtmParams();
```

```javascript
// On signup — send attribution data to your product analytics tool
const attribution = getAttributionData();

// PostHog example
posthog.identify(userId, {
  ...attribution,
  signup_date: new Date().toISOString(),
  plan: 'free'
});

// Mixpanel example
mixpanel.identify(userId);
mixpanel.people.set({
  ...attribution,
  signup_date: new Date().toISOString(),
  plan: 'free'
});
```

**Limitations:** Client-side only — ad blockers may prevent cookie setting. Cross-subdomain requires cookie domain configuration. No server-side validation. Good enough for Tier 1 and early Tier 2.

### Tier 2 — Server-Side Enrichment

On signup, your backend receives the attribution data from the client and stores it in your database alongside the user record. This is more reliable than client-side only.

```javascript
// Backend — on user creation
async function createUser(userData, attributionData) {
  const user = await db.users.create({
    ...userData,
    first_touch_source: attributionData.first_touch_source,
    first_touch_medium: attributionData.first_touch_medium,
    first_touch_campaign: attributionData.first_touch_campaign,
    first_landing_page: attributionData.first_landing_page,
    last_touch_source: attributionData.last_touch_source,
    last_touch_medium: attributionData.last_touch_medium,
    last_touch_campaign: attributionData.last_touch_campaign,
  });
  
  // Send enriched identify call from server (more reliable)
  analytics.identify({
    userId: user.id,
    traits: {
      email: user.email,
      plan: user.plan,
      ...attributionData,
      created_at: user.createdAt
    }
  });
  
  return user;
}
```

**What this enables:** You can now query your own database to answer "what's the retention rate of users from Google Ads vs. organic search?" without depending solely on the analytics tool.

### Tier 3 — CDP-Managed Identity

At Tier 3, a CDP (Segment or Rudderstack) handles identity resolution and event routing.

**Segment setup:**

```javascript
// Client-side — Segment's analytics.js replaces individual tool SDKs
analytics.identify(userId, {
  email: user.email,
  plan: user.plan,
  company: user.company
});

analytics.track('Monitor Created', {
  monitor_type: 'http',
  is_first_monitor: true
});
```

Segment routes these calls to all connected destinations (GA4, Mixpanel, Amplitude, your warehouse) with consistent identity and properties. You instrument once, Segment distributes everywhere.

**Rudderstack** is the open-source alternative. Same concept, self-hostable, often cheaper at scale.

**When a CDP is justified:**
- You're sending events to 3+ destinations
- Identity stitching across platforms is breaking
- You need server-side event reliability
- You want a warehouse as your single source of truth
- You have engineering capacity to set up and maintain it

**When it's not justified:**
- You have 1–2 analytics tools (just use their SDKs directly)
- You don't have a data warehouse
- You have < 1,000 users (the complexity isn't worth it)

---

## Metric Definitions & Benchmarks

### Core SaaS Metrics

| Metric | Definition | How to calculate | Alert threshold |
|---|---|---|---|
| **Signup rate** | Visitors who create an account | Signups / unique visitors | Drop > 20% week-over-week |
| **Activation rate** | Signups who hit the activation event | Activated users / signups (within activation window) | Below 25% for PLG products |
| **Day-1 retention** | Users who return the day after signup | Users active on day 1 / signups on day 0 | Below 20% |
| **Week-1 retention** | Users active in their second week | Users active in week 1 / signups in week 0 | Below 15% |
| **Month-1 retention** | Users active in their second month | Users active in month 1 / signups in month 0 | Below 10% |
| **Trial-to-paid** | Trial users who convert to paid | Paid conversions / trial starts | Below 3% for self-serve |
| **MRR** | Monthly recurring revenue | Sum of all active subscription amounts | Declining for 2+ months |
| **Churn rate** | Customers lost per period | Churned customers / starting customers | Above 5% monthly for SMB |
| **Expansion revenue** | Revenue growth from existing customers | Upgrades + seat additions - downgrades | Negative = net contraction |
| **CAC** | Cost to acquire a customer | Total sales + marketing spend / new customers | Rising without LTV improvement |
| **LTV** | Predicted lifetime revenue per customer | ARPU / monthly churn rate | LTV:CAC ratio below 3:1 |

### Benchmarks by Product Type

These are rough benchmarks from publicly available data. Your numbers will vary — the trend matters more than the absolute value.

**API / Developer tool:**

| Metric | Median | Good | Great |
|---|---|---|---|
| Visitor → signup | 2–5% | 5–10% | 10%+ |
| Signup → activation (7-day) | 20–30% | 30–50% | 50%+ |
| Week-4 retention | 15–25% | 25–40% | 40%+ |
| Trial → paid | 3–7% | 7–15% | 15%+ |
| Monthly churn (paid) | 5–8% | 3–5% | < 3% |

**SEO / Marketing SaaS:**

| Metric | Median | Good | Great |
|---|---|---|---|
| Visitor → signup | 3–7% | 7–12% | 12%+ |
| Signup → activation (7-day) | 25–40% | 40–60% | 60%+ |
| Week-4 retention | 10–20% | 20–35% | 35%+ |
| Trial → paid | 2–5% | 5–10% | 10%+ |
| Monthly churn (paid) | 6–10% | 4–6% | < 4% |

**Important:** Don't compare yourself to "great" benchmarks when you're at Tier 1. First, make sure you can measure. Then, make sure the metric is trending in the right direction. Absolute values come later.

---

## Dashboard Templates

### Tier 1 Dashboard — The Essentials (5 charts)

```
1. Weekly signups (line chart, 12 weeks)
   → Are we growing?

2. Signup → activation funnel (funnel chart)
   → Where are users dropping off?

3. Activation rate by week (line chart, 12 weeks)
   → Is our onboarding improving?

4. Weekly active users (line chart, 12 weeks)
   → Are users coming back?

5. Top acquisition channels by signup count (bar chart)
   → Where are users coming from?
```

This dashboard takes 30 minutes to build in any product analytics tool. It answers the five most basic questions. Don't add more charts until you're regularly acting on these five.

### Tier 2 Dashboard — Acquisition Quality (8–10 charts)

Everything from Tier 1, plus:

```
6. Activation rate by acquisition channel (grouped bar chart)
   → Which channels produce users who actually activate?

7. Week-4 retention by acquisition channel (grouped bar chart)
   → Which channels produce users who stick around?

8. Time to activate by channel (box plot or average line chart)
   → Do some channels produce users who need more onboarding help?

9. MRR over time (line chart, trailing 12 months)
   → Revenue trend

10. Trial-to-paid conversion by cohort (line chart)
    → Is our conversion improving over time?
```

### Tier 3 Dashboard — Operational (add per-team views)

Everything from Tier 2, plus team-specific views:

**Marketing dashboard:** CAC by channel, LTV:CAC ratio, channel-level ROAS, signup → paid conversion by channel.

**Product dashboard:** Feature adoption rates, activation funnel with segment filters, retention curves by plan type, usage frequency distribution.

**Executive dashboard:** MRR, net revenue retention, CAC payback period, runway (if applicable).

---

## Session Recording Tools

### Quick Comparison

| Tool | Free tier | Key differentiator |
|---|---|---|
| **PostHog** | 5,000 recordings/mo | Integrated with PostHog analytics — filter recordings by event |
| **Microsoft Clarity** | Unlimited | Completely free, includes heatmaps, lightweight |
| **Hotjar** | 35 sessions/day | Includes surveys and feedback widgets alongside recordings |
| **FullStory** | 1,000 sessions/mo | Best search and filtering — find sessions by frustration signals |

**Recommendation:** If you're already using PostHog, use its built-in recording. If not, start with Microsoft Clarity (free, no limits). Move to Hotjar or FullStory only if you need advanced filtering or built-in surveys.

### When to Watch Session Recordings

Don't watch random sessions — that's a time sink with no return. Watch recordings when you have a specific question:

- "Why do 40% of users drop off at step 3 of onboarding?" → Filter to sessions that reached step 2 but not step 3
- "Why are users from paid ads activating at lower rates?" → Filter to sessions where signup_source = paid
- "Users report confusion on the pricing page" → Filter to sessions that visited /pricing and did NOT sign up

Most tools let you filter sessions by events, pages visited, or user properties. Use this aggressively.

---

## Data Infrastructure (Tier 3)

This section covers tools for mature analytics stacks. Don't build this until you've exhausted what GA4 + a product analytics tool can do.

### Customer Data Platform (CDP)

**What a CDP does:** Routes events from your app to multiple analytics tools and your data warehouse. Handles identity resolution. Provides a single API for all tracking.

| CDP | Pricing model | Self-hostable | Best for |
|---|---|---|---|
| **Segment** | MTU-based (free up to 1,000 MTUs) | No | Teams already in the Twilio/Segment ecosystem |
| **Rudderstack** | Event-based (free tier available) | Yes | Teams that want open-source, control, or lower cost at scale |

**Architecture with a CDP:**

```
Your app → CDP (Segment/Rudderstack)
              ├→ GA4 (marketing analytics)
              ├→ Mixpanel/Amplitude/PostHog (product analytics)
              ├→ Data warehouse (BigQuery/Snowflake)
              ├→ Ad platforms (Google Ads, Meta — for conversion events)
              └→ CRM (HubSpot, Salesforce — for user enrichment)
```

### Data Warehouse

**What it does:** Stores all your raw event data in a SQL-queryable format. Becomes your single source of truth when you outgrow individual tool capabilities.

| Warehouse | Free tier | Best for |
|---|---|---|
| **BigQuery** | 1 TB queries/mo, 10 GB storage | GA4 users (native export), pay-per-query pricing |
| **Snowflake** | $400 credit trial | Heavy query workloads, multi-cloud |
| **Redshift** | None (but cheap small instances) | AWS-native teams |

**When you need a warehouse:**
- Analytics tools can't answer your questions (complex joins, custom attribution models)
- You need to combine analytics data with product database data
- Data retention in analytics tools is insufficient
- Multiple teams need different views of the same data

### BI Layer

**What it does:** Connects to your warehouse and lets non-SQL users build dashboards and explore data.

| BI tool | Free/Open source | Best for |
|---|---|---|
| **Metabase** | Open source (self-host free) | Startups wanting self-hosted BI with SQL + visual query builder |
| **Looker Studio** | Free | Teams using BigQuery, Google-native |
| **Tableau** | Paid (free Public version) | Enterprise, complex visualization needs |

**Recommendation:** Metabase (self-hosted) for most startups — it's free, connects to any SQL database, and has a visual query builder that non-technical teammates can use.

---

## Analysis Techniques

### Funnel Analysis

Funnel analysis measures conversion between sequential steps. Every product analytics tool has a funnel builder.

**How to build a useful funnel:**

1. Define the steps in order (e.g., signed_up → first_search → saved_list → upgraded)
2. Set a conversion window (how long between steps counts? 7 days? 30 days?)
3. Look at conversion rate between each pair of steps
4. Identify the biggest drop-off — that's your optimization priority
5. Segment by acquisition channel, plan, or user property to find where specific groups struggle

**Common mistake:** Funnels that are too long (8+ steps) or too short (2 steps). 3–5 steps per funnel keeps it actionable.

### Cohort Retention Analysis

Cohort analysis groups users by when they started (signup week/month) and measures how many return over time.

**How to read a retention table:**

```
            Week 0   Week 1   Week 2   Week 3   Week 4
Jan cohort  100%     35%      28%      22%      20%
Feb cohort  100%     40%      30%      25%      23%
Mar cohort  100%     45%      35%      30%      28%
```

This shows improving retention over time — the product is getting better at keeping users. If the numbers are declining cohort-over-cohort, something is degrading (could be worse traffic quality, a product change that hurt retention, or seasonal effects).

**Tiered approach:**

| Level | What to analyze |
|---|---|
| Good | Overall retention curve — is it flattening (good) or declining to zero (bad)? |
| Better | Retention by acquisition channel — which sources produce sticky users? |
| Best | Retention by activation status — do activated users retain at a fundamentally different rate? (This validates your activation metric.) |

### Acquisition Quality Analysis

The highest-leverage analysis for connecting marketing and product. It answers: "Which channels produce customers, not just signups?"

**How to run it:**

1. Segment users by first-touch acquisition source (from your UTM capture)
2. For each channel, calculate: activation rate, week-4 retention, trial-to-paid conversion, average revenue per user
3. Rank channels by downstream quality metrics, not signup volume
4. Compare CAC per channel against the quality metrics to find your most efficient channels

**Example output:**

| Channel | Signups | Activation rate | Week-4 retention | Trial→Paid | Cost per activated user |
|---|---|---|---|---|---|
| Google Search (brand) | 200 | 55% | 40% | 12% | $8 |
| Google Search (category) | 150 | 45% | 35% | 8% | $22 |
| Reddit posts | 300 | 30% | 20% | 3% | $0 (organic) |
| Product Hunt launch | 500 | 15% | 8% | 1% | $0 (organic) |

This table tells a completely different story than signup volume alone. Product Hunt looks great on signups but terrible on activation and retention. Google brand search is expensive per signup but cheap per activated user.

### Segment Comparison

Compare metrics across user segments to find your best-fit customers.

**Useful segments to compare:**
- Company size (solo / small team / enterprise)
- Plan type (free / trial / paid)
- Use case (if you capture this on signup)
- Geographic region
- Technical sophistication (API usage vs. UI-only)

**What to look for:** Segments where activation and retention are significantly higher — these are your best-fit customers. Double down on acquiring more of them rather than trying to improve metrics for poor-fit segments.
