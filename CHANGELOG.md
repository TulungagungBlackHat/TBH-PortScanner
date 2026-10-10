# Changelog

## Unreleased

- Ecosystem standardization: SECURITY.md, CONTRIBUTING.md, requirements, CI smoke checks.

## 1.0.0 (2026-09-18)

- Initial stable single-tool release (educational, authorized-use only).

## [3.0.0] - 2026-10-10
### Added
- Real top-100 port list (was 9), service names via getservbyport
- Banner grabbing on open ports
- CVE/exposure hints for 20+ services (Redis, Docker API, MongoDB...)
- Unified TBH v3 CLI: --version, --json, --no-color
- Exit codes for pipelines (0 ok, 1 finding, 2 error)
- Consistent JSON report schema
- Proper exception handling, honest versioning

## [3.1.0] - 2026-10-11
### Added
- Multi-target scanning: --targets file (one host per line)
- Aggregated JSON for batch runs; per-host elapsed
- Unresolvable hosts skipped instead of aborting the batch
