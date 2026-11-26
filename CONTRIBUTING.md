# Contributing

Thank you for your interest in Mendes Shield.

## Current contribution status

Code contributions are paused while the project owner reviews the license and contributor terms. The repository has no license yet. Please do not submit code for incorporation until this status changes.

Design questions, threat-model feedback, and documentation suggestions are welcome through [GitHub Issues](https://github.com/ErikaMendes89/mendes-shield/issues). For significant architecture proposals, describe the problem, alternatives, privacy and security implications, and measurable acceptance criteria. Record accepted decisions as [ADRs](docs/adr/README.md) before integration work begins.

## Development checks

The current application requires Python 3.12 or newer and `uv`.

```bash
uv sync --dev
uv run pytest
uv run ruff check .
uv run mypy src
```

The only implemented service is the foundation FastAPI API. Do not describe planned ingestion, detection, or mitigation behavior as available.

## Security and privacy

- Never commit credentials, tokens, private agent files, personal data, confidential telemetry, or private datasets.
- Do not include real attack traffic or tests against systems without explicit authorization.
- Do not disclose vulnerabilities in public issues; follow [SECURITY.md](SECURITY.md).
- Explain security, privacy, and rollback implications in any future code proposal.

## Review expectations

When code contributions reopen, use a focused pull request with relevant tests and exact verification commands. Include limitations and known risks. An agent-generated summary alone is not sufficient review evidence; see [GOVERNANCE.md](GOVERNANCE.md).
