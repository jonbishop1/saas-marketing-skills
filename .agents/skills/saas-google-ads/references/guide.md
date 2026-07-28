# Google Ads: Complete Reference Guide
 
---
 
## KEYWORDS
 
### How to Think About Keywords
 
A keyword is a bet that a certain query pattern predicts buyer intent. The query "api monitoring" is ambiguous — it could be a student, a developer evaluating tools, or someone who just had an outage. The query "api monitoring pricing" is much less ambiguous. Specificity costs less in volume but more per click, and converts better. For most software products, start specific and expand.
 
### Keyword Categories for Software
 
| Category | Examples | Intent | Notes |
|---|---|---|---|
| **Branded** | "[your product]", "[your product] pricing", "[your product] vs" | Very high | Defend these — competitors bid on them |
| **Competitor** | "[competitor name]", "[competitor] alternative", "[competitor] pricing" | Very high | High CPC, strong buying intent; keep in separate campaign |
| **Category/solution** | "api monitoring tool", "saas analytics platform" | High | Core acquisition; most volume at acceptable CPA |
| **Problem/pain** | "api keeps timing out", "how to reduce churn", "salesforce too expensive" | Medium-high | User has the pain but hasn't found the category yet |
| **Feature-specific** | "webhook retry logic", "nps survey widget", "sso saml integration" | High | Low volume, very targeted; often underpriced |
| **Integration/compatibility** | "hubspot api integration", "stripe webhook monitoring" | High | Strong signal: user is technical and has specific stack |
| **Comparison** | "datadog vs newrelic", "best api monitoring tools 2024" | High | User is in evaluation mode |
| **Alternative** | "datadog alternative", "cheaper than pagerduty" | Very high | High commercial intent; good for competitor campaigns |
 
### Intent Tiers
 
```
Tier 1 — Transactional (bid aggressively):
  "api monitoring pricing"
  "[competitor] alternative"
  "best [category] for [use case]"
  "[feature] tool"
 
Tier 2 — Commercial investigation (bid normally):
  "api monitoring software"
  "[category] comparison"
  "how to monitor api uptime"
 
Tier 3 — Informational (bid cautiously or exclude):
  "what is api monitoring"
  "api monitoring tutorial"
  "api monitoring github"
 
Tier 4 — Irrelevant lookalikes (negative these):
  "api monitoring open source"  ← if you're not OSS
  "api monitoring jobs"
  "api monitoring course"
```
 
### Building Your Initial Keyword List
 
1. Your product's category name(s) — what would someone type who knows what they need?
2. Competitor names — in-market buyers actively evaluating
3. The problem your product solves — phrased as a symptom ("api goes down"), not a solution
4. Your key features — by name if they have known industry names
5. Integrations your product has — "[tool they use] + [your product's function]"
 
**Sources:** Google Keyword Planner (volume + CPC estimates), Google Search Console (organic queries you already rank for), search terms report from existing campaigns, competitor landing pages and meta descriptions.
 
**For new/AI product categories with no search volume:** Target adjacent problem queries and tool-replacement queries. "ai code review" may have low volume, but "how to speed up code review", "github pr review tool", and "[competitor] alternative" may have meaningful volume. Expect lower conversion rates — users need more education.
 
### Match Types
 
| Type | Syntax | Behavior | Use when |
|---|---|---|---|
| **Exact** | `[keyword]` | Matches the keyword + close variants (misspellings, plurals, reordering) | You want maximum control; good for high-value, proven keywords |
| **Phrase** | `"keyword"` | Query must contain the phrase in order, with words before/after allowed | You know the core phrase but want to capture long-tail variants |
| **Broad** | `keyword` | Google interprets intent broadly; can match semantically related queries | Only with Smart Bidding + 30+ conversions/month; risky without data |
 
**Close variants:** Google treats "API monitoring", "monitor APIs", and "API uptime check" as close variants of each other. You don't need all three as separate keywords. But "API monitoring free" and "API monitoring enterprise" are meaningfully different intent signals — keep those as separate keywords or negatives.
 
**Recommended progression:**
1. Start: Exact + Phrase only
2. After 30+ conversions/month: test Broad on proven keywords with Target CPA bidding
3. Never use Broad on competitor keywords — Google will match your competitor name ads to your own brand terms
 
### Negative Keywords
 
Negatives are the highest-ROI action most underinvested accounts can take. Build the list before launch; add to it weekly from the Search Terms report.
 
**Universal software negatives (add at account level):**
```
free, free trial [only if you don't offer one], open source, github
jobs, careers, salary, hiring, interview, resume
tutorial, course, certification, training, learn, how to [informational]
reddit, stackoverflow, quora, hacker news
wikipedia, docs [unless you're targeting devs in docs mode]
crack, torrent, nulled, pirated
reviews [if you want buyers not researchers — but evaluate this per campaign]
```
 
