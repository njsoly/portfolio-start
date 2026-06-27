
# gh-config-calls

These are some commands for `gh` command-line that I'd like to save for later, to configure my projects, because for now, I don't feel like making a template repository.

```bash
# Hopefully sets up the repository to only allow squash merges.
# Could try to disable the merge commit, then enable squash, and re-enable merge commit?
# Not sure how else to mark squash as the default.
repo=${1:-$PWD}
gh repo edit njsoly/${repo} --enable-squash-merge  --enable-merge-commit=false --enable-rebase-merge=false
```

## Sources:
- https://github.com/copilot/share/804d1302-43e0-88d6-9012-984140432813
  - This is a dead link to a chat I had with GH Copilot... it turned out the code it gave me was rancid anyway.
  - This code is from me, after fixing the erroneous options from AI.
