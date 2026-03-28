---
name: bash-rules
description: Style choices and policies for bash scripts
---

# bash rules

## Error handling
Bash scripts should exit immediately on failure, and leave `$?` with the proper exit code.

```bash
set -e
```

## Help text
Bash scripts longer than 8 lines should have a `--help|-h` option that prints a helpful message.
