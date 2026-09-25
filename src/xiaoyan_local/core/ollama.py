from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any
from urllib import request


@dataclass(slots=True)
class OllamaClient:
    """Minimal local-only Ollama chat client.

    Uses the Python standard library so the bootstrap has no runtime
    dependencies. The default endpoint points to localhost.
    """

    base_url: str = "http://127.0.0.1:11434"

    def chat(
        self,
        *,
        model: str,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        think: bool | str | None = None,
        timeout: float = 300.0,
    ) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "model": model,
            "messages": messages,
            "stream": False,
        }

        if tools:
            payload["tools"] = tools

        if think is not None:
            payload["think"] = think

        body = json.dumps(payload).encode("utf-8")
        req = request.Request(
            f"{self.base_url.rstrip('/')}/api/chat",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
