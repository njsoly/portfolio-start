---
trigger: manual
description: 
globs: 
---

# Project structure

## Maintainability
- Any necessary imports should be in a requirements.txt file, or some equivalent to the project type.
- A build.sh BASH file should be maintained that:
  - activates virtual environment
  - installs any missing packages
  - calls any necessary build commands, should they exist
- A launch.sh BASH file should be maintained that:
  - calls build.sh
  - starts the application