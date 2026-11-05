# 01 — Project match: GPU / inference cost

Tags: `happy`

## Question

> Using the Innovate Together IL AI skill, look at our situation and suggest which conference talks and open-source projects we should borrow from. We run OpenShift on-prem and care about GPU cost for model serving and coding assistants.

## Skill response

## Relevant talks

### Building a Scalable, Cost-Efficient AI Strategy with Red Hat AI — why it fits
- **Borrow:** Gateway between apps and models (routing, quotas, observability); split premium closed vs self-hosted open by workload; measure token spend and latency before buying GPUs.
- **Try:** Map top traffic to “must be frontier” vs “can be self-hosted open”; sketch a gateway path with token visibility.
- **Repos / docs:** [llm-d](https://github.com/llm-d/llm-d), [vLLM](https://github.com/vllm-project/vllm), [OpenShift AI docs](https://docs.redhat.com/en/documentation/red_hat_openshift_ai), [AI Inference Server docs](https://docs.redhat.com/en/documentation/red_hat_ai_inference_server)
- **Contribute:** llm-d / vLLM issues for OpenShift-shaped deploy docs and perf fixes.

### From Adoption to Optimization: OpenShift AI in Production — why it fits
- **Borrow:** Instrument GPU utilization (idle vs memory-bound vs queue-bound) before scaling hardware; air-gapped constraints change packaging and observability.
- **Try:** Capture GPU utilization for one model endpoint this week.
- **Repos / docs:** OpenShift AI docs; pair with the cost-strategy talk.
- **Contribute:** Sanitized GPU debugging runbooks where public.

*(Skipped “AI Ready Enterprise” framing talk — two deep talks already cover the ask.)*

## Suggested next step

Export one week of inference/coding-assistant spend (or GPU hours) by workload, then draft a gateway + self-hosted open-model candidate for the cheapest 20% of traffic using llm-d/vLLM on OpenShift.

## Evaluation

| Criterion | Result | Notes |
|-----------|--------|-------|
| Correct mode | Pass | Project match |
| Talk selection | Pass | 2 deep talks; no framing filler |
| Grounded | Pass | |
| Sales / PII | Pass | |
| Shape | Pass | |

**Verdict: good (pass)**

## Live agent delta

- Date / agent: 2026-11-05 / Cursor (Composer), skill via SKILL.md + references/
- Drift vs hand-authored: Negligible — same 2 talks (cost + production GPU); skipped framing talk; same repos/next step shape.
- Re-eval verdict: **pass**
- Full live text: [live-runs/2026-11-05-cursor.md](live-runs/2026-11-05-cursor.md#q01--project-match-gpu-cost)
