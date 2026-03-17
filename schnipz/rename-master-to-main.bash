#!/usr/bin/env bash

# TODO: take in a -h|--help
# TODO: accept parameters
# TODO: also check what the primary branch is first

git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a