**Dev tool specific negatives:**
```
npm, pip, brew [package managers — looking for OSS]
vs code extension, plugin [if you're not a plugin]
self hosted [if you're SaaS only]
```
 
**Enterprise/B2B negatives:**
```
small business, smb, startup [if enterprise only]
personal, individual [if team product]
```
 
**Negative keyword list levels:**
- **Account-level shared list:** Universal negatives that apply everywhere
- **Campaign-level:** Negatives specific to that campaign's audience (e.g., exclude "free" from a paid-plan campaign but not from a free-trial campaign)
- **Ad group-level:** Prevent keyword cannibalization between ad groups (if you have one ad group for "API monitoring" and one for "API uptime", add each as a negative in the other)
 
**Weekly ritual:** Open Search Terms report → filter for last 7 days → scan for irrelevant queries → add as negatives → look for high-performing queries not yet in your keyword list → add as exact match.
 
### Competitor Keyword Strategy
 
**Legal considerations:** You can bid on competitor brand names in the US and most markets. You cannot use competitor trademarks in your ad copy (headline/description). Showing "Better than [Competitor]" is a grey area — avoid explicit claims. "Alternative to [Competitor]" as a headline is generally fine.
 
**Separate competitor campaigns** from non-brand. Competitor CPCs are high and CTRs are low — mixing with your regular campaigns pollutes your data and your Quality Score.
 
**Expected competitor campaign benchmarks:**
- CPC: 2–5× higher than category terms
- CTR: 1–3% (lower than category)
- Conversion rate: variable — often lower, but high-value when it converts
 
**Landing page for competitor campaigns:** Don't send to your homepage. Send to a dedicated comparison page that acknowledges the competitor, highlights your differentiation, and has a clear CTA. "Switching from [Competitor]" pages convert well.
 
---
 
## AD CREATION
 
### Responsive Search Ads (RSAs)
 
RSAs are the standard Search ad format. Provide up to 15 headlines (30 chars each) and 4 descriptions (90 chars each). Google ML selects combinations and optimizes over time.
 
**Important:** Google's optimization works better with diverse inputs. 15 variations of the same headline idea gives the algorithm nothing to work with. Write 3–4 distinct angles, then fill the rest with variations.
 
**Angles to cover across your headlines:**
- Category/keyword (for relevance and QS): "API Monitoring Tool"
- Problem: "APIs Failing Silently?"
- Outcome/benefit: "Know About Outages Before Users Do"
- Differentiator: "5-Minute Setup, No Code Required"
- Social proof: "Trusted by 10,000+ Engineering Teams"
- CTA/offer: "Start Free Trial" / "Free 14-Day Trial"
- Price/offer signal: "Free Plan Available" / "From $29/Month"
 
**Pinning:** Pin headline 1 to your primary keyword/category term to ensure relevance. Leave the rest unpinned. Don't over-pin — it defeats the purpose of RSAs.
 
**Description best practices:**
- Description 1: Core value prop in one sentence. Be specific: "Monitor every API endpoint with < 1 min alerts and 99.9% uptime SLA tracking."
- Description 2: Objection handling or trust signal: "No credit card required. SOC 2 compliant. Trusted by teams at Stripe, GitHub, and Twilio."
 
### Writing Copy for Technical Audiences
 
- **Specific beats vague:** "5ms latency checks" > "fast monitoring". "REST, GraphQL, and gRPC" > "supports all APIs".
- **Numbers and specifics build trust:** "<1 minute setup", "500+ integrations", "99.99% uptime SLA"
- **Avoid marketing language:** "revolutionary", "seamless", "game-changing", "best-in-class" — developers actively distrust this
- **Use the user's vocabulary:** If they searched "webhook retry logic", your headline should say "webhook retry logic" — not "reliable event delivery"
- **Non-technical buyers in enterprise:** CTOs and VPs want outcomes ("reduce API incident response time by 80%"), not features. Engineering managers want both.
 
### Writing Copy for AI Products
 
AI product copy has specific challenges:
- Avoid vague capability claims ("our AI understands your code") — they're unverifiable and sound like every other AI product
- Be specific about what the AI actually does: "Automatically categorizes API errors by root cause" > "AI-powered monitoring"
- Acknowledge limitations implicitly by being specific: specificity implies you know what the product does and doesn't do
- "Powered by GPT-4" is not a differentiator in 2024 — focus on the outcome
 
### Headline Formulas
 
