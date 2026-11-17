# Your Nodes Will Fail: How OpenShift Recovers VMs and Stateful Workloads

- **Time:** 12:50 (20 min)
- **Speakers:** Or Raz (Senior Software Engineer, Red Hat)
- **Materials:** slides-in-pack

## Abstract

Stateful VMs on RWO storage need fencing — Kubernetes alone cannot tell dead from disconnected and risks dual-write corruption. Red Hat Workload Availability (RHWA) / Medik8s operators detect unhealthy nodes and remediate (SNR, FAR, MDR, SBR) so workloads reschedule safely, aiming for seconds not minutes.

## Outline (from deck)

1. **At-most-one problem** — silent node; reschedule too early → RWO dual-write; wait → long downtime
2. **Why K8s alone fails** — NotReady/unreachable tolerations (~5m+); MachineHealthCheck limited; manual out-of-service taints
3. **Fencing** — unknown → fence (confirm off) → recover; Pacemaker/STONITH pattern via Medik8s
4. **RHWA** — optional day-2 operators from Software Catalog; FIPS; pairs with OpenShift Virtualization; planned maintenance (cordon/drain/live-migrate)
5. **Flow** — NodeHealthCheck detects → creates remediation CR → remediator (SNR/FAR/MDR/SBR) → VM reschedule
6. **Timing** — tune NHC timeouts; bottleneck node-monitor-grace-period; aggressive configs can approach ~90s (speaker numbers — treat as illustrative)
7. **Strategy picker** — SNR (no BMC); FAR (BMC IPMI/Redfish, fast); MDR (Machine API / cloud); SBR (storage heartbeats / RWX, fastest for Virt)
8. **Exploring** — sub-minute recovery; broader detection; fewer operators; multi-arch; AI-assisted kubectl medik8s plugin

## Takeaways to borrow

- Stateful Virt on RWO needs an explicit fencing strategy — not default K8s eviction timers
- Pick remediator per environment (BMC vs storage vs cloud Machine API)
- Install RHWA from catalog; find NHC/SNR/FAR/SBR/MDR/NMO there
- Upstream: https://medik8s.io/

## Repos & docs

- Medik8s: https://medik8s.io/
- OpenShift Virtualization docs
- OpenShift Software Catalog (RHWA operators)

## Contribution opportunities

- Upstream Medik8s issues for remediator UX / timing docs

## Try this in your environment

Ask: “For our Virt RWO workloads, which RHWA remediator fits (FAR vs SBR vs SNR), and what NHC timeout matches our SLO without false fencing?”
