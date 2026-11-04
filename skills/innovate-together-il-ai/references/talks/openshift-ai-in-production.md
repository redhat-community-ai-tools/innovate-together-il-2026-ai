# From Adoption to Optimization: OpenShift AI in Production

- **Time:** 13:25 (20 min)
- **Speakers:** Dor Sivan (Senior Consultant, Red Hat)
- **Slides:** Coming soon

## Abstract

In many air-gapped environments AI is still early. Deploying and managing models is complex; GPU use is the scarce resource. Session covers OpenShift AI advantages for adoption, practical production cases and challenges seen at customers, then how to run models in production with proper GPU utilization and investigation methods when issues arise — including approaches used to analyze GPU usage for optimization.

## Takeaways to borrow

- Adoption path ≠ production optimization path; plan both
- Instrument GPU utilization before buying more GPUs
- Air-gapped constraints change packaging, model delivery, and observability

## Repos & docs

- OpenShift AI docs: https://docs.redhat.com/en/documentation/red_hat_openshift_ai
- Related inference cost talk: [scalable-cost-efficient-ai-strategy](scalable-cost-efficient-ai-strategy.md)
- Model gating talk: [packaging-gating-models](packaging-gating-models.md)

## Contribution opportunities

- Share sanitized runbooks for GPU utilization debugging on OpenShift AI
- Upstream examples for air-gapped model deploy patterns where public

## Try this in your environment

Ask: “What metrics show our GPU idle vs memory-bound vs queue-bound today, and which OpenShift AI knobs should we change first?”