| Formula | Example |
|---|---|
| `[Category] for [Audience]` | "API Monitoring for Backend Engineers" |
| `[Problem]? [Solution].` | "APIs Failing Silently? Get Instant Alerts." |
| `[Action] [Outcome] \| [Differentiator]` | "Monitor Every Endpoint \| 5-Min Setup" |
| `[Number] + [Audience/Users] [Verb]` | "10,000+ Teams Monitor APIs With [Product]" |
| `Free [Product] \| [Trust Signal]` | "Free API Monitoring \| No Credit Card" |
| `[Competitor] Alternative` | "Datadog Alternative — 70% Less Expensive" |
 
### CTAs by Funnel Stage
 
**Hard CTAs** (bottom-funnel, search campaigns — use these by default):
Start Free Trial / Get Started Free / Book a Demo / Create Free Account / Get API Key
 
**Soft CTAs** (when product is complex, expensive, or long-cycle):
See How It Works / Watch Demo / Request a Demo / Compare Plans
 
**Action-oriented** (emphasizes outcome):
Start Monitoring in 5 Minutes / See Your First Alert / Connect Your First API
 
### Dynamic Keyword Insertion (DKI)
 
```
Headline: {KeyWord:API Monitoring Tool}
```
If the query matches a keyword in the ad group, it inserts the query. Falls back to "API Monitoring Tool" if no match.
 
Use only in tightly themed ad groups with controlled keyword lists. DKI produces awkward output on long-tail queries. Always set a meaningful fallback.
 
### Ad Assets (Extensions)
 
Add all relevant asset types — they expand your ad size and improve CTR at no extra cost per click.
 
| Asset | What to include for software |
|---|---|
| **Sitelinks** | Pricing, Docs/API Reference, Integrations, Case Studies, Free Trial |
| **Callouts** | "No Credit Card Required" / "SOC 2 Compliant" / "99.9% Uptime SLA" / "Open Source Available" |
| **Structured snippets** | Features: [list 4 key features]; Integrations: [list 4 key integrations] |
| **Lead form** | For demo/enterprise flows — captures lead in SERP without a click |
| **Price** | If pricing is transparent — pre-qualifies clicks and lowers irrelevant CPC |
| **Image** | Product screenshot or diagram — improves visual presence |
 
### Landing Pages
 
**The message match contract:** Every claim in your ad must be fulfilled on the landing page. Ad says "Free 14-day trial" → landing page CTA must be "Start your free trial". Ad headline uses "API monitoring" → landing page H1 must include "API monitoring". Mismatch between ad and landing page is the most common cause of high CPA with good CTR.
 
**Landing page structure for software:**
1. H1: matches ad headline keyword + primary outcome
2. Subheadline: secondary value prop or social proof
3. Above-fold CTA: single, clear, matching the ad offer
4. Feature summary: 3–4 key capabilities, specific and outcome-framed
5. Social proof: logos, testimonials, case study excerpts
6. Secondary CTA: same as above-fold
7. Objection handling: pricing transparency, security certs, trial terms
 
**Technical requirements:**
- LCP < 2.5s (check PageSpeed Insights — Google scores this for Quality Score)
- CLS < 0.1 (layout shift degrades experience and QS)
- Mobile responsive (even for dev tools — Google scores mobile)
- Minimal navigation — remove navbar/footer links that lead users away from conversion
- Form fields: ask for only what's required. Each extra field reduces CVR.
 
**Dedicated landing pages vs. homepage:** Never send paid traffic to a homepage that serves multiple audiences. Build dedicated pages per campaign intent:
- Brand campaign → homepage is ok if it's tight
- Competitor campaign → comparison/switching page
- Feature-specific campaign → feature landing page
- Problem-aware campaign → problem-solution narrative page
 
**Landing pages for different funnel stages:**
- Trial/signup: reduce friction to zero. Email + password, or SSO. One screen.
- Demo request: 3–4 fields max. Name, email, company, optional message.
- Content download/lead magnet: 2 fields. Email, first name.
 
---
 
## CONVERSION TRACKING
 
### How Attribution Works
 
When a user clicks a Google Ad, Google appends a `gclid` (Google Click ID) parameter to the URL. Your app should capture and store this. When a conversion happens (immediately or weeks later), Google matches the conversion event back to the original click using gclid.
 
What can break this chain:
- Redirect chains that strip URL parameters
- Cookie blocking / browser privacy settings (gclid lives in a cookie, 90 days)
- Cross-device journeys (user clicks on desktop, converts on mobile)
- Cross-domain journeys without cross-domain tracking configured
 
Enhanced conversions and offline conversion import exist specifically to patch these gaps.
 
