from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


class PermissionDenied(RuntimeError):
    """Raised when a requested local action is outside the approved sandbox."""


@dataclass(slots=True)
class ProjectPermissions:
    """Filesystem permissions for one XiaoYan project.

    The permission layer is intentionally independent from the LLM.
    A model can request an action, but this object decides whether the
    action is allowed.
    """

    read_roots: list[Path] = field(default_factory=list)
    write_roots: list[Path] = field(default_factory=list)

    @classmethod
    def from_strings(
        cls,
        *,
        read_roots: Iterable[str] = (),
        write_roots: Iterable[str] = (),
    ) -> "ProjectPermissions":
        return cls(
            read_roots=[Path(p).expanduser().resolve() for p in read_roots],
            write_roots=[Path(p).expanduser().resolve() for p in write_roots],
        )

    @staticmethod
    def _is_within(path: Path, root: Path) -> bool:
        try:
            path.relative_to(root)
            return True
        except ValueError:
            return False

    def _check(self, path: str | Path, roots: list[Path], action: str) -> Path:
        resolved = Path(path).expanduser().resolve()

        if not any(self._is_within(resolved, root) for root in roots):
            raise PermissionDenied(
                f"{action} denied for {resolved}: path is outside approved roots"
            )

        return resolved

    def require_read(self, path: str | Path) -> Path:
        return self._check(path, self.read_roots + self.write_roots, "read")

    def require_write(self, path: str | Path) -> Path:
        return self._check(path, self.write_roots, "write")
