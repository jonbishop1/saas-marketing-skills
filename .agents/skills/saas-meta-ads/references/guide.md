# Meta Ads: Complete Reference Guide
 
---
 
## PIXEL & CONVERSIONS API
 
### Why Both Are Required
 
The Meta Pixel is a JavaScript snippet that fires browser-side events. Post-iOS 14 ATT, ~60–70% of iOS users block third-party tracking — the pixel misses these conversions entirely. Conversions API (CAPI) sends the same events server-side, directly from your backend to Meta's servers, bypassing browser-level blocking.
 
Running pixel only: you're missing a significant portion of conversions, your lookalike audiences are built on incomplete data, and Meta's algorithm is optimizing against a partial signal.
 
Running pixel + CAPI with deduplication: you recover most of the lost signal. Meta deduplicates events that arrive from both sources using an `event_id` you provide.
 
### Pixel Implementation
 
Install the base pixel on every page. Replace `YOUR_PIXEL_ID`.
 
```html
<!-- Meta Pixel Base Code — paste in <head> on every page -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'YOUR_PIXEL_ID');
fbq('track', 'PageView');
</script>
<noscript>
  <img height="1" width="1" style="display:none"
  src="https://www.facebook.com/tr?id=YOUR_PIXEL_ID&ev=PageView&noscript=1"/>
</noscript>
```
 
### Standard Events for Software
 
Fire these pixel events at the appropriate points in your funnel:
 
```javascript
// Trial signup / account creation
fbq('track', 'CompleteRegistration', {
  value: 240.00,        // estimated LTV × conversion rate
  currency: 'USD',
  content_name: 'free_trial'
}, {eventID: 'evt_' + uniqueId});  // eventID for deduplication
 
// Demo request / lead form
fbq('track', 'Lead', {
  value: 1500.00,
  currency: 'USD',
  content_name: 'demo_request'
}, {eventID: 'evt_' + uniqueId});
 
// Paid conversion / upgrade
fbq('track', 'Purchase', {
  value: actualRevenue,
  currency: 'USD'
}, {eventID: 'evt_' + uniqueId});
 
// Key intent signals (track as custom events, don't optimize on these)
fbq('trackCustom', 'ViewPricing');
fbq('trackCustom', 'StartedOnboarding');
fbq('trackCustom', 'InvitedTeamMember');
```
 
### Conversions API (CAPI) Implementation
 
CAPI sends events from your server to Meta's Graph API. Requires a System User access token from Meta Business Manager.
 
**Basic Node.js / server-side implementation:**
 
```javascript
const axios = require('axios');
const crypto = require('crypto');
 
const PIXEL_ID = 'YOUR_PIXEL_ID';
const ACCESS_TOKEN = 'YOUR_CAPI_ACCESS_TOKEN';
 
function hashValue(value) {
  return crypto.createHash('sha256').update(value.toLowerCase().trim()).digest('hex');
}
 
async function sendMetaEvent({
  eventName,        // 'CompleteRegistration', 'Lead', 'Purchase'
  eventId,          // same eventID used in pixel call for dedup
  eventTime,        // Unix timestamp
  userEmail,        // will be hashed
  userPhone,        // optional, will be hashed
  clientIpAddress,  // from request headers
  clientUserAgent,  // from request headers
  eventSourceUrl,   // page URL where conversion happened
  value,            // conversion value
  currency = 'USD'
}) {
  const payload = {
    data: [{
      event_name: eventName,
      event_time: eventTime || Math.floor(Date.now() / 1000),
      event_id: eventId,
      event_source_url: eventSourceUrl,
      action_source: 'website',
      user_data: {
        em: [hashValue(userEmail)],
        ph: userPhone ? [hashValue(userPhone)] : undefined,
        client_ip_address: clientIpAddress,
        client_user_agent: clientUserAgent,
      },
      custom_data: {
        value,
        currency,
      }
    }],
    test_event_code: process.env.NODE_ENV !== 'production'
      ? 'TEST_EVENT_CODE'  // get from Events Manager during testing
      : undefined
  };
 
  await axios.post(
    `https://graph.facebook.com/v18.0/${PIXEL_ID}/events?access_token=${ACCESS_TOKEN}`,
    payload
  );
}
 
