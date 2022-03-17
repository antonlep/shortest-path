# Project definition
The purpose of this work is to compare two algorithms for calculating shortest distance between two points in a grid. Program will be made in Python (I can do peer reviews in projects made with Python, no sufficient knowledge of other languages).

## Algorithms and data structures
Used algorithms are JPS (Jump Point Search) and Dijsktra. Existing Python data structures will be used. Main goal is to compare the performance of these two algorithms in shortest path calculation in a uniform 2D grid, which consists of "free" and "blocked" squares. Dijkstra algorithm is chosen because of its familiarity, JPS because of its supposedly improved performance in comparison to Dijkstra in uniform-cost grid.

## Input and output
* Input files are 2D grid files that are in Moving AI lab .map format [1]
* Simple console UI is used to choose start and end points and select the algorithm
* Output is an image of shortest distance on a map (as .png file), calculated shortest distance value and calculation time

## Time and space complexity
Target time complexity is O(n + m log m) for Dijkstra[2], where n and m are number of nodes and edges. JPS is an improvement to A* search, which has worst-case time complexity O(b^d), where b is branching factor and d is depth [3]. Actual time complexity of JPS is expected to be better, because of heuristic that is used eliminates large number of nodes. In a way, algorith jumps from node to node in straight lines, without going with small steps like original A* algorithm. Overall, it is expected that JPS has better time complexity than Dijkstra in this case, altough magnitude of improvement is unclear.
Target space complexities are O(n + m ) for both algorithms (all vertices and edges stored in memory)

## Sources
[1] Sturtevant, N. R. (2012). Benchmarks for grid-based pathfinding. IEEE Transactions on Computational Intelligence and AI in Games, 4(2), 144-148. DOI: 10.1109/TCIAIG.2012.2197681

[2] https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

[3] https://en.wikipedia.org/wiki/Jump_point_search


## Study program
Tietojenkäsittelytieteen kandidaatti

## Documentation language
English
