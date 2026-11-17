# OpenShift Virtualization Roadmap

- **Time:** 11:05 (30 min)
- **Speakers:** Dan Kenigsberg (Director, Engineering, Red Hat); Ronen Sde-Or (Principal Product Manager - Technical, Red Hat)
- **Materials:** slides-in-pack

## Abstract

2026 roadmap for Red Hat OpenShift Virtualization: simplified air-gapped install, Virtualization Autopilot, VM management UX, resource efficiency, networking/storage protection, Cluster-as-a-Service, and migration tooling (Migration Advisor + MTV).

## Outline (from deck)

1. **Agent Installer** — tested ISO from console.redhat.com; UI-driven; pre-configured Virt operators; air-gapped / registry-less day-1; day-2 upgrade/add node with external/local registry
2. **Virtualization Autopilot** — opinionated plugins (load-aware balancing, observability, SWAP); GA plugins opt-out; DP/TP opt-in
3. **AI / MCP in action** — demos called out on stage (see sibling MCP/VM talks)
4. **VM management** — KubeVirt CNCF graduation; single pane of glass; advanced search; node-level views; templates (convert VM→template GA; OVA/VMware import roadmap)
5. **Resource efficiency** — higher memory overcommit defaults; automatic SWAP; KSM zero-pages; descheduler guardrails; Autopilot load-balancing
6. **Networking roadmap** — BGP cloud connector; OVS-DPDK; EVPN/Open PE; QoS for L2 VMs; MAC spoofing GA
7. **Storage & data protection** — QEMU CBT incremental backups; clustered workload live migration; single-file restore TP
8. **Cluster-as-a-Service** — standalone OpenShift on Virt (non-HCP); TP→GA timeline
9. **Migration** — OpenShift Migration Advisor (RVTools/OVA readiness); MTV: Hyper-V GA, Nutanix/Azure TP, deep inspection, dedicated migration hosts

## Takeaways to borrow

- Treat Virt day-1 air-gap install and Autopilot defaults as first-class platform product, not DIY glue
- Plan migration with Migration Advisor before MTV cutover
- Track resource-efficiency defaults (overcommit/SWAP/KSM) before buying nodes

## Repos & docs

- OpenShift Virtualization docs: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/virtualization
- KubeVirt: https://kubevirt.io/
- MTV docs: https://docs.redhat.com/en/documentation/migration_toolkit_for_virtualization

## Contribution opportunities

- Upstream KubeVirt / MTV issues for migration providers and install UX

## Try this in your environment

Ask: “Which Virt roadmap items (Agent Installer, Autopilot, MTV providers) unblock our VMware exit timeline this quarter?”
