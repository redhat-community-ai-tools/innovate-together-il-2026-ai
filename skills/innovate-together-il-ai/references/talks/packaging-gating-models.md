# Chain of Trust: The Hidden System Behind Validated AI Models

- **Time:** 11:55 (20 min)
- **Speakers:** Aviran (Abe) Badli; Uri Shaket (Red Hat)
- **Materials:** slides-in-pack
- **Slug:** `packaging-gating-models` (kept for stable agent matching)
- **Framing:** How **Red Hat** validates and gates models **for customers** (catalog trust / “Validated by Red Hat”) — not a workshop on rebuilding that pipeline yourself.
- **Note:** Deck + demos in organizer [AI-track Drive / Chain of Trust folder](https://drive.google.com/drive/folders/1hxS5yvWr1a3pkEj1bCFVmSqgrWvW0de2) (access-controlled).

## Abstract

Enterprise AI trust is not a leaderboard badge — it is whether a model runs on supported OpenShift / OpenShift AI with Red Hat AI Inference Server and vLLM on real GPUs without silent stack breaks. Red Hat’s Model Validation Program backs the “Validated by Red Hat” mark: Hugging Face weights → signed OCI / ModelCar on Konflux (hash, scan, attest, Enterprise Contract), smoke serve with vLLM, then measure with GuideLLM, Garak, EvalHub across hardware/framework/container combos. Fail closed before the catalog shows the model.

## Takeaways to borrow

- “Validated by Red Hat” means a fail-closed chain Red Hat runs before a model appears in the catalog — not a marketing badge
- What you get as a customer: signed/attested ModelCar provenance plus smoke-serve and eval evidence behind the mark
- Useful audit questions: what attestations exist, what failed closed, what hardware/stack combos were exercised

## Repos & docs

- OpenShift AI docs: https://docs.redhat.com/en/documentation/red_hat_openshift_ai
- Konflux: https://konflux-ci.dev/
- vLLM: https://github.com/vllm-project/vllm
- Garak (LLM vulnerability scanner): https://github.com/NVIDIA/garak

## Contribution opportunities

- Upstream eval tooling (GuideLLM / EvalHub / Garak integrations) where public
- Feedback on what “Validated” evidence auditors need to see (sanitized)

## Try this in your environment

Ask: “For models we consume from Red Hat’s catalog, which Validated-chain checks map to our approval / audit questions — and what should we ask Red Hat if a gap remains?”