// Call this in your signup handler, alongside your pixel call on the frontend
await sendMetaEvent({
  eventName: 'CompleteRegistration',
  eventId: `signup_${user.id}_${Date.now()}`,  // must match pixel eventID
  userEmail: user.email,
  clientIpAddress: req.ip,
  clientUserAgent: req.headers['user-agent'],
  eventSourceUrl: req.headers.referer,
  value: 240.00,
});
```
 
**Deduplication:** The `event_id` must be identical in both the pixel call and the CAPI call for the same conversion event. Meta uses this to deduplicate. If event IDs don't match, you'll double-count conversions.
 
**Getting your CAPI access token:**
1. Meta Business Manager → Business Settings → System Users
2. Create a system user with Standard access
3. Assign the pixel to the system user with "Analyze and advertise" permission
4. Generate token with `ads_management` and `ads_read` permissions
 
### iOS 14 Event Configuration
 
Post-iOS 14, Meta allows a maximum of 8 conversion events per pixel for optimization. Prioritize them in Events Manager:
 
```
Priority 1: Purchase (or equivalent — paid conversion)
Priority 2: CompleteRegistration (trial signup / account creation)
Priority 3: Lead (demo request)
Priority 4: InitiateCheckout (started upgrade flow)
Priority 5: ViewContent (pricing page view — useful signal)
Priority 6-8: Custom events (onboarding steps, key feature usage)
```
 
Only prioritized events can be used for campaign optimization and in Ads Manager reporting for iOS traffic.
 
### Event Quality Score
 
Meta's Events Manager shows an Event Match Quality score (0–10) for each event. Higher scores mean Meta can better match events to user profiles.
 
Improve match quality by sending more user data parameters: email (required), phone, first name, last name, date of birth, city, state, zip, country. All are hashed before sending. Even partial matches improve the score.
 
---
 
## CREATIVE SPECS & FORMATS
 
### Universal Requirements
 
- All ad images and videos must be uploaded at the highest resolution you have
- Text overlay: keep under 20% of image area (Meta penalizes heavy text)
- Always include captions on video ads (85% of users watch without sound)
- Every ad needs a destination URL with UTM parameters
 
### Format Specs
 
**Single Image:**
- Recommended: 1080×1080px (1:1) or 1200×628px (1.91:1)
- For Stories/Reels: 1080×1920px (9:16)
- File: JPG or PNG, max 30MB
- Text: 125 chars primary text, 40 chars headline
 
**Single Video:**
- Feed: minimum 1080×1080px, 4:5 ratio performs best (takes more vertical space)
- Stories/Reels: 1080×1920px (9:16)
- Length: 6–15s for cold (attention is short); up to 60s for warm/retargeting
- File: MP4 or MOV, H.264, max 4GB
- Always add closed captions (SRT file or Meta's auto-captions)
 
**Carousel:**
- 2–10 cards, each 1080×1080px
- Each card has its own headline, description, and destination URL
- First card is most critical — it determines whether users swipe
- Use for: feature showcase, step-by-step process, before/after, multiple products/plans
 
**Collection:**
- Cover image/video + 4 product images below
- Opens an Instant Experience (fast-loading full-screen page within Meta)
- Useful for showcasing multiple pricing plans or use cases
 
### Screen Recordings for Software
 
Screen recordings are the highest-authenticity format for software products and require no production budget:
 
- Record at 1080p minimum
- Use a clean browser/desktop (no personal data, no clutter)
- Show the most compelling moment in the first 3 seconds (not the login screen)
- Add text overlays to guide attention
- Trim ruthlessly — show the "aha moment" fast
- Add background music at low volume (20–30% of dialogue volume)
 
Tools: Loom, Quicktime, ScreenFlow, Descript for editing
 
### UGC-Style Video
 
UGC (user-generated content) style means it looks like something a real user filmed, not a brand ad. It performs well because it's native to the feed. You don't need actual users — you can produce it:
 
- Film on a phone, not a professional camera
- Casual setting (desk, home office)
- Founder or employee talking to camera
- No logo bumpers or professional transitions
- Authentic script, not polished ad copy
 
Hook structure for UGC talking-head video:
```
0–3s:   Direct-to-camera statement of the problem or claim
        "I wasted $40k on ads before I figured this out."
3–8s:   Brief context / credibility
        "I've been running SaaS marketing for 8 years and..."
