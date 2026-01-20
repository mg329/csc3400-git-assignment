Git Workflow Document:

This document describes the workflow used for the CSC3400 Software Engineering Project

Branching Strategy:
    -A feature-branch strategy was used for this project
    -master
        -always contains working, code which reflects the latest released version to clients
    -feature/* branches
        -Used for developing new features
        -feature/error-handling
        -feature/user-interface
    -hotfix/* branches
        -used for documentation updates and other urgent fixes
            -hotfix/redme-update

Commit Message Conventions:
    -We follow clear and descriptive commit messages
    -Use present tense
    -keep messages short and to the point
    -one logical change per commit

Code Review Process:
    -Developer creates a feature or hotfix branch
    -Changes are pushed to GitHub
    -A pull request is opened against master
    -The pull requestion should explain what was changed, and why the change was needed
    -Code is reviewed for correctness, readability, and error handling
    -Once it is approve, the branch is merged into main

Release Workflow:
    -Ensure main is stable and all tests pass
    -Merge approved feature and hotfix brances into main
    -Push final changes to GitHub

Common Git Commands Reference:
    -git branch
    -git checkout -b branchName/branchSubName
    -git checkout branchName
    -git switch branchName
    -git status
    -git add fileName
    -git commit -m "Commit Message"
    -git pull
    -git push
    -git merge branchName/branchSubName

