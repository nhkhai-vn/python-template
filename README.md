# python-template

A starting point for a Python 3.15 project: uv for environments, locking and builds, Ruff for formatting and linting, mypy in strict mode, pytest with a 100% branch coverage gate, a small non-root Docker image, and GitHub Actions with SHA-pinned actions.

## Start a project

Use this template on GitHub, then rename `app` in `pyproject.toml`, `src/app/` and the imports.

```sh
make install   # create .venv from uv.lock
make test
make run       # prints "Hello, world!"
```

## Commands

| | |
|---|---|
| `make install` | `uv sync --locked` |
| `make format` | Ruff format and safe fixes |
| `make lint` | lockfile up to date, Ruff format and lint, mypy |
| `make test` | pytest with branch coverage; fails below 100% |
| `make build` | Docker image `app` |
| `make run` | run the `app` entry point |

Add a dependency with `uv add <package>`, a development tool with `uv add --dev <package>`.

## What is set up

- **Python 3.15** from `.python-version`; `requires-python = ">=3.15"`.
- **Supply chain**: `exclude-newer = "7 days"` keeps uv from resolving any release younger than a week; Dependabot updates uv, GitHub Actions and the Docker base weekly with the same 7-day cooldown.
- **Docker**: built with uv in one stage, copied as a virtual environment into `python:3.15-slim`, runs as an unprivileged user.
- **CI** on every pull request and push to `main`: lint, type check, tests, Docker build and run; zizmor audits the workflows. Workflows have no permissions by default and actions are pinned by commit SHA.

## License

[MIT](LICENSE)
