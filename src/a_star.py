import math
from algorithm import Algorithm


class AStar(Algorithm):
    """Class that calculates shortest distance with A* algorithm.

    """

    def calculate_distance(self, graph, start, end):
        """Calculates shortest distance with A* algorithm.

        Args:
            graph: 2D-list which includes neighboring nodes and their cost
            start: Tuple with x, y coordinates of start point
            end: Tuple with x, y coordinates of end point

        Returns:
            Tuple of shortest distance (float), shortest route (list) and visited nodes (list)
        """
        # Create initial data structures
        distance, previous, closed, open_list, _ = self._initialize_data_structures(
            graph, start, end)

        if not distance:
            return -1, [end, start], []

        # Loop until there are no unvisited nodes to process.
        # Nodes are ordered according to estimated distance from start to end throug current node.
        while not open_list.empty():

            # Take next node from queue.
            # If it is end node, break from the loop.
            # If it is already processed, skip rest of the loop and take next node.
            x, closed, end_node, processed_node = self._take_next_node(
                open_list, closed, end)
            if end_node:
                break
            if processed_node:
                continue

            # Go through node neighbors, calculate distances for them
            # and update data structures accordingly.
            distance, previous, open_list = self._go_through_node_neighbors_and_update(
                graph, distance, previous, x, end, open_list)

        # If list has been gone through and no end point found, return -1.
        if distance[end] == self.inf:
            return -1, [end, start], []

        # Build lists for shortest route and visited nodes and return those.
        route = self._calculate_route(previous, start, end)
        visited = self._calculate_visited(closed)
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
