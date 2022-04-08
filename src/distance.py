from abc import abstractmethod


class Distance:
    """Template class that includes basic methods for route calculation.
        Methods that have to be implemented in subclasses are calculate_distance()
        and possibly heuristic().
    """

    def __init__(self):
        self.inf = 1e99

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
            prev = previous[u]
            direction = (prev[0] - u[0], prev[1] - u[1])
            if direction[0] >= 1:
                direction = (1, direction[1])
            elif direction[0] <= -1:
                direction = (-1, direction[1])
            if direction[1] >= 1:
                direction = (direction[0], 1)
            elif direction[1] <= -1:
                direction = (direction[0], -1)
            v = u
            while v != prev:
                v = (v[0] + direction[0], v[1] + direction[1])
                route.append(v)
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
            if value:
                visited.append(key)
        return visited

    @abstractmethod
    def calculate_distance(self, graph, start, end):
        pass

    def heuristic(self, node, end):
        pass
