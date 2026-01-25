# DevSecOps CI Demo

Minimal Python project with CI pipeline using GitHub Actions. This project demonstrates a minimal but production-oriented CI pipeline with linting, testing and security scanning

## Pipeline

## CI Pipeline для проекта DevSecOps Demo 🚀

```mermaid
flowchart TD
    A[Checkout code] --> B[Setup Python 3.11 + pip cache]
    B --> C[Install project & dev dependencies]
    C --> D[Ruff lint check]
    D --> E[Bandit security scan]
    E --> F[Pip-audit dependency audit]
    F --> G[Run tests with pytest]
    G --> H[Trivy FS scan - optional secrets scan]
    H --> I[CI complete ✅]
```

Triggered on push and pull requests.

![CI](https://github.com/WisePepper-tech/CI-Demo/actions/workflows/ci.yml/badge.svg)
