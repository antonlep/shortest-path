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

