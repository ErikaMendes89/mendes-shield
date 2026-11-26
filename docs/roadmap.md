# Public Roadmap

[Home](../README.md) · [Architecture](architecture/README.md) · [Getting started](getting-started/README.md) · [ADRs](adr/README.md)

This roadmap describes intended work. A status changes to implemented only when the corresponding code and verification evidence are present. No dates are promised.

| Area | Objective | Status |
| --- | --- | --- |
| Foundation | Minimal API, health checks, tests, quality tooling, CI, and container build | Implemented |
| Ingestion | Accept bounded, validated, privacy-aware HTTP metadata | Planned |
| Features | Aggregate sanitized events over bounded time windows | Planned |
| Detection | Compare an explainable statistical baseline with candidate anomaly models | Planned |
| Alerts and policies | Produce evidence-backed alerts and human-reviewed recommendations | Planned |
| Integration | Explore WAF adapters with auditability and rollback | Planned |
| Evaluation | Publish data provenance, false-positive measurements, latency, and resource use | Planned |

Planned items are not available in the current API. Each phase needs an implementation, relevant tests, privacy and threat-model review, and measurable acceptance criteria before it can be considered complete. Architecture choices must be recorded in [ADRs](adr/README.md) before integration work starts.

Discuss proposals through [GitHub Issues](https://github.com/ErikaMendes89/mendes-shield/issues). Do not include secrets, private telemetry, or unauthorized attack traffic.
