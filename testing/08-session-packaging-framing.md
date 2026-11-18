# 08 — Session brief: packaging/gating framing (RH-for-customers)

Tags: `happy` `multi-mode` `framing`

## Question

> Using the Innovate Together IL AI skill, brief me on Aviran Badli’s packaging and gating models talk: what should I take away, and what should I try next?

## Skill response

## Brief: Packaging and Gating Models for OpenShift AI Inference

### Packaging and Gating Models for OpenShift AI Inference

- **When / who:** 11:55 (20 min) — Aviran (Abe) Badli; Uri Shaket (Red Hat) | LinkedIn: from speakers.md | GitHub: —
- **Summary:** How **Red Hat** runs a fail-closed Model Validation Program so “Validated by Red Hat” means signed ModelCar provenance, smoke-serve, and evals **before** a model hits the catalog — trust customers consume, not a DIY gate-building workshop.
- **Takeaways:** Validated = fail-closed RH chain; know what assurance the mark implies; map audit questions to attestations / failed-closed evidence.
- **Repos / docs:** OpenShift AI docs; Konflux; vLLM; Garak (context for what RH’s chain uses).
- **Contribute:** public eval tooling feedback; what auditors need to see under “Validated” (sanitized).
- **Try:** Map our approval questions to RH’s Validated chain; ask Red Hat where gaps remain — **not** “build a minimal ModelCar gate for our catalog.”
- **Materials:** slides-in-pack (outline in the talk file; no downloadable deck in this repo)

## Evaluation

| Criterion | Result | Notes |
|-----------|--------|-------|
| Correct mode | Pass | session brief |
| RH-for-customers framing | Pass | not customer DIY pipeline workshop |
| No DIY ModelCar “Try” | Pass | audit/map questions instead |
| Materials honesty | Pass | slides-in-pack; RH-for-customers framing, no invented claims |

**Verdict: good (pass)**

## Anti-pattern (fail if present)

- “Sketch a minimal ModelCar + smoke-serve gate for *your* internal catalog”
- Framing the session as teaching customers to rebuild Konflux/Enterprise Contract themselves

## Live agent delta

- Date / agent: — (pending)
- Drift vs hand-authored: —
- Re-eval verdict: —
