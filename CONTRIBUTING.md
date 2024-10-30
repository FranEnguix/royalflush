# Contributor Guide

Welcome to the **Royal FLush** project! This guide will help you understand how to contribute effectively, including how to manage versioning and write changelog entries.

## Versioning Overview

We use a versioning based on the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format, and this project adheres to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html), limiting the versioning semantics to [this](https://regex101.com/r/4HWpCE/2) custom regular expression. Which means our version numbers follow the format:

```
MAJOR.MINOR.PATCH[-PRERELEASE[.VERSION]]
```

- **MAJOR**: Incompatible API changes.
- **MINOR**: Added functionality in a backward-compatible manner.
- **PATCH**: Backward-compatible bug fixes.
- **PRERELEASE**: Indicates unstable versions (`alpha`, `beta` and `rc`).
- **VERSION**: Backward-compatible code increments.

## Types of Changes

When contributing, categorize your changes using the following labels:

- **Added**: New features.
- **Changed**: Modifications to existing functionality.
- **Deprecated**: Features that will be removed in future releases.
- **Removed**: Features removed in this release.
- **Fixed**: Bug fixes.
- **Security**: Vulnerability fixes.

## Branching Model

We follow the [Gitflow](https://nvie.com/posts/a-successful-git-branching-model/) model with `main` and `develop` branches. Feature branches may be created from `develop` and merged back after completion.

## Bumping Versions with `bump2version`

We use `bump2version` for managing version numbers. Here's how to use it:

1. **Install bump2version**:

   ```bash
   pip install bump2version
   ```

2. **Determine the Version Part to Bump**:

   - **MAJOR**: For incompatible API changes.
   - **MINOR**: For new features and deprecations.
   - **PATCH**: For bug fixes and security patches.
   - **PRERELEASE**: Optional. For unstable versions.
   - **VERSION**: Optional. For version increment.

3. **Run bump2version**:

   ```bash
   bump2version [part]
   ```

   Replace `[part]` with `version`, `prerelease`, `patch`, `minor` or `major`.

4. **For Prerelease Versions**:

   Specify the `--new-version` flag with the prerelease tag:

   ```bash
   bump2version --new-version 1.2.0-alpha.1 prerelease
   ```

## Writing Changelog Entries

- **Location**: Add your entries under the `[Unreleased]` section in `CHANGELOG.md`.
- **Format**:

  ```markdown
  ### [Type of Change]
  - Description of change.
  ```

- **Example**:

  ```markdown
  ### Added
  - Implemented new data caching mechanism.

  ### Fixed
  - Resolved issue with incorrect data parsing in edge cases.
  ```

## Submitting a Pull Request

1. **Fork the Repository**: Create a personal fork of the project.
2. **Create a Feature Branch**: Use descriptive names like `feature/data-caching`.
3. **Commit Changes**: Write clear commit messages.
4. **Update Changelog and Version**: Edit `CHANGELOG.md` and bump the version if necessary.
5. **Push to Your Fork**: Push your feature branch to your forked repository.
6. **Create a Pull Request**: Submit a PR to the `main` branch of the original repository.

## Example Scenarios

### Adding a New Feature

- **Branch**: `feature/new-awesome-feature`
- **Version Bump**: Minor (`bump2version minor`)
- **Changelog Entry**:

  ```markdown
  ### Added
  - Introduced a new awesome feature that enhances user experience.
  ```

### Fixing a Bug

- **Branch**: `bugfix/resolve-crash-on-startup`
- **Version Bump**: Patch (`bump2version patch`)
- **Changelog Entry**:

  ```markdown
  ### Fixed
  - Resolved a crash that occurred during startup when no config file is present.
  ```

### Making a Breaking Change

- **Branch**: `feature/api-overhaul`
- **Version Bump**: Major (`bump2version major`)
- **Changelog Entry**:

  ```markdown
  ### Changed
  - Overhauled the API for better consistency; this introduces breaking changes.
  ```

### Security Patch

- **Branch**: `hotfix/security-fix`
- **Version Bump**: Patch (`bump2version patch`)
- **Changelog Entry**:

  ```markdown
  ### Security
  - Patched a vulnerability in input validation that could lead to injection attacks.
  ```

## Final Notes

- **Testing**: Ensure all tests pass before submitting your PR.
- **Documentation**: Update or add documentation for new features or changes.
- **Communication**: If in doubt, open an issue to discuss your proposed changes before implementation.

Thank you for contributing to **Royal FLush**!