# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Fixed

### Changed

### Removed

## [0.3.0] - 2025-08-25
### Added
- The CLI command `remove-outliers-for-column` has the same behaviour as the previous `remove-outliers`.
### Changed
- The CLI command `remove-outliers` now removes outliers for columns of interest.

## [0.2.2] - 2025-08-21

### Fixed
- CLI command `remove-outliers` now prints the inferior and superior limits.

## [0.2.1] - 2025-08-21

### Fixed
- Add typer entrypoint `guadalupe-weather`.

## [0.2.0] - 2025-08-21

### Added
- CLI command `remove-outliers`. Removes outliers using Tukey fences on a specified column.


## [0.1.0] - 2025-08-19

### Added
- CLI command `version`
- Extracted package from [`clima_guadalupe`](https://bitbucket.org/IslasGECI/clima_guadalupe/src/develop/
)

[unreleased]: https://github.com/IslasGECI/guadalupe_weather/compare/v1.1.1...HEAD
[0.1.0]: https://github.com/IslasGECI/guadalupe_weather/releases/tag/v0.0.1
