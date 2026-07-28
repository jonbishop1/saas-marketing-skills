# Context: SEO Intake Questions

Read this before advising. Gather missing background rather than giving generic recommendations. Many questions have safe defaults for software — noted below so you don't ask for information the user doesn't have yet.

---

## Questions to Ask

**Site & stack**
- What's the URL?
- What's the tech stack for public-facing pages? (Next.js, Astro, Gatsby, plain HTML, WordPress, Webflow, SPA framework) *(Matters for technical SEO — SSR vs. CSR changes the audit entirely)*
- Approximately how many public pages does the site have? (5, 50, 500, 5,000+)
- Is there a blog or content section? How many posts?
- Is there public documentation? Is it indexed?

**Current SEO state**
- Google Search Console set up? *(Safe default: assume no if they don't mention it)*
- Roughly how much organic traffic per month? *(Okay if they say "I don't know" — Search Console or analytics will tell us)*
- Any known SEO issues they're aware of?
- Have they done any SEO work before? What specifically?
- Any recent traffic drops or ranking changes they've noticed?
- Have they ever had a manual action from Google? *(Safe default: assume no)*

**Tools**
- Do they currently use any SEO tools? (Ahrefs, Semrush, Moz, SE Ranking, Screaming Frog, Surfer, etc.)
- If not, do they have budget for one? Roughly how much per month? *(Don't assume they should buy one — assess first)*
- Are they using Google Analytics or another analytics platform?

**Content**
- Who writes content currently? (Founder, co-founder, hired writer, agency, nobody)
- How often is new content published? *(Safe default: infrequently or never)*
- Is there a keyword strategy or content calendar, or is content published ad hoc?
- What topics do they want to rank for? (Even rough ideas are helpful)
- Do they have any content that ranks well already?

**Backlinks**
- Have they done any link building? What kind?
- Do they know roughly how many referring domains they have? *(Most won't — that's fine)*
- Are there industry publications, directories, or communities in their space?
- Any partnerships or integrations that could produce natural links?

**Competitors**
- Who are the 2–3 closest competitors in organic search? (May differ from product competitors)
- What do competitors seem to be doing well in SEO, in the founder's own words?
- What keywords do competitors appear to rank for?
- Are competitors running blogs, documentation, programmatic pages, or other content strategies?

**Time & resources**
- How many hours per week can they dedicate to SEO?
- Is it the founder doing this, or do they have someone (employee, contractor, agency)?
- What's the priority of SEO relative to other growth channels? (Primary channel, secondary, experimental?)

---

## Safe Defaults (don't ask, just apply)

| Parameter | Default |
|---|---|
| Search Console | Set up first if not already |
| Geographic target | United States (adjust if product is region-specific) |
| Language | English |
| Audit starting point | Technical → Content → Backlinks (in that order) |
| Content frequency | What the founder can sustain, not an ideal number |
| Tool recommendation | Free first, paid only if justified by site size/stage |
| Link building | Don't recommend until content foundation exists |
| Timeline expectations | 3–6 months for measurable organic growth |

---

## Routing After Intake

| Situation | Where to go |
|---|---|
| Pre-launch, no live site | SKILL.md → Pre-Launch: Speed to Ship. Stop there. |
| Live site, no Search Console | Set up Search Console first, then SKILL.md → Technical Audit |
| Live site, unknown organic traffic | Get into Search Console, establish baseline, then Situation Assessment |
| Has traffic but it's declining | SKILL.md → Technical Audit (check for indexation/crawl issues first) → Content Audit (check for content decay) |
| Has traffic, wants more | SKILL.md → Situation Assessment → Tiered Execution Plan |
| Specific question (e.g., "why don't I rank for X") | Answer the specific question first using relevant audit pillar, then broaden to full assessment if warranted |
| "Just audit my site" | SKILL.md → Situation Assessment → All three audit pillars at appropriate depth → Prioritized action plan |