8–20s:  The value / demonstration
        "Here's what actually works: [show product or insight]"
20–30s: CTA
        "Link in bio / Try it free"
```
 
---
 
## AD COPY FORMULAS
 
### Copy Structure
 
```
Primary text:   Hook → Context/problem → Solution/product → Proof → CTA
Headline:       Reinforce value prop or CTA (5–10 words, specific)
Description:    Supporting detail or objection removal (often truncated, put key info above)
```
 
### Hook Formulas for Software
 
**Pain statement:**
"If [common problem], you're losing [specific consequence]."
→ "If your API fails silently, you're the last to know about outages."
 
**Counterintuitive:**
"We [did thing everyone does] and [unexpected result]."
→ "We stopped targeting developers on LinkedIn and our CAC dropped 40%."
 
**Specific result:**
"How [company type] went from [before] to [after] in [time]."
→ "How a 4-person SaaS team reduced churn from 8% to 2% in 90 days."
 
**Direct address:**
"Attention [specific ICP]:"
→ "Attention founders running on AWS:"
 
**Question:**
"Are you still [outdated approach]?"
→ "Are you still manually monitoring your API endpoints?"
 
**Social proof lead:**
"[N] [audience type] use [product] to [outcome]."
→ "12,000 engineering teams use [Product] to catch API failures before users do."
 
**Bold claim:**
"[Product] is the [superlative] [category] for [audience]."
→ "This is the fastest way to set up uptime monitoring. Period."
 
### Copy for Cold vs. Warm Audiences
 
**Cold (no prior exposure):**
- Lead with a problem or insight, not the product
- Establish credibility before asking for anything
- Longer copy often works (pre-qualifies before the click)
- CTA: low-commitment ("See how it works", "Start free", "Watch demo")
 
**Warm retargeting (visited site, watched video):**
- They know you — skip the intro
- Address the objection that stopped them converting
- Shorter, more direct copy
- CTA: specific and action-oriented ("Start your free trial", "Book your demo today")
 
**Hot retargeting (trial users, demo no-shows):**
- Acknowledge where they are in the journey
- Specific offer or incentive if appropriate
- Urgency is appropriate here
- CTA: direct ("Complete your setup", "Reschedule your demo", "Upgrade now")
 
### Copy Length Testing
 
For cold audiences and complex software, test long-form copy. Long copy pre-qualifies and educates — users who read 300 words and click are more likely to convert than users who clicked impulsively on 2-line copy.
 
Long-form structure:
```
Line 1:   Hook (stop the scroll)
Lines 2-4: Problem elaboration (make them feel understood)
Lines 5-7: Solution introduction (your product, specifically)
Lines 8-10: Proof (numbers, customer names, specific results)
Lines 11-12: Objection removal ("No credit card required. Cancel anytime.")
Line 13:  CTA
```
 
Use line breaks aggressively. No paragraphs longer than 2 lines. Each line should earn the next.
 
---
 
## AUDIENCE SETUP: IMPLEMENTATION DETAILS
 
### Creating Lookalike Audiences
 
1. Meta Ads Manager → Audiences → Create Audience → Lookalike Audience
2. Select source → your pixel or a customer list
3. Select location (start with US)
4. Select size (1% = ~2M users in US = tightest match)
 
**Customer list format for upload:**
CSV with columns: email, phone, first_name, last_name, country
Meta hashes the data before matching. Higher match rate = better lookalike.
 
**Segment your customer list before uploading:**
- LTV top 20% → upload as "High LTV customers" → best seed
- All paid customers → upload as "All customers" → good seed
- Trial users who converted → useful seed
- All trial users → noisy; too broad
 
### Building Retargeting Audiences from Pixel
 
Meta Ads Manager → Audiences → Create Audience → Custom Audience → Website
 
Key audiences to build:
```
All website visitors         → 30 days
Pricing page visitors        → 14 days (URL contains /pricing)
Demo page visitors           → 14 days (URL contains /demo or /book)
Blog readers                 → 60 days (URL contains /blog)
Docs visitors                → 30 days (signals high intent for dev tools)
High-intent visitors         → 7 days (pricing OR demo page)
Converters                   → 30 days (use as exclusion)
```
 
### Engagement-Based Audiences
 
Build audiences from Meta-native engagement — these work even without pixel data:
 
- Video viewers: 25%, 50%, 75%, 95% completion thresholds
- Instagram profile engagers (last 365 days)
- Facebook page engagers (last 365 days)
- Lead form openers / completers
- Ad engagers (anyone who interacted with any of your ads)
 
Video viewer audiences are particularly useful: create a retargeting campaign targeting people who watched 50%+ of a prospecting video. They're warm but didn't click.
 
### Advantage+ Audiences
 
Meta's automated audience product. You can provide audience suggestions (interests, demographics) but Meta is free to go beyond them. Works best when:
- Pixel has 1,000+ conversions
- Product has broad potential appeal
- You've already tested and validated creative
 
Don't use Advantage+ Audiences as a shortcut to skip audience research. Use it when you have enough data for Meta's model to work from.
 
---
 
## OPTIMIZATION & TROUBLESHOOTING
 
### The Optimization Loop
 
```
Measure → Diagnose → Change one thing → Wait for learning → Measure
```
 
**Minimum wait time after changes:**
- New ad: 3–5 days before evaluating
- Budget change > 20%: 7 days (learning phase reset)
- Audience change: 7–14 days
- New campaign: 2 weeks before making structural decisions
 
### Diagnosing High CPA
 
```
Step 1: Is it pre-click or post-click?
  → Check CVR on your landing page (GA4, segmented by Meta source)
  → If landing page CVR is normal → problem is ad quality or audience
  → If landing page CVR is low → landing page problem
 
