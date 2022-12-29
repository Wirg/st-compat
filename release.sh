#!/usr/bin/env bash
set -e
RELEASE_TYPE=$1
VENV_PATH=$2

shopt -s extglob
if [[ $RELEASE_TYPE == @(minor|major|patch) ]]; then

    echo "\n--> Creating the release branch from main and increment the release version...\n"
    git fetch origin main
    git checkout main
    git reset --hard origin/main
    export new_version=$(poetry version --short)
    git checkout -b release/v${new_version}
    git push origin release/v${new_version} -f

    echo "\n--> Creating the pull requests on GitHub... \nYou may need to enter your GitHub credentials.\n"
    gh pr create --base main --title "Release ${current_version} => ${new_version} into main" --body ""
    gh pr create --base releases --title "Release ${current_version} => ${new_version} into releases" --body ""
    read -p "Ask a team member to approve the pull requests and wait until the tests pass. Then press enter to continue."

    echo "\n--> Merging release branch on releases branch... \n"
    git fetch origin releases
    git checkout releases
    git reset --hard origin/releases
    git merge --no-ff --no-edit release/v${new_version}
    git push

    echo "\n--> Creating a new version tag and updating the latest tag... \n"
    git tag v${new_version}
    git tag -f latest
    git push origin :latest
    git push origin --tags -f

    echo "\n--> Merging release branch on main branch... \n"
    git fetch origin main
    git checkout main
    git reset --hard origin/main
    git merge --no-ff --no-edit release/v${new_version}
    git push

    git branch -D release/v${new_version}
    git push origin :release/v${new_version}

    echo "\n--> Creating release on github... \n"
    rm -f .tmp_release.md
    (echo v${new_version} && cat .github/RELEASE_TEMPLATE.md) > .tmp_release.md
    hub release create v${new_version} --edit --file=.tmp_release.md
    rm -f .tmp_release.md

    echo "\nRelease v${new_version} has been successfully created.\n"
else
    echo "\nThe type must be specified and must be one of the parameters: minor, major, patch... \n"
    exit 0
fi
