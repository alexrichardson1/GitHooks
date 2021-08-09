#!/usr/bin/env bash


echo "--- Running pre-push hook ---"
echo "Stashing unstaged changes."
git stash --keep-index -u -q
# compile command here e.g. `make`, `cabal new-build`

if [ $? -eq 0 ]; then
  echo -e "\e[0;92mPre-push hook finished successfully.\e[0m"
  echo "-------------------------------"
  git stash pop -q
  exit 0
fi

echo -e "\e[1;31mfatal: code does not compile!\e[0m"
echo "-------------------------------"
git stash pop -q
exit 1
