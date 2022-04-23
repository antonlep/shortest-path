# Implementation
## Program structure
Program is divided into seven classes, and main executable file index.py. Short description of classes:
### MapImage
MapImage includes operations for creating MapImage object from input text file, adding routes and points to the image and saving the image to disk. Python Imaging Library (pillow) is used for image operations.
### Distance
Distance calculation algorithms are implemented with template method pattern. Distance class is superclass, which includes basic methods for creating shortest route and visited nodes, and skeleton methods for distance calculation and heuristic.
### Algorithm
Distance calculation algorithms are implemented with template method pattern. Algorithm class is superclass, which includes basic methods for creating shortest route and visited nodes, and skeleton methods for distance calculation and heuristic. Includes method also for running benchmark cases.
### Dijkstra, AStar and JPS 
These subclasses inherit the Distance class and overwrite its distance calculation method. Dijkstra and A* algorithm implementations are based on Tietorakenteet ja Algoritmit book and Wikipedia articles. JPS (jump point search) algorithm is based on Harabor and Grastien article.
### Graph
Class that includes methods for graph manipulation and is used to convert map file to graph file format.
### Input parser
Class for parsing command line arguments.

## Algorithm implementations

### Dijkstra

## Sources
[Laaksonen, Antti "Tietorakenteet ja algoritmit" (2021)](https://github.com/hy-tira/tirakirja/raw/master/tirakirja.pdf)

[Dijkstra algorithm, Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

[A* algorithm, Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)

[Harabor, Daniel, and Alban Grastien. "Online graph pruning for pathfinding on grid maps." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 25. No. 1. 2011.](http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf)
