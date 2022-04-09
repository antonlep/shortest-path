# Implementation
## Program structure
Program is divided into five classes, and main executable file main.py. Short description of classes:
### MapImage
MapImage includes operations for creating MapImage object, coverting it to graph format, adding routes and points to the image and saving the image to disk.
### Distance
Distance calculation algorithms are implemented with template method pattern. Distance class is superclass, which includes basic methods for creating shortest route and visited nodes, and skeleton methods for distance calculation and heuristic.
### Dijkstra, AStar and JPS 
These subclasses inherit the Distance class. Each class has its own distance calculation method according to the algorithm in use.
## Performance comparison
Berlin_0_256.map file is used as benchmark case for comparison between algorithms (https://movingai.com/benchmarks/grids.html).

| Start point | End point   | Time, Dijkstra | Time, A* | Time, JPS | Shortest distance |
| ----------- | ----------- | ----------- | ----------- | --------- | ----------------- |
| 79, 89       | 197, 57    | 0.182       | 0.027       | 0.082     | 145.7             |
| 220, 21       | 150, 220    | 0.240       | 0.137       | 4.066     | 258.1             |
| 9, 25       | 245, 251    | 0.265       | 0.258       | 4.120     | 368.9             |

Based on calculation times, it seems that A* is faster than Dijkstra, which makes sense considering that it is supposed to be improvement to the Dijkstra algorithm, and with the help of heuristic it doesn't have to visit as many nodes than Dijkstra. At the moment JPS is slowest especially with maps with large open spaces, which is in contradiction to theory which states that it should be fastest out of these three. There are some details in current JPS algorithm implementation that can be improved, at the moment it was quickly created without paying much attention to performance. 
## Sources
[Dijkstra algorithm, Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

[A* algorithm, Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)

[Harabor, Daniel, and Alban Grastien. "Online graph pruning for pathfinding on grid maps." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 25. No. 1. 2011.](http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf)

[Sturtevant, Nathan R. "Benchmarks for grid-based pathfinding." IEEE Transactions on Computational Intelligence and AI in Games 4.2 (2012): 144-148.](https://www.cs.du.edu/~sturtevant/papers/benchmarks.pdf)
