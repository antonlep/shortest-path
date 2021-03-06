# Test document
## Unit testing
Each class is separately tested with Python unittest framework. In addition there is TestBenchmark class for testing distance calculation with large map.

![coverage](https://user-images.githubusercontent.com/76871257/167906924-03763951-968b-4b5f-9561-6fc8cac6c99c.PNG)


https://app.codecov.io/gh/antonlep/shortest-path.

### MapImage
Map file import and graph creation is tested with two input files. Adding route to existing image is also tested. Testing of file loading from disk and saving to disk could be improved, at the moment it is tested by actually writing files to disk.
### Dijkstra, AStar and JPS
For these three classes, shortest distance, shortest route and visited nodes are tested with three input graphs and various start and end locations. JPS class has additional methods which are separately tested.
### Algorithm
Algorithm class own methods are tested in case that the class is used without using subclass. 
### Graph
Graph creation is tested with two maps.
### Input parser
A few cases with different input arguments are tested.
### MapImage
Image import, point and route addition and image saving are tested with two maps.
### Service
Class methods are tested with help of mock classes.
### TestBenchmark
Distance is calculated in a large map with random start and end locations. In total 20 cases are calculated. A* and JPS distance is compared to Dijkstra, which is used as reference case.

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
Berlin_0_256.map, Berlin_1_1024.map and Boston_0_256.map files from Moving AI Lab are used as a benchmark case for comparison between algorithms ([Sturtevant, Nathan R. "Benchmarks for grid-based pathfinding." IEEE Transactions on Computational Intelligence and AI in Games 4.2 (2012): 144-148.](https://www.cs.du.edu/~sturtevant/papers/benchmarks.pdf)). Berlin_1_1024 is the same map as Berlin_0_256 only in larger size, 1024x1024 instead of 256x256.

### Berlin_0_256 and Berlin_1_1024
![berlin_map](https://user-images.githubusercontent.com/76871257/166102499-1a2217e5-0ea6-461c-b16d-f7ffbe450560.PNG)

### Boston_0_256
![boston_map](https://user-images.githubusercontent.com/76871257/166102501-2f905345-f6d5-4fce-807b-f0354d0b77f6.PNG)

### Result comparison
![berlin_0_256](https://user-images.githubusercontent.com/76871257/164909280-3e03fe10-eda4-4a6b-befe-e94341b60533.PNG)

![berlin_1_1024](https://user-images.githubusercontent.com/76871257/164909284-07dc1702-0f8d-40d9-a6b8-9c6c88a96ea8.PNG)

![boston_0_256](https://user-images.githubusercontent.com/76871257/166102351-a5743eea-6f34-4924-95ff-4fc09a555c50.PNG)


| Map           | Number of cases | Time, Dijkstra | Time, A*  | Time, JPS |
| ------------- | --------------- | -------------- | --------- | --------- |
|  Berlin_0_256 |            930  |       159.73 s |   75.38 s |   48.40 s |           
| Berlin_1_1024 |           3920  |     14084.59 s | 7120.11 s | 4554.53 s |
|  Boston_0_256 |            950  |       162.68 s |   71.50 s |   51.78 s |

According to calculation times, Dijkstra is slowest, A* is about two times faster, and JPS is about 1.5 times faster than A*. That makes sense considering that A* is supposed to be improvement of Dijkstra, and JPS improvement of A*. With shortest path lengths, there is not much difference between algorithms. Probably the distance calculation itself doesn't take so much time with these lengths. Differences start to be more visible with longer path lengths. For Dijkstra, there is clear upper limit for calculation time visible. These are the cases where the full map has been explored, so it is not possible for calculation time to grow anymore.

There is some difference between Berlin and Boston maps. Probably because Berlin map has more open spaces, JPS algorithm is slightly faster there. In open spaces less jump points are created in comparison to small closed spaces.

Results with larger grid 1024x1024 are more clear in comparison to smaller map, most likely because pixel size is smaller in comparison to obstacles which doesn't create as much distraction to route calculation.
