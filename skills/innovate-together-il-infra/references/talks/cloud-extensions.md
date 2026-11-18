# From Legacy Infrastructure to AI with Red Hat Cloud Extensions

- **Time:** 11:55 (20 min)
- **Speakers:** Avishay Traeger (Senior Principal Software Engineer, Red Hat); Alona Paz (Manager, Software Engineering, Red Hat)
- **Materials:** slides-in-pack

## Abstract

Red Hat Cloud Extensions: a consistent cloud-service consumption layer on Red Hat infrastructure — turn platform capabilities into tenant-ready services for internal enterprise teams and for external cloud providers (stronger isolation + billing).

## Outline (from deck)

1. **When platform must operate as a cloud** — enterprises serving internal teams vs providers serving paying customers
2. **Gap Cloud Extensions fills** — shared consumption layer across the OpenShift portfolio
3. **Building blocks** — Identity & access; tenant boundaries (incl. ACM, compute, net, storage); policies & quotas; catalogs; provisioning & lifecycle; metering/billing integration
4. **Architecture** — entry → Fulfillment Service (authz/policy) → Management Cluster (Cloud Extensions + AAP) driving OpenShift Virtualization / ACM / OpenShift AI; AAP for third-party net/storage/DNS/hardware inventory
5. **Model** — platform team defines; tenant teams consume via self-service catalog
6. **Demo** — provider setup → tenant self-service
7. **Upstream pointer** — https://github.com/osac-project/osac

## Takeaways to borrow

- Separate “platform capability” from “tenant-ready cloud service” (catalog, quotas, lifecycle, metering)
- Use AAP as the integration glue to non-OpenShift estate pieces
- Design tenant boundaries before exposing Virt/AI as self-service

## Repos & docs

- OSAC / Cloud Extensions: https://github.com/osac-project/osac
- OpenShift / ACM / Virt docs as platform context

## Contribution opportunities

- Upstream OSAC issues/PRs for catalog/fulfillment UX

## Try this in your environment

Ask: “Which of our OpenShift capabilities are still ticket-only, and what Cloud Extensions–style catalog + quota boundary would make them tenant self-service?”
