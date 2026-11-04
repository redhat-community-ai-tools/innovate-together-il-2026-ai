# Packaging and Gating Models for OpenShift AI Inference

- **Time:** 11:55 (20 min)
- **Speakers:** Aviran (Abe) Badli; Uri Shaket (Red Hat)
- **Slides:** Coming soon
- **Related abstract title:** Chain of Trust: The Hidden System Behind Validated AI Models

## Abstract

Enterprise AI trust is not a leaderboard badge — it is whether a model runs on supported OpenShift / OpenShift AI with Red Hat AI Inference Server and vLLM on real GPUs without silent stack breaks. Red Hat’s Model Validation Program backs the “Validated by Red Hat” mark: Hugging Face weights → signed OCI / ModelCar on Konflux (hash, scan, attest, Enterprise Contract), smoke serve with vLLM, then measure with GuideLLM, Garak, EvalHub across hardware/framework/container combos. Fail closed before the catalog shows the model.

## Takeaways to borrow

- Treat models as signed supply-chain artifacts (ModelCar), not loose weight files
- Gate: package → smoke serve → security/perf/accuracy → catalog
- “Validated” means a failed-closed chain, not marketing copy

## Repos & docs

- OpenShift AI docs: https://docs.redhat.com/en/documentation/red_hat_openshift_ai
- Konflux: https://konflux-ci.dev/
- vLLM: https://github.com/vllm-project/vllm
- Garak (LLM vulnerability scanner): https://github.com/NVIDIA/garak

## Contribution opportunities

- Upstream eval tooling (GuideLLM / EvalHub / Garak integrations) where public
- Share ModelCar packaging patterns and failed-closed CI examples (sanitized)

## Try this in your environment

Ask: “What would a minimal ModelCar + smoke-serve gate look like before we promote a model to our internal catalog?”
