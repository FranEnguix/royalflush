# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html), limiting the versioning semantics to major, minor and patch versions.


## [Unreleased]

## [0.4.1] - 2025-04-17

### Changed
- Updated `pyproject.toml` to specify the license using the new recommended format.
- Updated `README.md` with the installation information.

### Fixed
- Switched `OrderedDict` to `Dict` to fix mypy warnings.

## [0.4.0] - 2025-04-15

### Added
- Improved UUID4 log filtering with a dedicated class.
- Auto-fix graph maximum order when nodes < 2 to increase the convergence speed.

### Changed  
- Weight convergence is now logged based on time instead of epochs and algorithm rounds.  
- Consensus now uses only the most recent weights.
- Suppressed SPADE warning messages.

### Fixed
- Removed Softmax from CNN output.
- Corrected tensor order in consensus formula.
- Corrected tests for the new consensus system.
- Fixed a bug preventing program termination.
- Improved `CHANGELOG.md` clarity.
- Removed SimilarityVector messages in ACoL algorithm.
- Removed ValueError if maximum order < 2.

## [0.3.5] - 2025-02-24

### Added
- Coordinator flag to track if agents are subscribed to their neighbors.
- Example graphs in the `royalflush_graphs` folder.  

### Changed
- Pytest graphs are now created in the `royalflush_test_graphs` folder.  
- Upgraded Torch from 1.11.0 to 2.6.0.  
- Upgraded Torchvision from 0.12.0 to 0.21.0. 
- Renamed `test.json` to `test_experiment.json`.

### Fixed
- Console output now removes UUID4 only when preceded by a double underscore.

## [0.3.4] - 2025-02-17

### Added
- PMACoFL Max algorithm.
- Parsing for Diritchlet alpha input.
- `ReputationManager` class.
- `xmpp_domain` to json template.
- Sphinx-RTD documentation webpage.

### Changed
- ReadTheDocs package info.

### Fixed
- CLI preventing running the client.

## [0.3.3] - 2025-01-27

### Changed
- Default Small-World graph set to k=4 and p=0.3.

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
- `bump2version` for `bump-my-version` package.

### Removed
- `.bumpversion.cfg` file.

### Fixed
- Version numbers in `CHANGELOG.md`.

## [0.2.0] - 2024-10-17

### Added
- Project configuration files.
- Read The Docs [documentation](https://royalflush.readthedocs.io/en/latest/).

## [0.1.0] - 2024-10-17

### Added
- Push initial commit.
- PyPI integration [royalflush](https://pypi.org/project/royalflush/).


