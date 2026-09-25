# XiaoYan Local AI — Architecture v0.1

## Goal

A Windows-first local assistant that remains useful with the network disconnected.

## Main components

### 1. Desktop UI

Responsibilities:

- Chat
- Project selection
- Reader
- Memory review
- Permission prompts
- Tool activity log
- Settings

The first implementation should keep the UI independent from the model runtime.

### 2. Core Agent

The Core Agent coordinates:

- model messages
- tool calls
- project context
- memory retrieval
- approval gates

The model must never receive unrestricted operating-system access by default.

### 3. Model adapters

Initial target:

- Ollama local API
- gpt-oss-20b as a preferred model when hardware permits

Future adapters can be added without changing the rest of the application.

### 4. Memory

Three separate scopes:

- Conversation history
- Long-term user-approved memory
- Project-specific memory

Storage should remain local. SQLite is the initial metadata store.

### 5. Knowledge / RAG

Documents are imported into a local library, parsed, chunked and indexed.

Planned sources:

- EPUB
- PDF
- TXT
- DOCX
- source code
- project documentation

Knowledge indexing is separate from model training.

### 6. Reader

Reader state includes:

- book/document ID
- current chapter/page
- bookmarks
- highlights
- notes
- spoiler boundary / reading progress

### 7. Tools

Tools are registered with explicit capability metadata.

Examples:

- read file
- write file
- search files
- run Python
- run PowerShell
- browser navigation

### 8. Computer control

Windows control is a separate privilege layer.

Preferred order:

1. Windows UI Automation / accessibility APIs
2. application-specific APIs
3. keyboard / mouse simulation only when necessary

High-risk actions require explicit confirmation.

## Data flow

```text
User
  ↓
Desktop UI
  ↓
Core Agent
  ├── Memory retrieval
  ├── Knowledge retrieval
  ├── Local model
  └── Tool dispatcher
         ↓
   Permission manager
         ↓
   Allowed local action
```

## Offline boundary

Offline-capable:

- local chat
- local memory
- local document reading
- local RAG
- local file tools
- local computer tools

Requires network:

- web search
- GitHub
- online plugins / cloud APIs
- downloading new models
