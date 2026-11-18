# Mobility of Virtual Machines in OpenShift Clusters: Storage Live Migration and Cross-Cluster Live Migration

- **Time:** 13:25 (20 min)
- **Speakers:** Jenia Peimer (Senior Software Quality Engineer, Red Hat — OpenShift Virtualization Storage)
- **Materials:** slides-in-pack

## Abstract

Three mobility modes for OpenShift Virtualization: compute live migration, storage live migration (any-to-any backends, incl. RWO), and cross-cluster live migration orchestrated with MTV — with requirements, limitations, and demos.

## Outline (from deck)

1. **Compute live migration** — why: node maintenance, rebalancing, upgrades; needs shared (RWX) storage
2. **Storage live migration** — why: rebalance/adopt/retire storage, local storage moves; any-to-any backend (RWO/RWX, block/filesystem); two compatible nodes; enabled via HCO workloadUpdateMethods LiveMigrate; MultiNamespaceVirtualMachineStorageMigrationPlan APIs; limitations: shareable disks, virtio-fs filesystems, LUN disks
3. **Cross-cluster live migration** — why: maintenance, rebalancing, on-prem↔cloud, consolidation; variant of storage live migration; special migration network in HCO; source/target VMIM sendTo/receive; MTV orchestrates providers, network/storage maps, plans
4. **Recap table** — compute vs storage vs cross-cluster; MTV for cross-cluster
5. **Demo** — CCLM / MTV CLI path

## Takeaways to borrow

- Pick mobility mode by storage access mode (RWX vs RWO) and whether the target is same cluster or another
- Use MTV for cross-cluster orchestration; exchange CA keys between providers
- Know hard limits (shareable / virtio-fs / LUN) before promising zero-downtime storage moves

## Repos & docs

- MTV docs: https://docs.redhat.com/en/documentation/migration_toolkit_for_virtualization
- OpenShift Virtualization docs
- KubeVirt live migration concepts: https://kubevirt.io/

## Contribution opportunities

- Upstream KubeVirt / MTV issues for storage and cross-cluster migration edge cases

## Try this in your environment

Ask: “For our Virt estate, which VMs need storage live migration vs cross-cluster MTV, and which disks hit the shareable/LUN limitations?”
