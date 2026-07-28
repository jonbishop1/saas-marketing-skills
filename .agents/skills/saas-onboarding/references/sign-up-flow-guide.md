# Signup Flow Design Guide

Complete guide to designing signup flows for SaaS products. Signup is the first conversion event in onboarding — everything that happens between "user clicks Sign Up" and "user is inside the product." This guide covers auth methods, form design, email verification, progressive profiling, mobile optimization, post-submit transitions, and conversion tracking.

---

## Table of Contents

1. [Why Signup Flow Matters](#why-signup-flow-matters)
2. [The Signup Pipeline](#the-signup-pipeline)
3. [Auth Method Strategy](#auth-method-strategy)
4. [Form Field Optimization](#form-field-optimization)
5. [Single-Step vs Multi-Step Forms](#single-step-vs-multi-step-forms)
6. [Email Verification Strategy](#email-verification-strategy)
7. [Progressive Profiling](#progressive-profiling)
8. [Mobile Signup Optimization](#mobile-signup-optimization)
9. [The Post-Submit Transition](#the-post-submit-transition)
10. [Security Considerations](#security-considerations)
11. [Signup Flow Measurement](#signup-flow-measurement)
12. [Tiered Signup Implementations](#tiered-signup-implementations)
13. [PingForge Signup Flow Design](#pingforge-signup-flow-design)
14. [KeyScope Signup Flow Design](#keyscope-signup-flow-design)
15. [Signup Anti-Patterns](#signup-anti-patterns)

---

## Why Signup Flow Matters

A user who clicks "Sign Up" or "Start Free Trial" has crossed the highest intent threshold on your marketing site. They've read the positioning, evaluated the offer, and decided to try. The only thing standing between that intent and a potential customer is the signup flow.

Every unnecessary step between "I want to try this" and "I'm using this" loses real users. The loss is invisible — they don't complain, they don't send feedback, they just close the tab. You'll never see them in your analytics because they never completed signup. They're the highest-quality leads you'll ever lose, and you lose them to friction.

The benchmark: best-in-class SaaS signup flows lose less than 20% of users between clicking "Sign Up" and landing in the product. Average flows lose 40–60%. Bad flows (many fields, email verification, separate login page) lose 60–80%.

---

## The Signup Pipeline

Break the signup flow into discrete stages and measure each:

```
Landing page CTA clicked        100%  ← This is your baseline
├─ Signup page loaded             95%  ← 5% loss: page speed, redirects
├─ Form interaction started       85%  ← 10% loss: form looks overwhelming, second thoughts
├─ Form submitted                 70%  ← 15% loss: too many fields, validation errors, friction
├─ Email verified (if required)   55%  ← 15% loss: inbox switching, spam folders, delays
├─ First product screen loaded    50%  ← 5% loss: redirects, loading, confusion
└─ First meaningful action taken  35%  ← 15% loss: blank screen, no guidance (this is onboarding, not signup)
```

The numbers above are illustrative but realistic for a typical SaaS flow with email/password signup and email verification. Every row is a point you can optimize. The goal: make each stage as close to 100% of the previous as possible.

---

## Auth Method Strategy

The auth method decision has the single largest impact on signup completion rate. Social auth reduces friction by 20–40% compared to email/password because it eliminates typing, password creation, and (in most cases) email verification.

### Auth method comparison

| Method | Friction | Completion rate impact | Best for |
|---|---|---|---|
| **Google OAuth ("Sign up with Google")** | Very low (2 clicks, zero typing) | +25–40% vs email/password | B2B SaaS, any product where users have Google accounts |
| **GitHub OAuth** | Very low | +30–40% for developer audience | Developer tools, API products, technical audiences |
| **Microsoft/Azure AD** | Very low | +20–30% for enterprise | Enterprise products, Microsoft ecosystem |
| **SSO (SAML/OIDC)** | Low for enterprise users | Required for enterprise, not relevant for self-serve | Enterprise-tier features, compliance-driven sales |
| **Magic link (passwordless email)** | Low (type email, click link in inbox) | +10–20% vs email/password | Low-frequency products, security-conscious audiences |
| **Email + password** | Highest (type email, create password, possibly verify) | Baseline | Fallback option, always offer alongside social |
| **Phone/SMS** | Medium | Varies — high in mobile-first markets, lower in B2B | Mobile-first products, markets where email isn't primary |

### Decision framework

**Step 1: Identify your audience's dominant auth ecosystem.**
- If your users are developers → GitHub + Google + email/password
- If your users are business professionals → Google + Microsoft + email/password
- If your users are enterprise → SSO (SAML) + Google/Microsoft + email/password
- If your audience is mixed → Google + email/password (Google is the universal option)

**Step 2: Lead with social auth.**
The social auth button should be the most prominent option on the signup page — above the email/password form, larger, more visually weighted. Many users will default to whatever is at the top of the page. Make the low-friction option the default path.

```
┌──────────────────────────────┐
│                              │
│  Start your free trial       │
│                              │
│  ┌────────────────────────┐  │
│  │  🔵 Sign up with Google │  │  ← Primary: most prominent
│  └────────────────────────┘  │
│  ┌────────────────────────┐  │
│  │  ⚫ Sign up with GitHub  │  │  ← Secondary (if dev audience)
│  └────────────────────────┘  │
│                              │
│  ──── or use email ────      │
│                              │
│  Email: [________________]   │
│  Password: [_____________]   │  ← Fallback: below the fold line
│                              │
│  ┌────────────────────────┐  │
│  │    Create account       │  │
│  └────────────────────────┘  │
│                              │
│  By signing up, you agree    │
│  to our Terms and Privacy.   │
└──────────────────────────────┘
```

**Step 3: Minimize email/password friction when it's used.**
Some users will always prefer email/password (privacy concerns, corporate policies, personal preference). For those users: 2 fields maximum (email + password), clear password requirements shown before they type (not as error messages after), and no separate "confirm password" field (use a show/hide toggle instead).

### Implementing social auth

For technical founders, social auth implementation is straightforward:
- **Google:** Google Identity Services (the new API). OAuth 2.0 consent flow. Returns email, name, and profile picture.
- **GitHub:** OAuth App or GitHub App. Returns email (if public), username, and avatar.
- **Microsoft:** Microsoft Identity Platform. OAuth 2.0 + OpenID Connect. Returns email, name, and tenant info.

All three follow the same pattern: redirect to provider → user authorizes → callback with auth code → exchange for token → create account with returned profile data.

Libraries: `passport.js` (Node), `omniauth` (Ruby), `social-auth-app-django` (Python), `socialite` (Laravel), `next-auth` (Next.js). These abstract the OAuth flow to a few lines of configuration.

**The key implementation decision:** When a user signs up with Google and later tries to sign in with email/password (or vice versa), what happens? The cleanest approach: link accounts by email address. If someone signs up with Google using `alice@company.com`, and later tries email/password login with the same address, link the accounts automatically and let them use either method. Don't create a confusing "account already exists" error.

### When to add SSO

SSO (SAML/OIDC) is an enterprise requirement, not a self-serve feature. Add it when:
- Enterprise deals are stalling because IT requires SSO
- You're selling to companies with 100+ employees
- Compliance frameworks (SOC 2, HIPAA) require centralized auth

SSO is a selling feature, not an onboarding feature. It doesn't improve signup flow for self-serve users — it enables a different class of buyer.

---

## Form Field Optimization

### The field reduction principle

Every form field has a cost (completion rate reduction) and a value (information gained). Most SaaS signup forms have fields that cost more than they're worth.

| Field | Cost (drop-off per field) | Value | Verdict |
|---|---|---|---|
| **Email** | Required — baseline | Account identifier, communication channel | Always include |
| **Password** | Low (expected) | Authentication | Include for email/password; skip for social auth |
| **Full name** | ~5% drop | Personalization, email addressing | Include if you'll use it in-product ("Welcome back, Alice"); skip if it sits unused in a database |
| **Company name** | ~8% drop | CRM enrichment, segmentation | Collect later via progressive profiling or enrich from email domain |
| **Team size** | ~8% drop | Sales qualification | Collect later or infer from behavior |
| **Phone number** | ~12% drop | Sales outreach | Almost never justified at signup for self-serve |
| **Job title / role** | ~8% drop | Personalization, segmentation | Only if it drives meaningfully different onboarding paths |
| **How did you hear about us?** | ~5% drop | Attribution | Capture via UTM parameters instead — never ask the user |
| **Company URL / domain** | ~5% drop | Enrichment, product setup | Only if the product needs it immediately (like KeyScope's domain input) |

### The minimum viable signup

**For most PLG SaaS:** Email + password. Two fields. That's it.

If your product needs a domain or URL to function (like KeyScope needs the user's domain for gap analysis, or PingForge needs an endpoint URL), collect that as the first action inside the product, not in the signup form. Signup creates the account. The product collects what it needs to deliver value.

**Exception — when extra fields earn their cost:** If asking "What's your role?" at signup allows you to personalize the welcome experience so dramatically that activation rates increase more than the signup drop-off, the field pays for itself. But you need data to prove this. Don't add fields on a hunch that they'll help personalization — add them when you've tested and confirmed the personalization actually moves activation.

### Form validation

Bad form validation is a silent signup killer. Users encounter an error, get frustrated, and leave.

**Principles:**
- **Validate inline, not on submit.** Show validation feedback as the user fills each field, not after they click "Create account." An email field that turns red the moment they leave it (with "Please enter a valid email") is better than a form submission that bounces with errors at the top.
- **Show password requirements upfront.** Display "8+ characters, one uppercase, one number" before the user types, not as an error message after they've typed something that doesn't meet the requirements. Even better: use a simple requirement (8+ characters, no other rules) and show a strength meter.
- **Be forgiving on format.** Accept "alice@company.com" and "  alice@company.com  " (with whitespace). Auto-trim. Don't reject an email because it has a trailing space.
- **Don't block on non-critical fields.** If you ask for a company name but it's not required for the product to work, don't make it a required field. Mark it optional or collect it later.

### Autofill and password managers

Design the form so autofill and password managers work correctly. This means:
- Use standard HTML `name` and `autocomplete` attributes (`autocomplete="email"`, `autocomplete="new-password"`)
- Don't use custom JavaScript inputs that break autofill
- Don't disable paste on password fields (this infuriates password manager users)
- Test with 1Password, LastPass, and browser autofill — if any of them fail, fix the form

---

## Single-Step vs Multi-Step Forms

### When to use single-step

- 2–3 fields total
- No conditional logic needed
- Product is simple enough that signup is a one-action event

Single-step is the default for most SaaS products. Two fields (email + password) on one page, one submit button, done.

### When to use multi-step

- 4+ fields are genuinely necessary before the user can enter the product
- Some fields are conditional on previous answers (role determines next questions)
- You want to capture the email first (so you can re-engage abandoners)

Multi-step advantages:
- Each step feels lighter than a long single form
- You can capture the email on step 1 and send an abandonment email if they don't complete
- Conditional logic can skip irrelevant steps

Multi-step disadvantages:
- Adds perceived effort (even if total effort is the same, "step 1 of 3" feels like more work)
- Each step transition is a drop-off point
- More complex to implement

### Multi-step structure (when justified)

```
Step 1: Account creation (email + password or social auth)
  → This step should complete account creation so you have
    a reachable user even if they abandon later steps

Step 2: Context that serves the user (role, goal, use case)
  → Only fields that change the experience
  → "Skip" option on every step after step 1

Step 3: Product-specific setup (domain, team name, etc.)
  → Only if truly needed before entering the product
  → Can often be deferred to in-product setup
```

**The email-first pattern:** Capture just the email on step 1. If the user abandons after step 1, you have their email and can send a "Finish setting up your account" email. This recovers 5–15% of abandoned signups.

---

## Email Verification Strategy

Email verification is one of the most consequential UX decisions in the signup flow. It adds a step that takes the user out of your product and into their email inbox — a hostile environment full of distractions.

### The verification decision matrix

| Scenario | Recommended approach | Reasoning |
|---|---|---|
| **PLG, self-serve, low ACV** | Defer verification | Let users in immediately. Require verification before a high-trust action (inviting team, exporting data, connecting integrations). |
| **PLG, self-serve, handling sensitive data** | Verify upfront with magic link | Security matters, but don't send them to a dead-end "check your email" page — use a magic link that logs them in automatically when clicked. |
| **Free tier / freemium** | Defer verification | Free users should get in as fast as possible. Verify when they do something that requires a verified identity. |
| **Social auth (Google/GitHub)** | No verification needed | The OAuth provider has already verified the email. Don't verify again. |
| **Sales-led / enterprise** | Verify upfront | Higher-intent users expect security. The friction is acceptable because the user is more committed. |

### Deferred verification pattern

The user signs up and enters the product immediately. A non-blocking banner appears:

```
┌─────────────────────────────────────────────────────────────┐
│ ✉️  Please verify your email to unlock all features.         │
│    We sent a link to alice@company.com.  [Resend]  [Later]  │
└─────────────────────────────────────────────────────────────┘
```

What's gated behind verification:
- Inviting team members
- Connecting third-party integrations
- Exporting data
- Changing account email or billing
- Anything with security implications

What's NOT gated:
- Using the product's core features
- Reaching the activation moment
- Exploring the full UI

This approach lets users experience value first and verify when they're already engaged. Verification rates are actually higher with deferred verification because the user is now motivated to unlock features they've already seen.

### Magic link verification

Instead of "click this link to verify your email," send a magic link that both verifies AND logs the user in:

```
Subject: Verify your KeyScope account

[One-click button: "Verify and open KeyScope →"]

Clicking this link verifies your email and takes you straight to your account.
```

The user clicks one link and is verified + logged in + inside the product. No separate login step. This is strictly better than traditional verification for the user experience.

### Implementation notes

- Verification emails should be transactional (sent via SendGrid, Postmark, SES, Resend — not your marketing email tool). Deliverability matters.
- Send immediately. A verification email that arrives 5 minutes later has a much lower click rate than one that arrives in 10 seconds.
- If the email doesn't arrive (spam filters, typos), make "Resend" prominent and allow email correction without creating a new account.
- Set verification tokens to expire in 24–48 hours — long enough for the user to find it, short enough for security.

---

## Progressive Profiling

### What it is

Collecting user information over time rather than all at signup. Instead of a 6-field form at signup, you ask 2 fields at signup, 1 field during onboarding, 1 field when they hit a feature gate, and 2 fields never (you infer them from behavior or enrich from the email domain).

### The progressive profiling timeline

| When | What to collect | How |
|---|---|---|
| **Signup** | Email, password (or social auth) | Signup form |
| **Welcome screen** | Role or primary goal (1 question) | In-app modal (only if it changes the experience) |
| **First session** | Nothing — let them use the product | — |
| **After activation** | Team size, company name | In-context prompt ("Invite your team to KeyScope") |
| **After value milestone** | Use case detail, industry | Micro-survey after they've seen value |
| **Never (infer instead)** | Company size, industry, location | Enrich from email domain via Clearbit, Apollo, or similar |
| **Never (track instead)** | How they heard about you | UTM parameters, first-touch attribution |

### Data enrichment as a signup shortcut

For B2B SaaS, the user's email domain tells you a lot. Tools like Clearbit, Apollo, or ZoomInfo can take `alice@stripe.com` and return: company name (Stripe), employee count (8,000+), industry (financial technology), location (San Francisco), and more.

This means you can skip asking "company name," "company size," "industry," and "location" at signup. The user types their email, and you know all of this in the background.

Cost: $100–500/month for enrichment APIs. Worth it when your signup volume justifies it (usually 200+ signups/month) and you use the data to personalize onboarding or qualify leads.

### Micro-surveys after value delivery

The best time to ask users questions is after they've received value — not before. A user who just completed their first keyword gap analysis and found 147 opportunities is in a positive, engaged state. That's the moment to ask: "What's your primary goal with KeyScope?" or "How large is your SEO team?"

Micro-surveys after value delivery get 3–5× higher completion rates than the same questions at signup, because the user is now invested and sees the relationship as reciprocal.

---

## Mobile Signup Optimization

30–60% of SaaS marketing site traffic is mobile. Even for B2B products, users discover and evaluate from their phones (reading about tools during commutes, clicking links from social media, forwarding trial links to personal devices).

### Mobile-specific signup principles

- **Social auth is even more critical.** Typing an email and creating a password on a mobile keyboard is 3–5× slower than desktop. "Sign up with Google" is one tap. This alone can double mobile signup completion.

- **Use appropriate input types.** `<input type="email">` shows the email keyboard (with @ and .com). `<input type="password">` triggers password manager suggestions. `<input type="tel">` shows the number pad. These small HTML attributes have outsized UX impact on mobile.

- **Make touch targets large.** Buttons should be minimum 48×48px (Apple HIG and Material Design both recommend this). Form fields should have generous padding. The "Sign up with Google" button should be easy to tap with a thumb.

- **Avoid horizontal scrolling.** The form should be single-column and fit within the viewport width. No side-scrolling forms.

- **Test on actual devices.** Not just Chrome DevTools responsive mode. Actual iPhones and Android phones. There are rendering differences, keyboard behaviors, and autofill behaviors that only appear on real devices.

- **Consider the mobile-to-desktop handoff.** Some users will discover your product on mobile but prefer to use it on desktop (especially for complex products). Make this easy: after mobile signup, send an email with a direct login link they can open on their desktop. Don't make them remember a password they created on their phone 3 hours ago.

### Mobile signup flow layout

```
┌─────────────────────────┐
│                         │
│  Start your free trial  │
│                         │
│  ┌───────────────────┐  │
│  │ 🔵 Continue with   │  │  ← Full-width, large tap target
│  │    Google          │  │
│  └───────────────────┘  │
│                         │
│  ┌───────────────────┐  │
│  │ ⚫ Continue with   │  │
│  │    GitHub          │  │
│  └───────────────────┘  │
│                         │
│  ─── or use email ───   │
│                         │
│  Email                  │
│  ┌───────────────────┐  │
│  │                   │  │  ← Large input, type="email"
│  └───────────────────┘  │
│                         │
│  Password               │
│  ┌───────────────────┐  │
│  │              👁️    │  │  ← Show/hide toggle, no confirm field
│  └───────────────────┘  │
│  8+ characters          │
│                         │
│  ┌───────────────────┐  │
│  │   Create account   │  │  ← Full-width button
│  └───────────────────┘  │
│                         │
│  By signing up you      │
│  agree to Terms.        │
└─────────────────────────┘
```

---

## The Post-Submit Transition

The moment between clicking "Create account" and seeing the product for the first time is surprisingly important. A poor transition — slow loading, confusing redirects, a "check your email" dead end — kills momentum at the exact moment the user is most eager to explore.

### Principles

- **Instant.** The user clicks submit and the product appears. Ideally under 2 seconds. If account creation involves background work (provisioning, enrichment), do it asynchronously and let the user in immediately.
- **No detours.** Don't redirect to a "check your email" page (if using deferred verification). Don't redirect to a separate login page. Don't show a "Your account has been created! Click here to log in" page. Every intermediate page is an off-ramp.
- **Continuity of intent.** The user wanted to try your product. The first thing they should see is the product (with a welcome experience). Not a billing page. Not an "about us" page. Not a blog post.
- **Loading state with context.** If there's any loading time, show a meaningful loading state: "Setting up your workspace..." with a progress indicator. Not a blank screen. Not a spinner with no text.

### Post-submit patterns by auth method

| Auth method | Ideal post-submit flow |
|---|---|
| **Social auth (Google/GitHub)** | OAuth redirect → callback → auto-create account → redirect to product with welcome screen. Should feel like 2 clicks total. |
| **Email + password (no verification)** | Submit form → create account → redirect to product with welcome screen. No intermediate page. |
| **Email + password (deferred verification)** | Submit form → create account → redirect to product with welcome screen + verification banner. |
| **Email + password (upfront verification)** | Submit form → show inline "Check your email" message on the same page (not a redirect). Email contains a magic link that logs in + verifies simultaneously. |
| **Magic link** | Submit email → show inline "Check your email" message. Magic link opens the product directly, no password needed. |

### The "check your email" dead end

This is the worst post-submit experience in SaaS signup:

```
❌  "Please check your email and click the verification link to continue."
    [That's it. No product access. No alternative. Just wait.]
```

The user leaves your site, opens their inbox, gets distracted by 47 other emails, forgets about your product, and never comes back. You've lost a user who was ready to try your product.

**If you must verify upfront,** stay on the same page, show a clear "email sent" state, include a "Resend" button and a "Wrong email?" correction option, and use a magic link that logs the user in automatically when clicked. Don't send them to a separate page.

---

## Security Considerations

Signup flow design involves real security tradeoffs. Here's how to think about them:

### Rate limiting

Protect against bot signups and brute force without adding friction for real users:
- Rate limit by IP address (max 5 signup attempts per hour per IP)
- Use invisible reCAPTCHA v3 (scores requests without user interaction) for the signup endpoint
- Only escalate to visible CAPTCHA if the invisible score is suspicious
- Never default to visible CAPTCHA for all users — it adds friction for everyone to stop a small number of bots

### Password policy

- **Minimum 8 characters** is sufficient for most SaaS products. Don't require uppercase + lowercase + number + special character — this creates passwords like "Password1!" that are weak but pass the rules. Length matters more than complexity.
- **Check against breached password lists** (HaveIBeenPwned's API offers this). If the password appears in a known breach, warn the user but don't necessarily block them.
- **Show a strength meter** instead of rigid rules. Users create better passwords when guided by a strength meter than when forced to include specific character types.

### OAuth security

- Always verify the email returned by the OAuth provider. Google returns verified emails; GitHub emails may be unverified.
- Use `state` parameter in OAuth flows to prevent CSRF attacks.
- Store access tokens securely. Don't expose them in URLs or frontend storage.

---

## Signup Flow Measurement

### Events to track

| Event | What it tells you |
|---|---|
| `signup_page_viewed` | How many people reach the signup page |
| `signup_form_interacted` | How many start filling the form (first field focused or social auth clicked) |
| `signup_form_submitted` | How many attempt to create an account |
| `signup_validation_error` | How many hit a validation error (and which field) |
| `signup_completed` | How many successfully create an account |
| `email_verification_sent` | How many receive a verification email |
| `email_verification_clicked` | How many click the verification link |
| `first_product_screen_viewed` | How many land in the product |
| `signup_method` (property) | Which auth method was used (google, github, email) |

### Key ratios

| Ratio | Benchmark | If below benchmark |
|---|---|---|
| Page viewed → form interacted | > 85% | The form looks overwhelming, or the page has UX issues |
| Form interacted → submitted | > 75% | Too many fields, confusing validation, slow page |
| Submitted → completed | > 90% | Backend errors, confusing error messages, duplicate account handling |
| Completed → email verified (if required) | > 65% | Emails landing in spam, verification too slow, user lost interest |
| Completed → first product screen | > 90% | Post-submit transition problem (redirects, loading, dead ends) |

### A/B testing signup flows

Signup flow A/B tests reach significance faster than most other tests because signup is high-volume and the conversion event is immediate. If you have 500+ signups/month, you can test meaningful variations in 2–4 weeks.

High-impact tests to run:
1. Social auth prominent vs. email/password prominent (usually social auth wins)
2. Fewer form fields vs. current fields (fewer usually wins)
3. Single-step vs. multi-step (depends on field count — test it)
4. Deferred verification vs. upfront verification (deferred usually wins for PLG)
5. With vs. without personalization question at signup (depends on how you use the answer)

---

## Tiered Signup Implementations

### Tier 1 — Minimum viable signup (1 day to build)

- Email + password form (2 fields)
- No email verification (defer until needed)
- Basic validation (email format, password length)
- Direct redirect to product after submission
- Track: signup_completed event

**What you sacrifice:** No social auth (higher friction), no enrichment, no progressive profiling. But it works, it's fast to build, and you can improve it later.

### Tier 2 — Optimized signup (2–3 days to build)

- Google OAuth + email/password
- Add GitHub OAuth if developer audience
- Deferred email verification with in-app banner
- One personalization question in welcome screen (not signup form)
- Basic rate limiting (IP-based)
- Track: full event funnel

**What you sacrifice:** No data enrichment, no advanced bot protection, no A/B testing infrastructure.

### Tier 3 — Full-featured signup (1 week to build + ongoing)

- Multiple social auth options + email/password + SSO
- Deferred verification with magic links
- Progressive profiling (signup → welcome → post-activation)
- Data enrichment from email domain
- Invisible reCAPTCHA + rate limiting
- Full event tracking with funnel analytics
- A/B testing on form variations

---

## PingForge Signup Flow Design

### Recommended: Tier 2

PingForge's audience is developers. The signup flow should be fast, technical-audience-friendly, and get them to "paste your first endpoint" as quickly as possible.

```
┌──────────────────────────────────┐
│                                  │
│  Start monitoring your APIs      │
│  Free for up to 5 endpoints      │
│                                  │
│  ┌────────────────────────────┐  │
│  │  ⚫ Sign up with GitHub     │  │  ← Primary for developer audience
│  └────────────────────────────┘  │
│  ┌────────────────────────────┐  │
│  │  🔵 Sign up with Google    │  │
│  └────────────────────────────┘  │
│                                  │
│  ──── or ────                    │
│                                  │
│  Email: [____________________]   │
│  Password: [________] 👁️         │
│  8+ characters                   │
│                                  │
│  ┌────────────────────────────┐  │
│  │    Create account           │  │
│  └────────────────────────────┘  │
│                                  │
│  Already have an account? Log in │
└──────────────────────────────────┘
```

**Key decisions:**
- **GitHub first.** Developer audience, GitHub is the identity they trust for technical tools.
- **No name field.** PingForge doesn't need the user's name to deliver value. If needed for email personalization later, pull it from the GitHub/Google profile or ask in-product.
- **No email verification.** API monitoring is not high-security at the signup stage. Verify later when they connect Slack/PagerDuty integrations.
- **"Free for up to 5 endpoints" below the headline.** Reduces anxiety about commitment before the user even starts filling the form.

**Post-submit:** Direct to the empty dashboard with the inline "Add your first endpoint" form. No intermediate pages.

---

## KeyScope Signup Flow Design

### Recommended: Tier 2 with one twist

KeyScope's audience is a mix of SEO professionals, content marketers, and technical founders. The signup flow should accommodate both technical and non-technical users.

```
┌──────────────────────────────────┐
│                                  │
│  Find your keyword gaps          │
│  Free for 14 days, no CC needed  │
│                                  │
│  ┌────────────────────────────┐  │
│  │  🔵 Sign up with Google    │  │  ← Primary: universal for this audience
│  └────────────────────────────┘  │
│                                  │
│  ──── or ────                    │
│                                  │
│  Email: [____________________]   │
│  Password: [________] 👁️         │
│  8+ characters                   │
│                                  │
│  ┌────────────────────────────┐  │
│  │    Start free trial         │  │
│  └────────────────────────────┘  │
│                                  │
│  Already have an account? Log in │
└──────────────────────────────────┘
```

**Key decisions:**
- **Google first, no GitHub.** KeyScope's audience is broader than developers. Google is the universal option. GitHub would confuse non-technical SEO professionals.
- **"Free for 14 days, no CC needed" below the headline.** Addresses the two biggest trial anxieties: cost and commitment.
- **No role/goal question at signup.** KeyScope already asks "What's your primary use case?" on the welcome screen (post-signup). Asking it in the signup form would add friction at the wrong stage.
- **Deferred email verification.** Let users run their first gap analysis before asking them to verify. By that point they've experienced value and have motivation to complete verification.

**The twist — domain input as the first in-product action, not in signup:**

Some SaaS products put their primary input (domain, URL, etc.) in the signup form to combine signup + first action. For KeyScope, this would mean:

```
Email: [__________]  Password: [__________]
Your domain: [__________]  ← Combined signup + first product action
```

**Don't do this.** It conflates two decisions (creating an account vs. starting analysis) and makes the form feel heavier. Instead, the domain input appears as the first in-product experience on the empty state screen after signup. This separates "I'm creating an account" from "I'm using the product" and keeps each step feeling lightweight.

---

## Signup Anti-Patterns

Common signup flow mistakes — watch for these and flag them proactively:

1. **The "complete your profile" wall.** After signup, a mandatory 5-field "complete your profile" form blocks access to the product. The user already signed up — let them in. Collect profile data progressively.

2. **CAPTCHA by default.** Visible CAPTCHAs for every signup punish real users for the behavior of bots. Use invisible reCAPTCHA and only escalate to visible challenges when the risk score is high.

3. **"Confirm password" fields.** These don't prevent password errors — users just copy-paste from the first field. Use a show/hide toggle instead. It's better UX and catches more actual typos.

4. **Separate signup and login pages with no cross-linking.** A user who already has an account and lands on the signup page (or vice versa) should be able to switch with one click. "Already have an account? Log in" and "Don't have an account? Sign up" should be prominent.

5. **OAuth that asks for too many permissions.** "Sign up with Google" that requests access to contacts, calendar, and drive scares users. Request only the permissions you actually need (email + profile for signup). Request additional permissions later, in context, when the user is using the feature that needs them.

6. **No error recovery for duplicate emails.** User tries to sign up with an email that already has an account. Bad: "An account with this email already exists." Good: "An account with this email already exists. [Log in instead →] or [Reset your password →]."

7. **Forcing terms/privacy checkbox.** A mandatory "I agree to Terms of Service and Privacy Policy" checkbox adds a field and a decision. Better: "By signing up, you agree to our Terms and Privacy Policy" as text below the submit button. Same legal coverage, zero friction.

8. **Success page instead of success action.** After signup: "Your account has been created! Click here to get started." That intermediate page is unnecessary. Just redirect them to the product. The "success" is seeing the product, not reading that the signup worked.
