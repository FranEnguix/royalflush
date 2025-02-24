# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html), limiting the versioning semantics to major, minor and patch versions.


## [Unreleased]


## [0.3.5] - 2025-02-24

### Added
- Add coordinator flag to know if agents are subscribed to their neighbours.
- Add example graphs in `royalflush_graphs` folder.

### Changed
- Now pytest graphs are created in `royalflush_test_graphs` folder.
- Upgraded torch version from 1.11.0 to 2.6.0.
- Upgraded torchvision version from 0.12.0 to 0.21.0.
- Renamed the experiment file `test.json` to `test_experiment.json`. 

### Fixed
- Now the console output only removes UUID4 when preceded by a double underscore.

## [0.3.4] - 2025-02-17

### Added
- Add PMACoFL Max algorithm.
- Add parsing to Diritchlet alpha input.
- Add ReputationManager class.
- Add xmpp_domain to json template.
- Add sphinx-rtd documentation webpage.

### Changed
- ReadTheDocs package info.

### Fixed
- CLI preventing running the client.

## [0.3.3] - 2025-01-27

### Changed
- Replace default Small-World graph set to k=4 and p=0.3.

### Fixed
- Circular import bug.

## [0.3.2] - 2025-01-17

### Fixed
- Circular import bug.

## [0.3.1] - 2025-01-17

### Fixed
- Circular import bug.

## [0.3.0] - 2025-01-15

### Added
- Start the first foundational project structure.
- Functional minimal version with templates.

### Changed
- Replace `bump2version` for `bump-my-version`.

### Removed
- Delete `.bumpversion.cfg` file.

### Fixed
- Fix version numbers in `CHANGELOG.md`.

## [0.2.0] - 2024-10-17

### Added
- Project configuration files.
- Add Read The Docs [documentation](https://royalflush.readthedocs.io/en/latest/).

## [0.1.0] - 2024-10-17

### Added
- Push initial commit.
- Add PyPI integration [royalflush](https://pypi.org/project/royalflush/).


