# Test document
## Unit testing
Each class have been separately tested with Python unittest framework.
![coverage](https://user-images.githubusercontent.com/76871257/161379994-a2261783-4fa2-472f-9451-4b8cc87c245d.PNG)
https://app.codecov.io/gh/antonlep/shortest-path.

### MapImage
Map file import and graph creation is tested with two input files. Adding route to existing image is also tested. Testing of file loading from disk and saving to disk could be improved.
### Dijkstra
Shortest distance, shortest route and visited nodes are tested with three input graphs and different start and end locations.
### AStar
Shortest distance, shortest route and visited nodes are tested with three input graphs and different start and end locations.
### Distance
What happens if Distance class is used directly instead of using subclass is tested.
## Manual testing
Program has been manually tested with Moving AI pathfinding benchmark example using Berlin_0_256.map scenario file. Calculated shortest path was correct with a few different start and end points, and with both Dijkstra ans A* algorithm. In addition, route and visited nodes have been tested with a simple reference case:
Dijkstra:
![dijkstra](https://user-images.githubusercontent.com/76871257/161380415-1bc8d1d6-a67d-4843-8877-4e112426ca50.PNG)
A*:
![a_Star](https://user-images.githubusercontent.com/76871257/161380419-8547b7c3-0138-4ce5-9e5d-fa61599aac9e.PNG)
