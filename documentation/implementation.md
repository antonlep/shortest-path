# Implementation
## Program structure
```mermaid
 classDiagram
      main ..> InputParser
      main ..> TextUI
      main ..> MapImage
      main ..> Service
      main ..> Algorithm
      TextUI -- Service
      TextUI -- MapImage
      Service ..> Algorithm
      Service ..> MapImage
      Service ..> Graph
      Dijkstra ..> Graph
      AStar ..> Graph
      JPS ..> Graph
      Graph ..> MapImage
      Algorithm --|> Dijkstra
      Algorithm --|> AStar
      Algorithm --|> JPS
      class main{
      }
      class InputParser{
      }
      class Algorithm{
      }
      class MapImage{
      }
      class Graph{
      }
      class Dijkstra{
      }
      class AStar{
      }
      class JPS{
      }
```
Program is divided into nine classes, and main executable file index.py. Short description of classes:
### MapImage
MapImage includes operations for creating MapImage object from input text file, adding routes and points to the image and saving an image to the disk. Python Imaging Library (pillow) is used for image operations.
### Algorithm
Distance calculation algorithms are implemented with template method pattern. Algorithm class is superclass, which includes basic methods for creating shortest route and visited nodes, and skeleton method for distance calculation. Includes method also for running benchmark cases.
### Dijkstra, AStar and JPS 
These subclasses inherit the Algorithm class and overwrite its distance calculation method.
### TextUI
Class for text-based user interface. Includes methods for reading user input and outputting text to console. There is association to MapImage and Service classes.
### Service
Has upper class methods for running distance calculation and benchmark cases using MapImage objects. Purpose of Service class is to have common methods that multiple other classes need in one place.
### Graph
Class that includes methods for graph manipulation and is used to convert map file to graph file format.
### Input parser
Class for parsing command line arguments.

## Algorithm implementations
Dijkstra and A* algorithm implementations are based on Tietorakenteet ja Algoritmit book and Wikipedia articles. JPS (jump point search) algorithm is based on Harabor and Grastien article. 2D grid is modelled as adjacency matrix (python list of lists) where each node includes neighboring nodes and their distance (1 to horizontal and vertical direction, sqrt(2) to diagonal direction).

### Dijkstra
Algorithm uses python PriorityQueue for storing nodes to be calculated. PriorityQueue is build on Python heapq module, which is based on a binary heap Nodes are arranged in queue based on their distance from start point, so that nodes with shortest distance from start are gone through first:
```
queue.put((0,start)
while not queue.empty()                 # O(n)
    node = queue.get()                  # O(log n)  
    if closed[node]
        continue
    closed[node] = true
    for neighbor, dist in graph[node]   # O(8)
        old = distance[neighbor]
        new = distance[node]+dist
        if new < old
            distance[neighbor] = new
            queue.put((new, neighbor))  # O(log n)
```
In the case of 2D grid examined here, number of nodes in a graph is x * y = n, where x is number of nodes in horizontal direction and y in vertical direction. In worst case, all nodes are gone through in a while loop, which takes O(n) time. Inside one iteration, PriorityQueue get() method is called once (takes O(log n) time for binary heap). Then adjacent neighbor nodes are gone through inside for loop. There can be zero to eight neighbor nodes, so maximum number of iterations is 8. Inside this for loop, PriorityQueue put() method can be called once for each iteration, each function call taking O(log n) amount of time. Maximum total time used is O(n(log n + 8 log n)), which can be simplified to O(n(8 log n)) and further to O(n log n).

Largest data structure is a list inside a list, where nodes and their neighbors are stored. Space complexity is O(8n).

### A*
Algorithm is almost the same as Dijkstra, except heuristic function is included. Order in which nodes are to be calculated is based on the sum of distance from start to the current node and estimated distance from current node to the end (calculated with euclidean distance). Nodes with shortest total estimated distance are to be calculated first:
```
f_cost = distance_to_end(start)
queue.put(f_cost,start)
while not queue.empty()                 # O(n)
    node = queue.get()                  # O(log n)  
    if closed[node]
        continue
    closed[node] = true
    for neighbor, dist in graph[node]   # O(8)
        old = distance[neighbor]
        new = distance[node]+dist
        if new < old
            distance[neighbor] = new
            f_cost = new + distance_to_end(neighbor)
            queue.put((f_cost, neighbor))  # O(log n)
```
In comparison to Dijkstra, there is additional calculation to estimate distance from current node to the end. This is a simple calculation taking O(1) time, so it doesn't cause significant increase in calculation time. Theoretically maximum calculation time is the same O(n log n) as for Dijkstra, but on average the algorithm is faster because heuristic function ensures that nodes that are closer to the end are calculated first, so there will be less visited nodes in total. 

Space complexity is the same O(8n) as for Dijkstra.

### Jump Point Search
Algorithm is quite similar to A*. Difference is that in A* all neighbors are considered for distance calculation, but in JPS only certain nodes, so called jump points, are calculated more extensively. There is additional processing where jump points are identified based on direction and if neighbor nodes are blocked or not. This processing is done with recursive jump method, which returns jump point if it is found:
```
f_cost = distance_to_end(start)
queue.put(f_cost,start)
while not queue.empty()                 # O(n)
    node = queue.get()                  # O(log n)  
    if closed[node]
        continue
    closed[node] = true
    neighbors = prune(neighbors)        # O(1)
    successors = []
    for neighbor in neighbors           # O(8)
        jump_point = jump(neighbor)     # O(n/2)
        successors.append(jump_point)
    for successor in successors         # O(8)
        old = distance[successor]
        new = distance[node]+distance(node, successor)
        if new < old
            distance[successor] = new
            f_cost = new + distance_to_end(successor)
            queue.put((f_cost, successor))  # O(log n)
```
In theory, if the examined node is in the middle of the map and jump point method goes through all directions until the end of the map, it would take O(8n/2) = O(n) amount of time. In this case, the total calculation time for the algorithm would be O(n(log n + n)) = O(n^2). This shows that the calculation time for one iteration (taking one node from queue, processing etc.) is greater than for Dijkstra and A*. On the other hand, JPS doesn't need to do nearly as many iterations than Dijkstra or A*, because it can "jump" in straight line for longer distance between nodes, and consequently doesn't need to do so many computationally expensive queue.get() and queue.put() operations. This causes JPS to be overally faster than A* with typical 2D grids.

Space complexity is the same O(8n) as for other algorithms.

## Performance comparison
Performance analysis with three maps and about 6000 calculation cases ([Test document](https://github.com/antonlep/shortest-path/blob/master/documentation/test_document.md)) showed that JPS is faster, A* second and Dijkstra slowest, as could be expected based on theoretical analysis. On average, A* was 2.16 times faster than Dijkstra and JPS 3.20 times faster than Dijkstra. 

## Improvement areas
- Because calculation takes relatively long time especially for large grids, some faster programming language than Python could be used, for example Java or C++. 
- In some web sources it was mentioned that JPS could be even faster in comparison to A* than was achieved here. Could be related to JPS implementation details or Python language features.
- Class structure could be improved, for example methods related to handling command line arguments could be moved from index.py to a new class. 
- Graphical user interface could be added.
- Algorithm code could be made more clear, also redundant code could be removed.
## Sources
[Laaksonen, Antti "Tietorakenteet ja algoritmit" (2021)](https://github.com/hy-tira/tirakirja/raw/master/tirakirja.pdf)

[Dijkstra algorithm, Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

[A* algorithm, Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)

[Harabor, Daniel, and Alban Grastien. "Online graph pruning for pathfinding on grid maps." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 25. No. 1. 2011.](http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf)
