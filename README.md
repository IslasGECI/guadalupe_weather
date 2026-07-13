<table><tr><td>

# Guadalupe Weather
</td>
<td>
<a href="https://www.islas.org.mx/"><img src="https://www.islas.org.mx/img/logo.svg" width="75%" /></a>
</td></tr></table>
CLI tools for analyzing and visualizing weather data from Isla Guadalupe. This package provides commands for outlier detection, multi-annual temperature and rainfall analysis, and typical-year boxplot rendering.

----
[![codecov](https://codecov.io/gh/IslasGECI/guadalupe_weather/graph/badge.svg?token=RY807ST1T1)](https://codecov.io/gh/IslasGECI/guadalupe_weather)
![example branch
parameter](https://github.com/IslasGECI/guadalupe_weather/actions/workflows/actions.yml/badge.svg)
![licencia](https://img.shields.io/github/license/IslasGECI/guadalupe_weather)
![languages](https://img.shields.io/github/languages/top/IslasGECI/guadalupe_weather)
![commits](https://img.shields.io/github/commit-activity/y/IslasGECI/guadalupe_weather)
![PyPI - Version](https://img.shields.io/pypi/v/guadalupe_weather)

## CLI Usage

The package exposes the `guadalupe-weather` command with the following subcommands:

| Command | Description |
|---|---|
| `render-typical-year-boxplot` | Render a boxplot of a typical year for temperature or cumulative rain |
| `render-temperature-across-year` | Plot temperature across selected years with boxplot overlay |
| `render-rain-across-year` | Plot cumulative rainfall across selected years with boxplot overlay |
| `remove-outliers` | Remove outliers from all columns in a CSV dataset |
| `remove-outliers-for-column` | Remove outliers from a specific column in a CSV dataset |
| `version` | Print the package version |

Use `guadalupe-weather <command> --help` for command-specific options.
