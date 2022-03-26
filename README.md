# Shortest path solver
![Github Actions](https://github.com/Kaltsoon/ohtu-2021-viikko1/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/antonlep/shortest-path/branch/master/graph/badge.svg?token=95Q7ZhVw8A)](https://codecov.io/gh/antonlep/shortest-path)

Shortest path solver in Python.

## Documentation
[Project definition](https://github.com/antonlep/shortest-path/blob/master/documentation/project_definition.md)

[Weekly report 1](https://github.com/antonlep/shortest-path/blob/master/documentation/weekly_report1.md)

## Installation

Requires Python (>=3.8) and Poetry (>=1.1.11)

- Install dependencies `poetry install`

## Instructions

### Calculate shortest distance between two points

`poetry run invoke start Berlin_0_256 164 62 64 139`

Berlin_0_256: map file name

146: start location x coordinate

62: start location y coordinate

64: end location x coordinate

139: end location y coordinate

Picture with shortest route and visited nodes are saves as .png file to src/data/

### Run tests

`poetry run invoke test`

### Generate a test coverage report to htmlcov directory

`poetry run invoke coveragehtml`

### Run pylint checks

`poetry run invoke lint`

## Instructions without poetry

Requires Pillow (>=9.0.1)

`python3 src/index.py Berlin_0_256 164 62 64 139`
