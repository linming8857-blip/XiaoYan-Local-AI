from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


SCHEMA = """
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id TEXT,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id TEXT,
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    source TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    UNIQUE(project_id, key)
);
"""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(slots=True)
class MemoryStore:
    path: Path

    def connect(self) -> sqlite3.Connection:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        db = sqlite3.connect(self.path)
        db.row_factory = sqlite3.Row
        db.executescript(SCHEMA)
        return db

    def add_message(
        self,
        *,
        role: str,
        content: str,
        project_id: str | None = None,
    ) -> None:
        with self.connect() as db:
            db.execute(
                """
                INSERT INTO conversations(project_id, role, content, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (project_id, role, content, _utc_now()),
            )

    def set_memory(
        self,
        *,
        key: str,
        value: str,
        project_id: str | None = None,
        source: str | None = None,
    ) -> None:
        now = _utc_now()
        with self.connect() as db:
            db.execute(
                """
                INSERT INTO memories(
                    project_id, key, value, source, created_at, updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(project_id, key) DO UPDATE SET
                    value = excluded.value,
                    source = excluded.source,
                    updated_at = excluded.updated_at
                """,
                (project_id, key, value, source, now, now),
            )

    def list_memories(self, project_id: str | None = None) -> list[dict]:
        with self.connect() as db:
            rows = db.execute(
                """
                SELECT id, project_id, key, value, source, created_at, updated_at
                FROM memories
                WHERE project_id IS ?
                ORDER BY updated_at DESC
                """,
                (project_id,),
            ).fetchall()
        return [dict(row) for row in rows]
