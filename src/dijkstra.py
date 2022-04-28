import queue
from algorithm import Algorithm


class Dijkstra(Algorithm):
    """Class that calculates shortest distance with Dijkstra algorithm.

    """

    def calculate_distance(self, graph, start, end):
        """Calculates shortest distance with Dijkstra algorithm.

        Args:
            graph: 2D-list which includes neighboring nodes and their cost
            start: Tuple with x, y coordinates of start point
            end: Tuple with x, y coordinates of end point

        Returns:
            Tuple of shortest distance (float), shortest route (list) and visited nodes (list)
        """
        if not graph:
            return -1, [], []
        n = len(graph)
        m = len(graph[0])

        # Check if start and end points are outside of graph.
        if (not graph or end[0] < 0 or end[0] >= m or end[1] < 0 or end[1] >= n
                or start[0] < 0 or start[0] >= m or start[1] < 0 or start[1] >= n):
            return -1, [], []

        # Create and initialize dictionary for distance (from start node)
        # and closed (visited) nodes.
        distance = {}
        previous = {}
        closed = {}
        for i in range(m):
            for j in range(n):
                distance[(i, j)] = self.inf
                closed[(i, j)] = False

        # Create PriorityQueue for storing open (unvisited) nodes, and put start node there.
        distance[start] = 0
        open_list = queue.PriorityQueue()
        open_list.put((0, start))

        # Loop until there are no unvisited nodes to process.
        while not open_list.empty():

            # Take next node from queue.
            # If it is end node, break from the loop.
            # If it is already processed, skip rest of the loop and take next node.
            # Nodes are ordered according to distance from start.
            _, x = open_list.get()
            if x == end:
                break
            if closed[x]:
                continue
            closed[x] = True

            # Go through neighbor nodes. If distance through the current node to neighbor node
            # is smaller than already exists for neighbor node, put neighbor node to PriorityQueue.
            for neighbor, dist in graph[x[0]][x[1]]:
                old = distance[neighbor]
                new = distance[x] + dist
                if new < old:
                    distance[neighbor] = new
                    previous[neighbor] = x
                    open_list.put((new, neighbor))

        # If list has been gone through and no end point found, return -1.
        if distance[end] == self.inf:
            return -1, [], []

        # Build lists for shortest route and visited nodes and return those.
        route = self.calculate_route(previous, start, end)
        visited = self.calculate_visited(closed)
        return distance[end], route, visited
