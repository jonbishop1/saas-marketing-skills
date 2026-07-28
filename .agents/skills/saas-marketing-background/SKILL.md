---
name: saas-marketing-background
description: >
  Shared intake background for SaaS marketing skills. This skill is not triggered directly — it holds the common intake questions, safe defaults, and routing logic used by saas marketing skills. Those skills reference this file by path. Do not delete or rename this skill if any marketing skills depend on it.
---
 
# SaaS Marketing background
 
This skill exists as a shared dependency. It contains the intake questions and safe defaults that skills all reference.
 
**File:** `references/background.md`
 
Any marketing skill that needs founder/product/audience background before advising should point here rather than maintaining its own copy.
 
 
### Updating this file
 
If you change the intake questions or safe defaults, the change applies to all skills automatically. That's the point — one source of truth.