Step 2: Pre-click diagnosis
  → CTR < 0.5%? → Hook/creative not resonating → test new angles
  → CPM rising? → Audience saturation or increased competition → broaden or refresh
  → Frequency > 3? → Creative fatigue → rotate in new ads
  → Relevance score < 6? → Creative/audience mismatch → tighten targeting or change creative
 
Step 3: Post-click diagnosis
  → Page load > 3s? → Fix this first — every second costs ~7% CVR
  → Ad promise ≠ landing page? → Message mismatch → align copy
  → Form friction? → Too many fields → reduce to email only if possible
  → Mobile experience broken? → Check on actual mobile device
```
 
### Diagnosing Low CTR
 
| CTR range | Diagnosis | Action |
|---|---|---|
| < 0.3% | Hook failing entirely | Test 5+ new hook concepts |
| 0.3–0.6% | Hook weak or audience mismatch | Test new hooks; also test audience |
| 0.6–1% | Acceptable for cold B2B software | Optimize elsewhere |
| 1–2% | Good | Scale this creative |
| > 2% | Excellent | Scale aggressively; protect from fatigue |
 
### Diagnosing Creative Fatigue
 
Early warning signs (act before performance crashes):
- CTR declining 3+ weeks in a row
- CPA increasing 20%+ without audience change
- Frequency > 3 on cold audiences
- Negative/repetitive comments on ads
- CPM rising (Meta deprioritizing fatigued creative)
 
Response:
1. Duplicate winning ad set
2. Replace ads in duplicate with new creative variations
3. Don't pause the original until new creative is live and gathering data
4. Test new angle, not just new visuals
 
### Diagnosing Attribution Issues
 
Meta-reported conversions ≠ actual conversions. To understand the gap:
 
1. Compare Meta conversions to GA4 goal completions (same date range, GA4 source = "meta" or "facebook")
2. Compare Meta conversions to your backend signup/demo data
3. Calculate your blended CAC: total Meta spend ÷ actual new customers acquired
 
If Meta reports 100 conversions but GA4 shows 40 and your backend shows 35: Meta's view-through attribution is likely inflating reported conversions. Switch to 7-day click only attribution in Ads Manager for a more conservative (and more accurate) view.
 
### Weekly Review Checklist
 
**Spend & efficiency:**
- [ ] Spend vs. budget — on track?
- [ ] CPA vs. target — within ±30%? (Meta has more variance than Search)
- [ ] ROAS vs. target?
 
**Creative health:**
- [ ] Frequency by ad set — any cold ad sets above 3?
- [ ] CTR trend — declining week-over-week?
- [ ] Bottom-quartile ads — pause if frequency > 3 and CPA > 2× target
 
**Audience health:**
- [ ] Audience overlap between ad sets? (use Audience Overlap tool)
- [ ] Retargeting audience sizes — shrinking? (pixel/CAPI issue)
- [ ] Converters excluded from all prospecting?
 
**Tracking:**
- [ ] Pixel firing on all key events? (check Events Manager)
- [ ] CAPI events receiving? (check Events Manager → CAPI tab)
- [ ] Event match quality scores — above 6?
- [ ] Meta conversions vs. GA4/backend — reasonable ratio?
 
### Monthly Audit
 
- Creative refresh: any ad running > 6 weeks without refresh? Evaluate fatigue risk
- Audience performance: compare CPA by audience type — which seeds are producing best lookalikes?
- Placement breakdown: check CPA by placement — Audience Network often underperforms for software; consider excluding
- Attribution audit: recalculate blended CAC for the month
- Event quality: review CAPI event match quality; look for ways to send more user data parameters
 
---
 
## SCALING
 
### Signals You're Ready to Scale
 
- CPA stable and below target for 3+ consecutive weeks
- Pixel has 50+ weekly conversion events (learning phase exited)
- At least 1 winning creative identified (CTR > 1%, CPA on target)
- Conversion tracking verified clean
- Creative pipeline established (you have 3–5 new variations ready)
 
### Vertical Scaling (Increasing Budget)
 
- Increase budget maximum 20% per week to avoid triggering learning phase reset
- CBO campaigns tolerate larger increases than ABO (Meta redistributes internally)
- Monitor CPA for 7 days after each increase before increasing again
- If CPA spikes after increase: reduce budget back 10-15%, wait for stabilization
 
### Horizontal Scaling (Expanding Reach)
 
1. **Duplicate winning ad sets** with new audiences (new lookalike percentages, new interest clusters)
2. **Test new creative angles** — the biggest unlock for plateaued accounts
3. **Expand geographies** — add CA, GB, AU if US is saturated; localize copy for non-English markets
4. **Add placements** — if running feed only, test Stories and Reels with native 9:16 creative
5. **Add campaign types** — Advantage+ Shopping Campaigns (ASC) for e-commerce; Reels-specific campaigns
 
### The Creative Pipeline as Scaling Constraint
 
Most Meta accounts plateau not from audience exhaustion but from creative exhaustion. At scale, you need a system for continuous creative production:
 
**Minimum viable creative pipeline:**
- 2–3 new ad concepts tested per month
- Each concept: 1 video + 1 static (minimum)
- Winner identified after 2 weeks; scaled; loser paused
- Evergreen winners refreshed every 6–8 weeks (new hook, same concept)
 
**Creative types ranked by production cost vs. potential:**
 
| Format | Production cost | Ceiling |
|---|---|---|
| Screen recording + voiceover | Very low | Medium-high |
| Founder UGC talking head | Low | High |
| Customer testimonial video | Low-medium | High |
| Animated explainer | Medium | Medium |
| Professional video production | High | High (but not always better) |
| Static image (Canva/Figma) | Very low | Medium |
 
For most software companies, founder UGC + screen recordings outperform expensive production until very high spend levels.
 
### International Expansion
 
**Sequence:** US → English-speaking (GB, CA, AU, NZ) → Non-English with translated creative (DE, FR, ES, NL) → Emerging markets
 
**Before expanding:**
- Check GA4 for organic traffic by country — where are people already finding you?
- Check existing customer base — where do you already have customers?
- Confirm product works and support is available in the target market
 
**Localization minimum:** Translate ad copy and landing page. Don't just run English ads in non-English markets — CTR and CVR drop significantly.
 
### Advantage+ Shopping Campaigns (ASC)
 
Meta's most automated campaign type. Combines prospecting and retargeting in one campaign, uses all placements, optimizes automatically. Best for:
- Accounts with 50+ purchases/week
- Products with broad consumer appeal
- E-commerce or PLG with low-friction conversions
 
Not recommended for:
- Enterprise software with long sales cycles
- Developer tools with small TAM
- Accounts without mature pixel data
 
### When Meta Hits Its Ceiling
 
Signs you've reached the efficient frontier on Meta:
- Scaling budget increases CPA faster than volume
- New audiences and creative aren't improving CPA below a floor
- Blended CAC is acceptable but not improvable further
 
At this point: invest in improving the funnel (landing page CVR, trial activation, pricing) rather than Meta optimization. Or expand to complementary channels (LinkedIn for enterprise, YouTube for broad awareness, content/SEO for organic demand).
