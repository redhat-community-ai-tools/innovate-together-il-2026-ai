# Building a Scalable, Cost-Efficient AI Strategy with Red Hat AI

- **Time:** 11:05 (30 min)
- **Speakers:** Roy Nissim (Senior Manager, Engineering, Red Hat)
- **Materials:** slides-pending

## Abstract

As enterprise AI moves from experiment to production, teams hit surging inference bills, fragmented tooling, and observability gaps. This session covers Red Hat’s Hybrid Inference Strategy: a unified AI gateway (observability, token management, intelligent routing across self-hosted and external models), a curated validated model catalog, and a high-performance inference stack on vLLM and llm-d. Includes how Red Hat uses this architecture internally.

Related abstract (coding-cost angle): Hybrid AI Gateway / MaaS governance + llm-d for self-hosting to mix premium and open models without freezing developer speed.

## Takeaways to borrow

- Put a gateway between apps and models: routing, quotas, observability
- Split “premium closed” vs “self-hosted open” by workload, not by politics
- Measure token spend and TTFT/ITL before optimizing GPUs

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
