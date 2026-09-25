# XiaoYan Local AI

**XiaoYan Local AI（小言 Local）** is a Windows-first local AI assistant project.

The goal is to build a private, offline-capable assistant that can combine:

- Local LLM inference
- Long-term memory
- Local knowledge / RAG
- EPUB / PDF / TXT / DOCX reading
- File access with explicit folder permissions
- Coding-agent workflows
- Browser automation
- Windows computer control
- Optional local speech and vision modules

## Design principles

1. **Local-first** — core chat, memory and document workflows should work without Internet access.
2. **Permission-based** — file and computer access must be explicitly scoped.
3. **Project isolation** — each project can have its own allowed folders, memory and knowledge base.
4. **Human confirmation for risky actions** — destructive or privileged actions require approval.
5. **Modular backends** — model runtime, memory, reader, tools and UI remain replaceable.
6. **No forced cloud account** — local operation must not require an OpenAI / ChatGPT account.

## Planned architecture

```text
XiaoYan Local
├─ Desktop UI
├─ Core Agent
│  ├─ Local model adapter
│  ├─ Tool dispatcher
│  └─ Permission manager
├─ Memory
│  ├─ Conversations
│  ├─ Long-term memory
│  └─ Project memory
├─ Knowledge / RAG
├─ Reader
│  ├─ EPUB
│  ├─ PDF
│  ├─ TXT
│  └─ DOCX
├─ Tools
│  ├─ Files
│  ├─ Python
│  ├─ PowerShell
│  └─ Browser
└─ Computer Control
   ├─ Windows UI Automation
   ├─ Screenshots
   └─ Approval gates
```

## Initial technology references

The project is currently evaluating / integrating ideas from:

- OpenAI `gpt-oss`
- Ollama
- browser-use

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Open WebUI is **not** bundled into this repository at this stage.

## Status

Early architecture / bootstrap stage.

## Repository layout

```text
docs/          Design documents
src/           XiaoYan Local source code
references/    Notes about upstream projects (not full vendored copies)
scripts/       Development / setup scripts
```

## Security model

XiaoYan Local is intended to support scoped permissions such as:

- Chat only
- Read-only folders
- Read / write project folders
- Computer-control mode

Deletion, registry edits, administrator commands, system-directory writes and other high-risk actions should require explicit confirmation.

---

This repository is under active development.
