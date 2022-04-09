import queue
from distance import Distance


class Dijkstra(Distance):
    """Class that calculates shortest distance with Dijkstra algorithm.

    """

    def calculate_distance(self, graph, start, end):
        """Calculates shortest distance with Dijkstra algorithm.

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
        open_list.put((0, start))
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
                    open_list.put((new, neighbor))
        if distance[end] == self.inf:
            return -1, [], []
        route = self.calculate_route(previous, start, end)
        visited = self.calculate_visited(closed)
        return distance[end], route, visited
