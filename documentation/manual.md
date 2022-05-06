## Installation

Requires Python (>=3.8) and Poetry (>=1.1.11)

- Install dependencies `poetry install`

## Instructions

### Calculate shortest distance between two points

`poetry run invoke start dijkstra Berlin_0_256 164 62 64 139`

dijkstra: shortest path algorithm (dijkstra | a_star | jps)

Berlin_0_256: map file name (located in src/data folder)

146: start location x coordinate

62: start location y coordinate

64: end location x coordinate

139: end location y coordinate

Picture with shortest route and visited nodes is saved as .png file to src/data/

### Calculate benchmark case

`poetry run invoke benchmark dijkstra Berlin_0_256`

dijkstra: shortest path algorithm (dijkstra | a_star | jps)

Berlin_0_256: map.scen file name (located in src/data folder)

Results are saved as .csv file to src/data/

### Run tests

`poetry run invoke test`

### Generate a test coverage report to htmlcov directory

`poetry run invoke coveragehtml`

### Run pylint checks

`poetry run invoke lint`

## Instructions without poetry

Requires Pillow (>=9.0.1)

`python3 src/index.py dijkstra Berlin_0_256 164 62 64 139`