### Auto-Tagging vs. UTM Parameters
 
Both are needed. They serve different purposes.
 
**Auto-tagging (gclid):** Powers Google Ads → GA4 attribution. Enabled in Account Settings → Auto-tagging. Required for importing GA4 conversions and for Smart Bidding to work correctly.
 
**UTM parameters:** Work in any analytics tool; survive redirect chains; captured by CRMs on form fill (gclid usually isn't). Set a tracking template at account level:
 
```
Account Settings → Tracking → Tracking template:
{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={adgroupid}&utm_term={keyword}
```
 
ValueTrack parameters (`{campaignid}`, `{keyword}`, etc.) are auto-populated by Google. Set this once at account level and it applies to all campaigns.
 
Run both. gclid for Google attribution, UTMs for everything else.
 
### Google Tag Manager Architecture
 
GTM sits between your codebase and your tracking tags. Instead of hardcoding tracking calls in your app, you push structured data to a `dataLayer` array, and GTM handles routing that data to Google Ads, GA4, etc. This means tracking changes don't require deploys.
 
**Core concepts:**
- **Container:** Your GTM workspace; one snippet installed on every page
- **Tags:** What fires (e.g., Google Ads Conversion tag, GA4 Event tag)
- **Triggers:** When tags fire (e.g., Custom Event matching `trial_signup`)
- **Variables:** Data pulled from the page or dataLayer (e.g., `{{DLV - user_id}}`)
- **dataLayer:** A JS array your app pushes structured events to
 
**GTM container snippet (install on every page):**
```html
<!-- In <head> -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
 
<!-- Immediately after <body> -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```
 
**Pushing a conversion event from your app:**
```javascript
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({
  event: 'trial_signup',           // matches GTM Custom Event trigger
  user_id: user.id,
  plan: 'free_trial',
  value: 240,                      // estimated LTV × conversion rate
  currency: 'USD',
  transaction_id: user.id          // deduplication
});
```
 
Then in GTM: Create a Custom Event trigger matching `trial_signup`, attach a Google Ads Conversion Tracking tag, map `value` and `transaction_id` from the dataLayer.
 
### Direct gtag.js Implementation (alternative to GTM)
 
Use when: small team, no need for marketer-controlled tracking, no GTM container yet.
 
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-XXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-XXXXXXXXX');
</script>
```
 
Fire conversion on event:
```javascript
gtag('event', 'conversion', {
  send_to: 'AW-XXXXXXXXX/AbCdEfGhIjKlMnOp',
  value: 240.0,
  currency: 'USD',
  transaction_id: user.id
});
```
 
### Conversion Values
 
Assigning values enables value-based bidding (Target ROAS, Maximize Conversion Value). Even rough values beat no values.
 
| Conversion type | Value formula |
|---|---|
| Trial signup | LTV × trial-to-paid rate (e.g., $1,200 × 20% = $240) |
| Demo booked | LTV × demo-to-close rate (e.g., $10,000 × 15% = $1,500) |
| Paid purchase | Actual revenue |
| MQL form | Estimated revenue per lead |
| API key created | LTV × activation-to-paid rate |
 
Update these values quarterly as you get better funnel data.
 
### Enhanced Conversions
 
Improves attribution by hashing and sending first-party user data (email, name, phone) with conversion events, allowing Google to match conversions to signed-in Google users even when cookies are blocked or device is different.
 
**Enable:** Google Ads → Tools → Conversions → Settings → Enhanced conversions → turn on.
 
**Implementation via GTM — push user data with every conversion event:**
```javascript
window.dataLayer.push({
  event: 'trial_signup',
  user_data: {
    email: 'user@example.com',      // GTM/Google handles SHA-256 hashing
    phone_number: '+15551234567',
    address: {
      first_name: 'Jane',
      last_name: 'Smith'
    }
  }
});
```
 
Most valuable for: enterprise software with long sales cycles; cross-device journeys; privacy-restricted environments (Safari ITP, Firefox ETP).
 
### Offline Conversion Import
 
For sales-led products: the deal closes in your CRM, not on your website. Offline conversion import feeds closed-won revenue back into Google Ads so Smart Bidding can optimize for actual revenue.
 
**Step 1: Capture gclid on every form submission**
```javascript
// On page load, read gclid and persist it
const params = new URLSearchParams(window.location.search);
const gclid = params.get('gclid');
if (gclid) {
  // Store in cookie (90-day window)
  document.cookie = `gclid=${gclid}; max-age=7776000; path=/; SameSite=Lax`;
  // Also store in hidden form field
  const field = document.querySelector('input[name="gclid"]');
  if (field) field.value = gclid;
}
```
 
**Step 2: Save gclid with the lead in your CRM**
Pass gclid through your form to your backend → store on the lead record in your CRM alongside UTM fields.
 
**Step 3: Upload conversions when deals close**
Options:
- Manual CSV upload: Google Ads → Conversions → Upload (format: gclid, conversion_name, conversion_time, conversion_value)
- Google Ads API: automate for high-volume pipelines
- Native CRM connectors: Salesforce and HubSpot both have Google Ads integrations that handle this
 
**What to import:**
- MQL created (intermediate signal)
- SQL / opportunity created (stronger signal)
- Closed-won deal (strongest signal — use actual ACV/ARR)
 
### Attribution Models
 
| Model | Behavior | Use when |
|---|---|---|
| **Last click** | 100% credit to last ad clicked | Default; fine for short cycles |
| **Data-driven** | ML distributes credit based on conversion path data | Best; requires 300+ conversions/month |
| **Linear** | Equal credit across all touchpoints | Understanding full funnel |
| **First click** | 100% credit to first ad | Brand awareness measurement |
 
Use data-driven when available. Use last click otherwise. Don't use time-decay (penalizes upper-funnel unfairly for long-cycle SaaS).
 
### GA4 Integration
 
Link in Google Ads → Tools → Linked Accounts → Google Analytics 4.
 
What you unlock:
- GA4 audiences available in Google Ads (e.g., "users who viewed pricing page but didn't sign up")
- Post-click behavior data segmented by campaign (bounce rate, pages/session, goal completions)
- Cross-channel attribution in GA4
- Import GA4 conversions into Google Ads as conversion actions
 
Cross-domain tracking: if your product lives on `app.product.com` and your marketing site on `product.com`, configure cross-domain measurement in GA4 (Admin → Data Streams → Configure tag settings → Configure your domains).
 
### When Tracking Breaks Silently
 
Silent tracking failures are common and masquerade as performance drops. Before changing bids or pausing campaigns, verify tracking is working.
 
**Common causes:**
- Site deploy removed GTM snippet from `<head>`
- Thank-you page URL changed (conversion tag fires on URL match that no longer exists)
- Redirect chain stripping gclid (e.g., link shortener, SSO redirect)
- GTM container published with an error
- Form submission now uses AJAX and the page doesn't reload (conversion fires before GTM is ready)
 
**How to detect:**
- Compare Google Ads conversion count vs. GA4 goal completions for the same period — should be within 10–15%
- Use Google Tag Assistant (Chrome extension) on your own site to verify tags fire on conversion
- Check raw session volume in GA4 — if sessions are flat and conversions dropped, it's tracking
 
**Data exclusions:** If you have a known period of broken tracking (e.g., a deploy broke your conversion tag for 3 days), exclude those dates in Google Ads (Tools → Conversions → Data exclusions). This prevents Smart Bidding from treating the conversion drought as a signal to adjust bids downward.
 
---
 
## AUDIENCES
 
### Observation vs. Targeting Mode
 
- **Observation:** Audience added for data collection and bid adjustment only. Your ads still show to everyone; you just get segmented reporting and can bid ± on this audience.
- **Targeting:** Restricts your ads to only show to this audience. Use carefully on Search — it dramatically reduces reach.
 
Default: add all audiences in Observation mode. Switch specific audiences to Targeting only when you have clear evidence they convert much better and you're okay limiting reach.
 
### First-Party Audiences
 
| Audience | How to create | Use |
|---|---|---|
| All website visitors | GA4 → Google Ads audience sync | Retargeting; bid +15–20% for RLSA |
| Pricing page visitors | GA4 custom audience (page path contains /pricing) | High intent; bid +30–50% |
| Demo page visitors (non-converters) | GA4 audience with session_start and no conversion event | RLSA bid boost |
| Converters | GA4 audience with conversion event | Exclude from prospecting |
| Customer list | Upload CSV of customer emails (Customer Match) | Exclude from acquisition; upsell campaigns |
 
### RLSA (Remarketing Lists for Search Ads)
 
Attach first-party audiences to Search campaigns in Observation mode. When a past visitor searches your keywords again, bid higher — they already know you and are more likely to convert.
 
Typical bid adjustments:
- All site visitors: +10–20%
- Pricing page visitors: +25–40%
- Demo page visitors: +30–50%
- Previous trial users (non-converted to paid): +40%
 
### Google Audiences (In-Market, Affinity)
 
Add in Observation mode to learn which Google audience segments over- or under-index for your conversions. Don't restrict reach. After 4+ weeks of data, apply bid adjustments to segments with strong performance.
 
Useful in-market segments for software:
- Enterprise Technology (SaaS/cloud)
- Business Software
- Developer Tools (in some markets)
- CRM Software, Marketing Automation (for relevant categories)
 
### Audience Exclusions
 
Always exclude:
- Existing customers from acquisition campaigns (use Customer Match exclusion)
- Converters from RLSA prospecting (they've already signed up)
 
For enterprise/sales-led: exclude current pipeline contacts if your CRM integrates with Google Ads — no need to pay for clicks from deals already in progress.
 
---
 
## BIDDING
 
### Bidding as a Control System
 
Smart Bidding works like a PID controller: you set a target (CPA or ROAS), and Google adjusts bids in real-time per auction to minimize deviation from the target. The system needs a reliable feedback signal (conversion tracking), enough volume to model the system (30+ conversions/month), and budget headroom to act.
 
If any of those are missing, manual or rule-based bidding outperforms Smart Bidding — not because you're smarter than the algorithm, but because the algorithm has nothing to optimize against.
 
### Strategy Selection
 
```
Do you have reliable conversion tracking?
  No → Fix tracking. Use Manual CPC temporarily.
  Yes →
    Do you have 30+ conversions/month in this campaign?
      No → Maximize Conversions (no target) to build data
      Yes →
        Do you know your target CPA or ROAS?
          Yes → Target CPA or Target ROAS
          No → Maximize Conversions, monitor until you have a CPA baseline,
               then set Target CPA at 120% of actual CPA to give the algo headroom
```
 
### Strategy Comparison
 
| Strategy | Google controls | You control | Best for |
|---|---|---|---|
| Manual CPC | Nothing | Bid per keyword | New accounts; auditing baseline CPCs |
| Enhanced CPC | Bid ±30% per auction | Base bid | Transitioning from manual |
| Maximize Clicks | Bids to get max clicks | Budget cap | Traffic only; no conversion tracking |
| Maximize Conversions | Bids to max conversion volume | Budget | Building data; no CPA constraint |
| Target CPA | Bids to hit CPA target | Target CPA | Established accounts, 30+ conv/month |
| Target ROAS | Bids to hit ROAS target | Target ROAS | When conversions have revenue values |
| Maximize Conv. Value | Bids to max total revenue | Budget | Mature accounts with value-based tracking |
 
**Portfolio bid strategies** (Tools → Shared Library → Bid strategies): Apply one Smart Bidding strategy across multiple campaigns. Useful when individual campaigns don't have enough conversion volume on their own but combined they do. Common for enterprise with separate brand/competitor/category campaigns.
 
### Budget Sizing
 
```
Minimum daily budget per campaign = Target CPA × 3
Monthly budget to test Smart Bidding = Target CPA × 50
 
Google can overdeliver by up to 2× on any given day.
Monthly spend won't exceed (daily budget × 30.4).
 
Budget allocation starting point:
  Brand campaigns:         10–15%  (high ROI, protect your name)
  Competitor campaigns:    15–25%  (high CPA, in-market buyers)
  Category/solution:       40–50%  (core acquisition volume)
  Problem-aware:           10–20%  (top-of-funnel)
  Retargeting (Display):   5–10%
```
 
Shared budgets (Tools → Shared Library → Budgets): Let Google dynamically allocate across campaigns. Only use when campaigns have similar CPAs — Google will over-invest in higher-volume campaigns at the expense of lower-volume ones.
 
### Auction Mechanics
 
```
Ad Rank = bid × Quality Score × expected asset impact
 
Actual CPC = (competitor's Ad Rank ÷ your Quality Score) + $0.01
```
 
This means: a competitor with twice your bid but half your Quality Score has the same Ad Rank as you — but pays more per click. Improving QS is free performance.
 
### Bid Adjustments
 
Layer on top of base strategy. Less impactful under full Smart Bidding (Google accounts for these signals natively) but meaningful under manual/eCPC.
 
| Dimension | Common use |
|---|---|
| Device | -20–30% mobile for B2B enterprise; neutral for PLG/dev tools |
| Location | +bid for high-converting geos (e.g., SF, NYC, London for enterprise) |
| Time of day | +bid during business hours for B2B |
| Audience | +bid for pricing page visitors, -bid or exclude for unqualified audiences |
 
---
 
## OPTIMIZATION & TROUBLESHOOTING
 
### The Optimization Loop
 
```
Measure → Diagnose → Hypothesize → Change one thing → Wait → Measure
```
 
**Minimum observation windows after a change:**
- Budget change: 7 days before evaluating
- Bid strategy change: 14 days (learning period)
- Ad copy change: 2–4 weeks (need statistical significance)
- Structural change (new ad group, new campaign): 2–3 weeks
 
Make one significant change at a time. Multiple simultaneous changes make it impossible to isolate causality.
 
### Optimization Lever Priority
 
| Priority | Action | Why |
|---|---|---|
| 1 | Verify tracking is working | Everything depends on clean data |
| 2 | Mine Search Terms → add negatives | Reduces wasted spend immediately |
| 3 | Improve Quality Score on core keywords | Lowers CPC without changing bids |
| 4 | Pause keywords > 3× target CPA, 0 conversions | Stops budget bleed |
| 5 | Test new ad copy angle | High variance upside; 2–4 week feedback loop |
| 6 | Adjust bids by device/location/time | Fine-tuning; only meaningful with volume |
| 7 | Change bidding strategy | Last resort; triggers learning period |
 
### Diagnosing High CPA
 
```
Step 1: Is the problem pre-click or post-click?
  → In GA4: compare landing page CVR by campaign
  → If CVR is normal → problem is ad quality or audience
  → If CVR is low → problem is landing page
 
Step 2: Pre-click diagnosis
  → Search Terms report: irrelevant queries burning budget?
  → Quality Score by keyword: below 6 means overpaying per click
  → Audience segments: which device/location/time has poor CPA?
  → Match type: broad match pulling in bad traffic?
 
Step 3: Post-click diagnosis
  → PageSpeed Insights: LCP > 2.5s kills CVR
  → CTA mismatch: does landing page fulfill the ad's promise?
  → Form friction: too many fields?
  → Message match: does the page headline match the keyword?
```
 
### Diagnosing Low CTR
 
| Symptom | Likely cause | Fix |
|---|---|---|
| Low CTR on brand terms | Competitor bidding on your brand | Improve brand ad copy; add defensive sitelinks |
| Low CTR on non-brand | Ad copy doesn't mirror search query | Pin keyword-matched headline to position 1; rewrite for intent |
| Low CTR across the board | Ad fatigue or poor QS | Refresh copy; check RSA ad strength |
| Impressions but no clicks | Ad position too low | Increase bid or improve QS |
 
### Diagnosing Rising CPC
 
- New competitor entering auctions → check Auction Insights report
- Quality Score drop → review expected CTR, ad relevance, landing page experience
- Match type drift (broad serving lower-quality queries) → add negatives, tighten match types
- Budget exhausting early in day → Google raising CPC to slow delivery (increase budget or add ad scheduling)
 
### Quality Score Deep Dive
 
QS = f(Expected CTR, Ad Relevance, Landing Page Experience)
 
Each component scored Below Average / Average / Above Average.
 
**Improving Expected CTR:**
- Make your headline mirror the keyword exactly (DKI or manual)
- Test different copy angles — problem-led vs. outcome-led vs. social proof
- Add more/better assets (sitelinks increase overall ad CTR)
 
**Improving Ad Relevance:**
- Tighten ad group themes — one ad group, one keyword cluster, one intent
- If a keyword's intent doesn't match any ad in the group, move it
 
**Improving Landing Page Experience:**
- LCP < 2.5s
- Mobile responsiveness
- Content matches what the ad promised
- Clear, single CTA
 
### Auction Insights
 
Reports → Auction Insights (at campaign or ad group level). Shows who else appears in auctions you participate in: Impression Share, Overlap Rate, Position Above Rate, Top of Page Rate.
 
Use it to:
- Identify new competitors entering your auctions (explains sudden CPC increases)
- See if competitors are pulling ahead (high "Position Above Rate" means they frequently outrank you)
- Decide whether to increase bids in response to competitive pressure, or focus on improving QS instead
 
### Campaign Experiments
 
Tools → Experiments → Campaign experiments. Creates a split-test where % of traffic goes to an experimental variant. Statistically rigorous — don't rely on eyeballing.
 
Good experiments to run:
- Bid strategy changes (e.g., Manual CPC vs. Target CPA)
- Landing page variants (A/B different value props)
- Broad vs. Phrase match on proven keywords
- Campaign structure changes (consolidated vs. segmented ad groups)
 
**Statistical significance:** Google shows confidence intervals in the Experiments report. Don't call a winner until the primary metric (usually CPA or CVR) is significant. For high-CPA software products with low volume, this often takes 4–8 weeks.
 
### Weekly Review (20–30 min)
 
**Spend & efficiency:**
- [ ] Total spend vs. budget — on track?
- [ ] CPA vs. target — within ±20%?
- [ ] ROAS vs. target (if value-based)
 
**Traffic quality:**
- [ ] Search Terms report — add negatives, harvest new keywords
- [ ] Impression Share — core campaigns > 50%? If not: budget or rank issue?
- [ ] CTR — drops by campaign?
 
**Creative:**
- [ ] RSA ad strength — any "Poor" ratings?
- [ ] Bottom-quartile ads by CVR — pause if > 300 impressions and no conversion
 
**Tracking health:**
- [ ] Google Ads conversion count vs. GA4 goal completions — within 15%?
- [ ] Any conversion tracking gaps in the data?
 
### Monthly Audit
 
- QS audit: pull QS column on all active keywords; investigate anything < 6
- Keyword performance: pause keywords at > 3× target CPA with 0 conversions
- Budget allocation: are high-performing campaigns budget-constrained? Poor performers consuming budget?
- Audience performance: review bid adjustment ROI by device/location/time — remove ineffective adjustments
- Auction Insights: new competitors? Competitive IS shifts?
- Ad copy rotation: are RSA combos diverse? Any headline never being served?
 
### Reporting Setup
 
**Columns to add in Google Ads interface:**
Conversions, Conv. rate, Cost/conv., Conv. value, ROAS, Impression Share, IS Lost (Budget), IS Lost (Rank), Quality Score, Avg. CPC, Search Impr. Share
 
**Segmentation:** Always segment by device on any campaign where mobile/desktop split might differ. Segment by time period (week-over-week) to catch sudden changes.
 
**Looker Studio:** Connect Google Ads + GA4 + (optionally) your CRM via Google Sheets or a data connector. Build one dashboard showing: spend by campaign, CPA by campaign, CVR by landing page, Search IS by campaign, top search terms, Auction Insights over time.
 
---
 
## SCALING
 
### Signals That You're Ready to Scale
 
- CPA stable and below target for 30+ consecutive days
- Search Impression Share < 70% on core keywords (traffic being left on the table)
- Conversion tracking verified and clean
- Landing page CVR benchmarked and stable
- No active structural issues (poor QS, high wasted spend on irrelevant queries)
 
### Budget Scaling Rules
 
- Increase budget by maximum 20% per week
- Each significant budget increase triggers a Smart Bidding learning period (expect CPA instability for 7–14 days)
- Don't pause and unpause — this resets learning. Reduce budget instead.
- Wait at least 2 full weeks at a new budget level before evaluating performance
 
### Keyword Expansion Sequence
 
1. Add high-performing search terms from Search Terms report as exact-match keywords
2. Add new exact-match keywords in adjacent features or use cases
3. Loosen match types: Exact → Phrase on proven keywords (more variant coverage)
4. Add Broad match on proven keywords once Target CPA bidding is stable (30+ conv/month)
5. Expand competitor keyword list to adjacent or second-tier competitors
6. Add problem-aware keywords (Tier 2 intent) once category terms are profitable
 
### Adding Campaign Types
 
| Campaign type | When to add | Requirements |
|---|---|---|
| Display (retargeting) | Once you have 1,000+ site visitors/month | Converters audience for exclusion; remarketing tag verified |
| Demand Gen | Once Search is profitable; need brand awareness | Creative assets (images, video); $5k+/month budget |
| Performance Max | Search campaigns profitable; need more volume | 50+ conversions/month; clean conversion tracking; existing assets |
 
**Performance Max caution:** PMax gives Google broad control over placements, audiences, and creative combinations. It works well when conversion data is mature. Running it alongside Search: use campaign-level negative keywords (PMax has limited negative keyword controls as of 2024) and monitor cannibalization in Auction Insights.
 
### Geographic Expansion
 
Sequence: US → English-speaking markets (GB, CA, AU, NZ) → non-English-speaking with translated landing pages → emerging markets.
 
Don't expand to a geography if you can't support customers there (timezone, language, compliance). Check CPA by country in existing campaigns before adding new geo campaigns — some countries may already be converting from your US campaigns.
 
### Maintaining CAC/LTV Targets at Scale
 
As you scale, you'll face diminishing returns — the highest-intent, lowest-CPA queries get saturated first. Track the marginal CPA of each new source added:
 
```
Healthy scaling: new volume added at CPA ≤ your target
Diminishing returns: new volume only available at CPA 1.5–2× target
Efficiency ceiling: all incremental volume has CPA > acceptable LTV ratio
```
 
At the efficiency ceiling for search, options are: improve landing page CVR (lowers CPA at same spend), improve trial-to-paid conversion (raises LTV, so CPA ceiling rises), or add new channels (Demand Gen, LinkedIn, content/SEO).
 
Benchmark: a well-run Google Search Ads account for a SaaS product captures 60–80% of branded search impression share and 40–60% of non-brand category impression share. Beyond that, you're likely hitting diminishing returns on pure Search.
