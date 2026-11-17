# Giving AI Agents Tools to Manage Virtual Machines

- **Time:** 12:30 (20 min)
- **Speakers:** Ben Oukhanov (Software Engineer, OpenShift Virtualization, Red Hat)
- **Materials:** slides-in-pack

## Abstract

OpenShift MCP Server (tech preview): give AI agents (Claude Code, Codex, …) tools to manage OpenShift Virtualization VMs — lifecycle, troubleshooting (status/events/console screenshots), templates — bridging the gap when `oc get vm` says Running but the guest has kernel-panicked.

## Outline (from deck)

1. **Monitoring gap** — VM/pod Running ≠ guest healthy; console shows boot failure while virt-launcher is green
2. **Architecture** — AI agent → OpenShift MCP Server → VMs on OpenShift Virtualization
3. **MCP features (TP)** — create/inspect/start/stop/restart; status/events; console screenshots; inspect Virt install; create from templates
4. **Demo** — troubleshoot unresponsive but “Running” VM via MCP tools from Claude Code
5. **Enterprise deployment** — (stage visual) how to roll out MCP safely in enterprise

## Takeaways to borrow

- Add guest-console / event signals to agent tooling — don’t trust VM Ready alone
- Prefer MCP tools with RBAC over pasting kubeconfigs into chat
- Pair with harness/security practices from the AI-track harness-eval talk when enabling agent→cluster tools

## Repos & docs

- OpenShift Virtualization docs: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/virtualization
- Search upstream/OpenShift for “OpenShift MCP Server” as public repos evolve
- Related AI-track: [agent-harness-safe](../../innovate-together-il-ai/references/talks/agent-harness-safe.md)

## Contribution opportunities

- Feedback on MCP VM tool surface / false positives in troubleshooting flows

## Try this in your environment

Ask: “If we exposed an OpenShift MCP Server for Virt, which VM lifecycle vs console-troubleshoot tools should be allowed under our RBAC — and how do we gate them with harness-eval?”
