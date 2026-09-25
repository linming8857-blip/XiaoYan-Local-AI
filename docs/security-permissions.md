# Permission model

## Permission levels

### Chat

No filesystem or computer-control access.

### Read-only project

May read only approved roots.

Example:

```text
D:\TSOnline\
D:\Game-HD-Enhancer\
```

### Read / write project

May create and modify files inside approved roots.

### Computer control

May interact with explicitly allowed applications and UI surfaces.

## Always-confirm actions

The following should require confirmation even when computer-control mode is enabled:

- file or folder deletion
- recursive bulk changes
- writes outside approved roots
- registry modification
- administrator / elevated commands
- system-directory writes
- software installation
- disk / partition operations
- credential access
- network upload of local files

## Path safety

Before a filesystem action:

1. Resolve the path to an absolute canonical path.
2. Reject path traversal.
3. Compare against approved roots.
4. Apply the requested read/write permission.
5. Log the action.

Symlinks, junctions and reparse points must not be allowed to escape an approved project root.

## Project sandbox

Each project has its own:

- approved roots
- memory namespace
- knowledge namespace
- tool policy

Closing or switching projects removes the previous project's temporary permissions.
