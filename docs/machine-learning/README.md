# Machine Learning Design

[Home](../../README.md) · [Architecture](../architecture/README.md) · [Security](../security/README.md) · [Roadmap](../roadmap.md)

## Current status

No model has been trained or benchmarked for this repository. The API does not currently ingest events or perform anomaly detection.

## Evaluation principles

The research plan is to compare an explainable statistical baseline with candidate anomaly models using aggregated, sanitized HTTP metadata. Any evaluation should:

- use chronological splits to reduce temporal leakage;
- document dataset provenance, permissions, and preprocessing;
- report precision and recall where trustworthy labels exist;
- measure false positives on legitimate traffic;
- quantify detection latency, CPU, and memory costs;
- evaluate drift and describe limitations.

An anomaly score is not the probability that an event is an attack. Model output is a review signal, not an automatic enforcement decision. See the [public roadmap](../roadmap.md) and [security design](../security/README.md).
