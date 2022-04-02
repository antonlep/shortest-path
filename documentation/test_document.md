# Test document
## Unit testing
Each class have been separately tested with Python unittest framework.
Unit test coverage is here: https://app.codecov.io/gh/antonlep/shortest-path.
![coverage](https://user-images.githubusercontent.com/76871257/161379994-a2261783-4fa2-472f-9451-4b8cc87c245d.PNG)

### MapImage
Map file import and graph creation is tested with two input files. Adding route to existing image is also tested. Testing of file loading from disk and saving to disk could be improved.
### Dijkstra
Shortest distance, shortest route and visited nodes are tested with three input graphs and different start and end locations.
### AStar
Shortest distance, shortest route and visited nodes are tested with three input graphs and different start and end locations.
### Distance
What happens if Distance class is used directly instead of using subclass is tested.
