---
trigger: manual
description: 
globs: 
---

# Project structure

## Python
### Maintainability
- Any necessary imports should be in a requirements.txt file, or some equivalent to the project type.
- Bash scripts to build and run apps should 
  - introduce themselves and declare which project they operate on
  - print information on major or time-consuming steps to console before they happen
  - quit on error, with a good error message, if the failing command isn't expected to give one
- A build.sh BASH file should be maintained that:
  - checks that the python module `venv` is available for use
  - activates virtual environment
  - installs any missing packages
  - calls any necessary build commands, should they exist
- A launch.sh BASH file should be maintained that:
  - calls build.sh
  - starts the application
