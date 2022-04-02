import queue
import math
from distance import Distance


class AStar(Distance):
    """Class that calculates shortest distance with A* algorithm.

    """

    def calculate_distance(self, graph, start, end):
        """Calculates shortest distance with A* algorithm.

        Args:
            graph: Dictionary which includes neighboring nodes and their cost
                   {(x,y): [((x2,y2), 1)]}
            start: Tuple with x, y coordinates of start point
            end: Tuple with x, y coordinates of end point

        Returns:
            Tuple of shortest distance (float), shortest route (list) and visited nodes (list)
        """
        if start not in graph or end not in graph:
            return -1, [], []
        distance = {}
        previous = {}
        ready = {}
        for i in graph:
            distance[i] = self.inf
            ready[i] = False
        distance[start] = 0
        priority_queue = queue.PriorityQueue()
        f_cost = self.heuristic(start, end)
        priority_queue.put((f_cost, start))
        while not priority_queue.empty():
            _, x = priority_queue.get()
            if x == end:
                break
            ready[x] = True
            for y in graph[x]:
                old = distance[y[0]]
                new = distance[x] + y[1]
                if new < old:
                    distance[y[0]] = new
                    previous[y[0]] = x
                    f_cost = new + self.heuristic(y[0], end)
                    priority_queue.put((f_cost, y[0]))
        if distance[end] == self.inf:
            return -1, [], []
        route = self.calculate_route(previous, start, end)
        visited = self.calculate_visited(ready)
        return distance[end], route, visited

    def heuristic(self, node, end):
        """Heuristic calculation.

        Args:
            node: start node coordinates
            end: end node coordinates

        Returns:
            Euclidean distance between start and end points.
        """
        return math.sqrt((node[0]-end[0])**2+(node[1]-end[1])**2)
