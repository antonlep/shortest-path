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
        closed = {}
        for i in graph:
            distance[i] = self.inf
            closed[i] = False
        distance[start] = 0
        open_list = queue.PriorityQueue()
        f_cost = self.heuristic(start, end)
        open_list.put((f_cost, start))
        while not open_list.empty():
            _, x = open_list.get()
            if x == end:
                break
            if closed[x]:
                continue
            closed[x] = True
            for neighbor, dist in graph[x]:
                old = distance[neighbor]
                new = distance[x] + dist
                if new < old:
                    distance[neighbor] = new
                    previous[neighbor] = x
                    f_cost = new + self.heuristic(neighbor, end)
                    open_list.put((f_cost, neighbor))

        if distance[end] == self.inf:
            return -1, [], []
        route = self.calculate_route(previous, start, end)
        visited = self.calculate_visited(closed)
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
