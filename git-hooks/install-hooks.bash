#!/usr/bin/env bash

# Run the command `chmod +x ./install-hooks.bash` in the scripts directory

HOOK_DIR=git-hooks
GIT_DIR=$(git rev-parse --git-dir)

chmod +x pre-commit.py commit-msg.py pre-push.bash post-checkout.py

echo "Installing hooks..."
# symlinks to the pre-commit script
git config --local commit.template $HOOK_DIR/commit_template.txt
ln -sf $GIT_DIR/../$HOOK_DIR/pre-commit.py $GIT_DIR/hooks/pre-commit
ln -sf $GIT_DIR/../$HOOK_DIR/commit-msg.py $GIT_DIR/hooks/commit-msg
ln -sf $GIT_DIR/../$HOOK_DIR/pre-push.bash $GIT_DIR/hooks/pre-push
ln -sf $GIT_DIR/../$HOOK_DIR/post-checkout.py $GIT_DIR/hooks/post-checkout
echo "Done!"
