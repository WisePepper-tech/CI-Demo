# DevSecOps CI Demo

Minimal Python project with CI pipeline using GitHub Actions. This project demonstrates a minimal but production-oriented CI pipeline with linting, testing and security scanning

## Pipeline

The CI pipeline runs:
- Ruff (lint)
- Pytest (tests)
- Security scanning (bandit and pip-audit)

Triggered on push and pull requests.

![CI](https://github.com/WisePepper-tech/CI-Demo/actions/workflows/ci.yml/badge.svg)
