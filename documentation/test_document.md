# Test document
## Unit testing
Each class is separately tested with Python unittest framework.
![coverage](https://user-images.githubusercontent.com/76871257/164908658-851ff4bb-d1b6-415e-b946-221e60697192.PNG)

https://app.codecov.io/gh/antonlep/shortest-path.

### MapImage
Map file import and graph creation is tested with two input files. Adding route to existing image is also tested. Testing of file loading from disk and saving to disk could be improved.
### Dijkstra, AStar and JPS
For these three classes, shortest distance, shortest route and visited nodes are tested with three input graphs and various start and end locations.
### Distance
Distance class own methods are tested in case that the class is classed without using subclass.
## Route testing with small map
Four reference test cases have been made with four different map files to validate shortest path and to make sure that visited nodes are correct. In case of JPS algorithm, jump points are examined instead of visited nodes. Color codes: wall = white, unvisited floor = blue, visited floor = red, shortest route = black, start point = yellow, end point = green. 

### test_small.map, start point (0,4), end point (7,4), shortest distance 10.07
![test_small](https://user-images.githubusercontent.com/76871257/162573767-1d47e352-cf83-48e9-a351-9cc543c1722c.PNG)

### test_small2.map, start point (6,5), end point (12,0), shortest distance 22.66
![test_small2](https://user-images.githubusercontent.com/76871257/162574266-80eb12e6-d8fa-431c-a9ca-20d774010c88.PNG)

### test_medium.map, start point (0,4), end point (4,6), shortest distance 22.97
![test_medium](https://user-images.githubusercontent.com/76871257/162574419-60110c6c-01d7-4f28-944d-797c7e304de3.PNG)

### test_medium2.map, start point (2,8), end point (12,8), shortest distance 19.31
![test_medium2](https://user-images.githubusercontent.com/76871257/162574528-b1e8a97e-1e3a-4f07-8cd8-4370ed155bb3.PNG)

## Performance testing with large map
Berlin_0_256.map file from Moving AI Lab is used as a benchmark case for comparison between algorithms ([Sturtevant, Nathan R. "Benchmarks for grid-based pathfinding." IEEE Transactions on Computational Intelligence and AI in Games 4.2 (2012): 144-148.](https://www.cs.du.edu/~sturtevant/papers/benchmarks.pdf)).

| Map          | Start point | End point   | Shortest distance | Time, Dijkstra | Time, A*  | Time, JPS | 
| ------------ | ----------- | ----------- | ----------------- | -------------- | --------- | --------- |
| Berlin_0_256 | 79, 89      |  197, 57    | 145.7             | 0.192          | 0.040     | 0.043     |            
| Berlin_0_256 | 220, 21     |  150, 220   | 258.1             | 0.251          | 0.160     | 0.088     |
| Berlin_0_256 | 9, 25       |  245, 251   | 368.9             | 0.303          | 0.236     | 0.098     |

Based on calculation times, it seems that A* is faster than Dijkstra, which makes sense considering that it is supposed to be improvement to the Dijkstra algorithm, and with the help of heuristic it doesn't have to visit as many nodes than Dijkstra. JPS is generally faster than A*, especially with large maps.
