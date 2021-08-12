# Git Hooks
This is a template repository for my Git hooks, that I use in many of my projects.

I use the following hooks:
- `pre-commit`
- `commit-msg`
- `pre-push`
- `post-checkout`

If a hook exits non-zero, then the command that invoked the hook will be **aborted**.

### Commit message template


The commit message convention guidelines can be viewed in [commit_tempate.txt](git-hooks/commit_template.txt).

### Hooks


||`pre-commit` |`commit-msg`  |`pre-push`| `post-checkout`|
|---|---|---|---|---|
|Invoked by|`git commit`|`git commit`|`git push`| e.g. `git checkout`|
|Used for|Automatically format specified files for you.|Validate the commit message.|Automatically check the compilation of staged files.|Clean generated files when checking out.|
|Can exit non-zero||:heavy_check_mark:|:heavy_check_mark:||

## Setup

To setup the git hooks locally, run the following commands:

- `cd git-hooks`
- `chmod +x install-hooks.bash`
- `./install-hooks.bash`

