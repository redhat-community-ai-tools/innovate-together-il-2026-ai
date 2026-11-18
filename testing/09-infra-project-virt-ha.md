# 09 — Infra project match: Virt HA on RWO

Tags: `happy` · Skill: `innovate-together-il-infra`

## Question

> Using the Innovate Together IL Infra skill: we run OpenShift Virtualization with mostly RWO disks. Nodes fail occasionally and VMs sit Terminating. Which talks and operators should we adopt?

## Skill response

## Relevant talks

### Your Nodes Will Fail — fencing before reschedule

- **Borrow:** Stateful Virt on RWO needs an explicit fence (RHWA / Medik8s: SNR, FAR, MDR, SBR). Kubernetes NotReady timers alone can dual-write or wait minutes.
- **Try:** Pick a remediator that matches the nodes (no BMC → SNR; BMC → FAR).
- **Repos / docs:** OpenShift Virtualization docs; https://medik8s.io/
- **Materials:** slides-in-pack (outline in the talk file; no downloadable deck in this repo)

### VM Mobility — after the node is confirmed down

- **Borrow:** Storage live migration and cross-cluster live migration for the disks that can move.
- **Materials:** slides-in-pack

## Suggested next step

Inventory RWO VM disks and whether those nodes have a BMC, then enable one RHWA remediator in a non-prod cluster.

## Evaluation

| Criterion | Result | Notes |
|-----------|--------|-------|
| Correct skill / mode | Pass | Infra project match |
| Talk selection | Pass | nodes-will-fail + vm-mobility |
| Grounded | Pass | No invented BMC product |
| No private deck link | Pass | |
| Shape | Pass | |

**Verdict: good (pass)**
