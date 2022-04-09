# Test document
## Unit testing
Each class is separately tested with Python unittest framework.
![coverage](https://user-images.githubusercontent.com/76871257/162572972-7839da38-b157-4e79-a766-0d2b70b6b6eb.png)

https://app.codecov.io/gh/antonlep/shortest-path.

### MapImage
Map file import and graph creation is tested with two input files. Adding route to existing image is also tested. Testing of file loading from disk and saving to disk could be improved.
### Dijkstra, AStar and JPS
For these three classes, shortest distance, shortest route and visited nodes are tested with three input graphs and various start and end locations.
### Distance
Distance class own methods are tested in case that the class is classed without using subclass.
## Manual testing
Four reference test cases have been made with four different map files. In all cases the calculated shortest path and visited nodes are correct. Color codes: wall = white, unvisited floor = blue, visited floor = red, shortest route = black, start point = yellow, end point = green. 

### test_small.map, start point (0,4), end point (7,4), shortest distance 10.07
![test_small](https://user-images.githubusercontent.com/76871257/162573767-1d47e352-cf83-48e9-a351-9cc543c1722c.PNG)
