# Shortest path solver
![Github Actions](https://github.com/Kaltsoon/ohtu-2021-viikko1/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/antonlep/shortest-path/branch/master/graph/badge.svg?token=95Q7ZhVw8A)](https://codecov.io/gh/antonlep/shortest-path)

Shortest path solver in Python.

## Documentation
[Project definition](https://github.com/antonlep/shortest-path/blob/master/documentation/project_definition.md)

[Test document](https://github.com/antonlep/shortest-path/blob/master/documentation/test_document.md)

[Weekly report 1](https://github.com/antonlep/shortest-path/blob/master/documentation/weekly_report1.md)

[Weekly report 2](https://github.com/antonlep/shortest-path/blob/master/documentation/weekly_report2.md)

[Weekly report 3](https://github.com/antonlep/shortest-path/blob/master/documentation/weekly_report3.md)


## Installation

Requires Python (>=3.8) and Poetry (>=1.1.11)

- Install dependencies `poetry install`

## Instructions

### Calculate shortest distance between two points

`poetry run invoke start dijkstra Berlin_0_256 164 62 64 139`

dijkstra: shortest path algorithm (dijkstra | a_star)

Berlin_0_256: map file name (located in src/data folder)

146: start location x coordinate

62: start location y coordinate

64: end location x coordinate

139: end location y coordinate

Picture with shortest route and visited nodes is saved as .png file to src/data/

### Run tests

`poetry run invoke test`

### Generate a test coverage report to htmlcov directory

`poetry run invoke coveragehtml`

### Run pylint checks

`poetry run invoke lint`

## Instructions without poetry

Requires Pillow (>=9.0.1)

`python3 src/index.py dijkstra Berlin_0_256 164 62 64 139`
