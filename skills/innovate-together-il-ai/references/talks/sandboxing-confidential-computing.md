# Leveraging Sandboxing and Confidential Computing for Agents and Models

- **Time:** 12:50 (20 min)
- **Speakers:** Ariel Adam (Director, Engineering, Red Hat)
- **Materials:** slides-in-pack

## Abstract

Virtualization is becoming critical for AI factories. On the **agent** side: agent-sandbox (Kata-based) sandboxes Openshell agents to prevent kernel escapes; confidential computing protects agents from malicious admins. On the **model** side: confidential containers with KServe provide confidential inference — private model-as-a-service protecting model, weights, and data from malicious admins.

## Outline (from deck)

1. **Crash course** — workload isolation vs confidentiality on OpenShift (sandboxed containers vs confidential containers)
2. **Two threat directions**
   - Protect the **host / cluster** from untrusted agent/tool code (sandbox / OpenShell)
   - Protect **customer data, prompts, weights, credentials** from untrusted infra / admins (confidential containers + attestation)
3. **Agent path** — OpenShell sandbox: network isolation, policy evaluation, credential resolution, DNS/proxy; supervisor governs the agent; ties to RH AI Factory patterns
4. **Model path** — confidential inference with OpenShift AI Serving (KServe) / llm-d / vLLM / NIM-style stacks inside Kata confidential containers; encrypted models/weights; Trustee attestation, KMS, RVPS
5. **Compose them** — sandbox the agent *and* confidentially serve the model when both threat models apply

## Takeaways to borrow

- Separate **agent execution sandbox** from **model confidentiality** — different threats, both needed in AI factories
- Prefer Kata / confidential containers over trusting the host admin boundary alone
- Design agents so untrusted generated code runs in short-lived sandboxes with policy + credential proxying
- Ask for attestation / key-release story when models or prompts must stay confidential on shared infra

## Repos & docs

- Kata Containers: https://katacontainers.io/
- Confidential Containers: https://confidentialcontainers.org/
- KServe: https://kserve.github.io/website/
- OpenShift sandboxed / confidential containers docs (product docs): https://docs.redhat.com/en/documentation/openshift_sandboxed_containers
- Search upstream for `agent-sandbox` / OpenShell as public repos evolve

## Contribution opportunities

- Kata / CoCo / KServe issues for AI inference and agent sandbox UX
- Document threat models (malicious admin vs malicious agent code) in your org’s ADRs

## Try this in your environment

Ask: “Where do we execute untrusted agent-generated code today, and what would a Kata-based sandbox gate look like before shell/tools run — and which workloads also need confidential inference?”
