# Chain of Trust: The Hidden System Behind Validated AI Models

- **Time:** 11:55 (20 min)
- **Speakers:** Aviran (Abe) Badli; Uri Shaket (Red Hat)
- **Materials:** slides-in-pack
- **Slug:** `packaging-gating-models` (kept for stable agent matching)
- **Framing:** How **Red Hat** validates and gates models **for customers** (catalog trust / “Validated by Red Hat”) — not a workshop on rebuilding that pipeline yourself.

## Abstract

Enterprise AI trust is not a leaderboard badge — it is whether a model runs on supported OpenShift / OpenShift AI with Red Hat AI Inference Server and vLLM on real GPUs without silent stack breaks. Red Hat’s Model Validation Program backs the “Validated by Red Hat” mark: Hugging Face weights → signed OCI / ModelCar on Konflux (hash, scan, attest, Enterprise Contract), smoke serve with vLLM, then measure with GuideLLM, Garak, EvalHub across hardware/framework/container combos. Fail closed before the catalog shows the model.

## Outline (from deck)

1. **Mission** — customers choose/deploy models with confidence: performance, accuracy, integration, Red Hat trust mark
2. **Scope of the validation program** — validate new model releases on supported products; source of truth for model–product support; provenance / licensing / basic security; performance & accuracy benchmarks; visibility across Selection → Packaging → Validation → Benchmarking → Publish to AI Hub
3. **Out of scope** — product QA ownership, product-specific tests, debugging product bugs, release go/no-go, writing security tests for the product itself
4. **Priorities called out** — Model Catalog integration; validate/benchmark many new models; automate validation; self-serve benchmarking on RHOAI; move from static validation toward continuous / post-deploy alignment
5. **Toolchain named** — GuideLLM, LM-Eval / EvalHub, Garak, Konflux / ModelCar / Enterprise Contract, vLLM smoke serve
6. **Customer lens** — ask what attestations exist, what failed closed, which hardware/stack combos were exercised

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
