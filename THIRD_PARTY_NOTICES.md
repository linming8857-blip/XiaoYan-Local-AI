# Third-party references

XiaoYan Local AI is designed as its own codebase. At this stage, this repository does **not** vendor full copies of the projects below.

## OpenAI gpt-oss

- Upstream: `openai/gpt-oss`
- License observed upstream: Apache License 2.0
- Intended use: local model / Harmony / tool-calling compatibility research.

## Ollama

- Upstream: `ollama/ollama`
- License observed upstream: MIT
- Intended use: local model runtime and local HTTP API integration.

## browser-use

- Upstream: `browser-use/browser-use`
- License observed upstream: MIT
- Intended use: browser-agent architecture and browser automation research.

## Open WebUI

Open WebUI is **not bundled** into XiaoYan Local AI at this stage.

Its current licensing and branding terms should be reviewed separately before any future direct code reuse or redistribution.

## Policy

When third-party code is actually copied, modified, vendored or redistributed later:

1. Preserve the applicable upstream copyright and license notices.
2. Record the exact upstream repository, commit and source path.
3. Keep copied code clearly separated from XiaoYan-owned implementation where practical.
4. Re-check the upstream license at the time of integration.
