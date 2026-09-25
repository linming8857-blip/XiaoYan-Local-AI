from __future__ import annotations

import argparse

from xiaoyan_local.core.ollama import OllamaClient


def main() -> None:
    parser = argparse.ArgumentParser(description="XiaoYan Local AI bootstrap CLI")
    parser.add_argument("--model", default="gpt-oss:20b")
    parser.add_argument(
        "prompt",
        nargs="*",
        help="Prompt to send to the local model",
    )
    args = parser.parse_args()

    prompt = " ".join(args.prompt).strip()
    if not prompt:
        print("XiaoYan Local AI bootstrap is installed.")
        print("Usage: xiaoyan-local --model <model> <prompt>")
        return

    client = OllamaClient()
    result = client.chat(
        model=args.model,
        messages=[{"role": "user", "content": prompt}],
    )

    message = result.get("message") or {}
    print(message.get("content", result))


if __name__ == "__main__":
    main()
