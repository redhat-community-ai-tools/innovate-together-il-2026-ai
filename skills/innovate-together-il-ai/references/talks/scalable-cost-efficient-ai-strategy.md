# Building a Scalable, Cost-Efficient AI Strategy with Red Hat AI

- **Time:** 11:05 (30 min)
- **Speakers:** Roy Nissim (Senior Manager, Engineering / Inference Lead, Red Hat AI)
- **Materials:** slides-in-pack

## Abstract

As enterprise AI moves from experiment to production, teams hit surging inference bills, fragmented tooling, and observability gaps. This session covers Red Hat’s Hybrid Inference Strategy: a unified AI gateway (observability, token management, intelligent routing across self-hosted and external models), a curated validated model catalog, and a high-performance inference stack on vLLM and llm-d. Includes how Red Hat uses this architecture internally.

## Outline (from deck)

1. **Production gaps** — environments/hardware scarcity, workflow reproducibility, enterprise compliance
2. **Red Hat AI stack map** — OpenShift foundation + AI gateway / MCP gateway / Model-as-a-Service, inference optimization (vLLM, llm-d, validated models, compression), observability (tokens + infra), AgentOps (tracing, sandboxing, agent identity), evaluations
3. **Enterprise AI paradox** — velocity trap (frontier models for experiments) · cost cliff (unpredictable inference bills) · control gap (fragmented providers, no central observability)
4. **Inference levers** — compress models; distributed inference; hybrid runtime; validated/optimized models (Red Hat AI Hugging Face repository; GuideLLM + LM Eval; LLM Compressor)
5. **vLLM** — high-throughput OSS inference (continuous batching, speculative decoding, PagedAttention; HF / OpenAI-style APIs)
6. **llm-d** — Kubernetes-native distributed inference (Red Hat, Google, NVIDIA, Hugging Face, …): prefix/KV-aware routing, prefill/decode disaggregation, KV cache tiers, MoE expert parallelism
7. **Models as a Service** — one gateway so the org becomes a model provider (quotas, APIs, GPU sharing)
8. **Case study: EnMaaS** (Red Hat internal Engineering Model as a Service) — single endpoint for 10k+ engineers; Praxis/MaaS lineage; auth → quota → schema translation → intelligent routing → metering; mix of self-hosted open-weight (e.g. CurveBender / GLM / DeepSeek) and commercial via Vertex/OpenAI
9. **Pilot results claimed on stage** — massive monthly token volume; ~70% traffic on open-weight when access is seamless; ~40–70% effective cost reduction; developer momentum retained (treat as speaker-reported, not independent audit)

## Takeaways to borrow

- Put a **gateway** between apps/agents and models: auth, quotas, routing, spend visibility
- Split premium closed vs self-hosted open by **workload**, not politics — make the open path the easy default
- Optimize with **vLLM + llm-d** patterns (KV routing, prefill/decode split) before buying more GPUs
- Measure token spend and TTFT/TPOT before tuning hardware

## Repos & docs

- llm-d: https://github.com/llm-d/llm-d
- vLLM: https://github.com/vllm-project/vllm
- Red Hat AI Inference Server docs: https://docs.redhat.com/en/documentation/red_hat_ai_inference_server
- OpenShift AI docs: https://docs.redhat.com/en/documentation/red_hat_openshift_ai

## Contribution opportunities

- llm-d issues/PRs for distributed inference
- Upstream vLLM performance and OpenShift deployment docs/examples

## Try this in your environment

Ask: “Where are our AI coding / inference costs opaque today, and what would a gateway + self-hosted open-model path look like for the top 20% of traffic?”
