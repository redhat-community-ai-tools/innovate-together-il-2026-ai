# 06 — Project match: confidential / regulated inference

Tags: `happy`

## Question

> Using the Innovate Together IL AI skill: we need confidential inference for a regulated workload. Which talk, docs, and upstream projects apply?

## Skill response

## Relevant talks

### Leveraging Sandboxing and Confidential Computing for Agents and Models — why it fits
- **Borrow:** Split agent-code sandbox (Kata / agent-sandbox) vs confidential inference (confidential containers + KServe) so model/weights/data are protected from a malicious admin.
- **Try:** Threat-model admin vs agent code vs model theft; pick the matching control first.
- **Repos / docs:** [Kata](https://katacontainers.io/), [Confidential Containers](https://confidentialcontainers.org/), [KServe](https://kserve.github.io/website/)
- **Contribute:** Upstream CoCo/KServe AI inference UX; internal ADR for the threat model.

### Packaging and Gating Models for OpenShift AI Inference — why it fits
- **Borrow:** Fail-closed package → smoke-serve → eval before confidential prod serves new weights (ModelCar / validated chain).
- **Try:** “No unsigned weights in prod” gate before the confidential cluster serves anything new.
- **Repos / docs:** OpenShift AI docs; Konflux; vLLM; Garak
- **Contribute:** Public-safe packaging CI examples

## Suggested next step

One-page threat model, then spike confidential containers + KServe for a non-prod model behind a packaging gate.

## Evaluation

| Criterion | Result | Notes |
|-----------|--------|-------|
| Talk selection | Pass | 2 deep talks; skipped soft framing |
| Grounded | Pass | |
| Sales | Pass | |

**Verdict: good (pass)**

## Live agent delta

- Date / agent: 2026-11-05 / Cursor (Composer)
- Drift vs hand-authored: Negligible — confidential + packaging gates; 2 deep talks.
- Re-eval verdict: **pass**
- Full live text: [live-runs/2026-11-05-cursor.md](live-runs/2026-11-05-cursor.md#q06--confidential-inference)
