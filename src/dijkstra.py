from heapq import heappush, heappop


class Dijkstra:
    """Class that calculates shortest distance with Dijkstra algorithm.

    """

    def __init__(self):
        self.inf = 1e99

    def calculate_distance(self, graph, start, end):
        """Calculates shortest distance with Dijkstra algorithm.

        Args:
            graph: Dictionary which includes neighboring nodes and their cost {(x,y): [((x2,y2), 1)]}  
            start: Tuple with x, y coordinates of start point
            end: Tuple with x, y coordinates of end point

        Returns:
            Tuple of shortest distance, shortest route and visited nodes
        """

        distance = {}
        previous = {}
        ready = {}
        for i in graph:
            distance[i] = self.inf
            ready[i] = False
        distance[start] = 0
        heap = []
        heappush(heap, (0, start))
        while heap:
            d, x = heappop(heap)
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
                    heappush(heap, (new, y[0]))
        if distance[end] == self.inf:
            return -1, [], []
        route = self.calculate_route(previous, start, end)
        visited = self.calculate_visited(ready)
        return distance[end], route, visited

    def calculate_route(self, previous, start, end):
        """Calculates route.

        Args:
            previous: Dictionary with previous nodes that connect to the node.
            start: Tuple with x, y coordinates of start point
            end: Tuple with x, y coordinates of end point

        Returns:
            List of nodes on a route.
        """
        route = [end]
        u = end
        while u != start:
            route.append(previous[u])
            u = previous[u]
        return route

    def calculate_visited(self, ready):
        """Returns visited nodes.

        Args:
            ready: Dictionary which has value True if node is visited, False otherwise

        Returns:
            List of visited nodes.
        """
        visited = []
        for key, value in ready.items():
            if value == True:
                visited.append(key)
        return visited
