# Git Workflow Step-by-Step Guide

This guide explains the Git commands needed to follow the Git workflow effectively. It covers everything from setting up your repository to handling different types of branches and preparing for a release.

## Initial Setup

1. **Clone the Repository**
   - To start working with the repository, clone it to your local machine:
     ```bash
     git clone <repository-url>
     cd <repository-name>
     ```

2. **Create the Develop Branch**
   - Immediately create a develop branch if it doesn't already exist:
     ```bash
     git checkout -b develop
     git push -u origin develop
     ```

## Working with Branches

### Feature Branches

1. **Create a Feature Branch**
   - When starting work on a new feature, branch off from `develop`:
     ```bash
     git checkout develop
     git checkout -b feature/<feature-name>
     ```
   
2. **Push the Feature Branch**
   - Regularly push your branch to keep it synced:
     ```bash
     git push -u origin feature/<feature-name>
     ```

3. **Merge the Feature Branch**
   - After completing the feature and conducting necessary reviews and tests:
     ```bash
     git checkout develop
     git merge feature/<feature-name>
     git push origin develop
     ```
   - Optionally, delete the feature branch if it's no longer needed:
     ```bash
     git branch -d feature/<feature-name>
     git push origin --delete feature/<feature-name>
     ```

### Release Branches

1. **Create a Release Branch**
   - To prepare a new version release from `develop`:
     ```bash
     git checkout develop
     git checkout -b release/<version>
     ```

2. **Complete the Release**
   - Finalize the release, fix bugs, and finalize documentation:
     ```bash
     git commit -m "Final changes for release"
     ```

3. **Merge the Release Branch**
   - Merge into `master` and tag the release:
     ```bash
     git checkout master
     git merge release/<version>
     git tag -a <version> -m "Release <version>"
     git push origin master
     git push origin <version>
     ```

   - Also, merge back into `develop` to include any last-minute changes made in the release:
     ```bash
     git checkout develop
     git merge release/<version>
     git push origin develop
     ```

   - Optionally, delete the release branch:
     ```bash
     git branch -d release/<version>
     git push origin --delete release/<version>
     ```

### Hotfix Branches

1. **Create a Hotfix Branch**
   - If an urgent fix is required in production, branch off from `master`:
     ```bash
     git checkout master
     git checkout -b hotfix/<hotfix-name>
     ```

2. **Complete the Hotfix**
   - Make necessary changes and commit them:
     ```bash
     git commit -m "Fix urgent issue"
     ```

3. **Merge the Hotfix Branch**
   - Merge back to `master` and tag if necessary:
     ```bash
     git checkout master
     git merge hotfix/<hotfix-name>
     git push origin master
     ```

   - Also, merge into `develop`:
     ```bash
     git checkout develop
     git merge hotfix/<hotfix-name>
     git push origin develop
     ```

   - Optionally, delete the hotfix branch:
     ```bash
     git branch -d hotfix/<hotfix-name>
     git push origin --delete hotfix/<hotfix-name>
     ```

## Conclusion

This step-by-step guide provides a clear framework for managing branches and preparing releases using Git. By adhering to this workflow, you ensure that your repository remains organized and that all changes are integrated smoothly and efficiently.
