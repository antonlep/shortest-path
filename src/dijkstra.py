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
        ready = {}
        for i in graph:
            distance[i] = self.inf
            ready[i] = False
        distance[start] = 0
        heap = queue.PriorityQueue()
        heap.put((0, start))
        while not heap.empty():
            _, x = heap.get()
            if x == end:
                break
            if ready[x]:
                continue
            ready[x] = True
            for y in graph[x]:
                old = distance[y[0]]
                new = distance[x] + y[1]
                if new < old:
                    distance[y[0]] = new
                    previous[y[0]] = x
                    heap.put((new, y[0]))
        if distance[end] == self.inf:
            return -1, [], []
        route = self.calculate_route(previous, start, end)
        visited = self.calculate_visited(ready)
        return distance[end], route, visited
