# Leveraging Sandboxing and Confidential Computing for Agents and Models

- **Time:** 12:50 (20 min)
- **Speakers:** Ariel Adam (Director, Engineering, Red Hat)
- **Slides:** Coming soon

## Abstract

Virtualization is becoming critical for AI factories. On the **agent** side: agent-sandbox (Kata-based) sandboxes Openshell agents to prevent kernel escapes; confidential computing protects agents from malicious admins. On the **model** side: confidential containers with KServe provide confidential inference — private model-as-a-service protecting model, weights, and data from malicious admins.

Related abstract phrasing: “The role of virtualization technologies in AI factories” / securing agentic workloads with openshell and agent-sandbox (fast sandboxes, policy).

## Takeaways to borrow

- Separate agent execution sandbox from model confidentiality
- Prefer Kata / confidential containers over trusting the host admin boundary alone
- Design agents so untrusted generated code runs in short-lived sandboxes

## Repos & docs

- Kata Containers: https://katacontainers.io/
- Confidential Containers: https://confidentialcontainers.org/
- KServe: https://kserve.github.io/website/
- Search upstream for `agent-sandbox` / openshell as speaker materials confirm exact repos

## Contribution opportunities

- Kata / CoCo / KServe issues for AI inference and agent sandbox UX
- Document threat models (malicious admin vs malicious agent code) in your org’s ADRs

## Try this in your environment

Ask: “Where do we execute untrusted agent-generated code today, and what would a Kata-based sandbox gate look like before shell/tools run?”
