# Security Design

[Home](../../README.md) · [Architecture](../architecture/README.md) · [ML design](../machine-learning/README.md) · [Disclosure policy](../../SECURITY.md)

## Current status

The foundation API has no ingestion, detection, or mitigation features. The items below are design goals for future work and are not controls provided by the current code.

## Design goals

- Use a threat model to document assets, actors, trust boundaries, and abuse cases before integrations.
- Minimize telemetry and exclude credentials, cookies, tokens, and request bodies by default.
- Validate and bound all untrusted events and processing work.
- Keep analytics isolated from the protected application's serving path.
- Default to shadow observation; require human approval and a rollback path before any policy change.
- Restrict access to training data and model artifacts, and make evaluation provenance reviewable.

Future security and privacy controls require implementation and independent verification. For vulnerability reports, follow the [responsible disclosure policy](../../SECURITY.md).
