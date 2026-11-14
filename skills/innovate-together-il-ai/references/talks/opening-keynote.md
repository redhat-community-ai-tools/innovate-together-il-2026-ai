# Opening Keynote

- **Time:** 09:10 (55 min)
- **Speakers:** Michael Kotelnikov (Red Hat); Shlomi Ambar (Head of Technology Strategy & Solution Engineering, Maccabi Healthcare Services); Official Representative, Israel Ministry of Defense
- **Materials:** slides-in-pack

## Abstract

New generations of workloads keep pushing IT platforms. The modern platform must adapt to the AI landscape, scale, and new initiatives while keeping critical production applications and traditional workloads up. Red Hat Israel leadership and key customers show how to build a resilient, secure foundation that accelerates innovation without compromising production stability.

## Outline (from deck)

1. **Unified platform** — containers, virtualization, AI models, and AI agents on one OpenShift footing
2. **Platform jobs that never go away** — deliver apps, keep current, keep running, keep observable (automation / GitOps / procedures)
3. **What if the platform could reason and act?** — OpenShift framed as an *agentic* platform: intelligent but still predictable under load
4. **OpenShift Lightspeed: chatbot → agent** — from RAG-over-docs answers to intent + MCP tools that *act* on the cluster (with the user’s permissions)
5. **Examples shown** — ask for a VM and get one; alert → analyze → remediate in a sandbox → verify; ask “why are CoreDNS errors high?” and get an operational path
6. **AI moves fast; ops run for years** — under operational load the platform must stay predictable
7. **Lifecycle** — OpenShift 4 vs 5 support windows; upgrade framed as the “most boring thing you’ve done”; Lightspeed-assisted upgrade readiness (“is this upgrade safe for my environment?”)

## Takeaways to borrow

- Frame AI as another generation of platform workload, not a side project
- Prefer agents that **act through the control plane** (with RBAC) over chatbots that only quote docs
- Put remediations through a sandbox / verify loop before production
- Plan upgrades with compatibility/readiness reports, not hope

## Repos & docs

- OpenShift docs: https://docs.openshift.com/
- OpenShift AI overview: https://www.redhat.com/en/technologies/cloud-computing/openshift/ai

## Contribution opportunities

N/A (keynote). Follow product talks later in the track for OSS entry points.

## Try this in your environment

Ask: “Given our uptime / compliance constraints, which later AI-track talks map to gaps in our platform readiness — and where would a Lightspeed-style agent need MCP tools vs read-only RAG?”
