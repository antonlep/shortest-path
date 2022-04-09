# Test document
## Unit testing
Each class has been separately tested with Python unittest framework.
![coverage](https://user-images.githubusercontent.com/76871257/162572972-7839da38-b157-4e79-a766-0d2b70b6b6eb.png)

https://app.codecov.io/gh/antonlep/shortest-path.

### MapImage
Map file import and graph creation is tested with two input files. Adding route to existing image is also tested. Testing of file loading from disk and saving to disk could be improved.
### Dijkstra, AStar and JPS
For these three classes, shortest distance, shortest route and visited nodes are tested with three input graphs and various start and end locations.
### Distance
Distance class own methods are tested in case that the class is classed without using subclass.
## Manual testing
Program has been manually tested with Moving AI pathfinding benchmark example using Berlin_0_256.map scenario file. Calculated shortest distance was correct with a couple of different start and end points, and with both Dijkstra and A* algorithm. In addition, route and visited nodes have been tested with a simple reference case:

Dijkstra:

![dijkstra](https://user-images.githubusercontent.com/76871257/161380415-1bc8d1d6-a67d-4843-8877-4e112426ca50.PNG)

A*:

![a_Star](https://user-images.githubusercontent.com/76871257/161380419-8547b7c3-0138-4ce5-9e5d-fa61599aac9e.PNG)
