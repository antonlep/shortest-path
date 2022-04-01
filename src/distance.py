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
            if value:
                visited.append(key)
        return visited

    @abstractmethod
    def calculate_distance(self, graph, start, end):
        pass

    def heuristic(self, node, end):
        pass
