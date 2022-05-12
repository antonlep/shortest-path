import math
from algorithm import Algorithm


class JPS(Algorithm):
    """Class that calculates shortest distance with JPS algorithm.

    """

    def calculate_distance(self, graph, start, end):
        """Calculates shortest distance with JPS algorithm.

        Args:
            graph: 2D-list which includes neighboring nodes and their cost
            start: Tuple with x, y coordinates of start point
            end: Tuple with x, y coordinates of end point

        Returns:
            Tuple of shortest distance (float), shortest route (list) and visited nodes (list)
        """
        # Create initial data structures
        distance, previous, closed, open_list, first_node = self._initialize_data_structures(
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

            # Go through jump points starting from current node, calculate distances for them
            # and update data structures accordingly.
            distance, previous, open_list, first_node = self._go_through_jump_points_and_update(
                graph, distance, previous, x, start, end, open_list, first_node)

        # If list has been gone through and no end point found, return -1.
        if distance[end] == self.inf:
            return -1, [end, start], []

        # Build lists for shortest route and visited nodes and return those.
        route = self._calculate_route(previous, start, end)
        visited = self._calculate_visited(closed)
        return distance[end], route, visited

    def _prune(self, graph, parent, node):

        # Remove unnecessary neighbor nodes according to JPS algorithm.
        new_neighbors = []
        direction = (node[0] - parent[0], node[1] - parent[1])

        # If direction is bigger than one, reduce to one.
        if direction[0] >= 1:
            direction = (1, direction[1])
        elif direction[0] <= -1:
            direction = (-1, direction[1])
        if direction[1] >= 1:
            direction = (direction[0], 1)
        elif direction[1] <= -1:
            direction = (direction[0], -1)

        # Select new neighbors according to JPS algorithm.
        # Directions are checked separately to improve performance.
        if not self._is_blocked(graph, node, direction):
            new_neighbors.append(
                (node[0] + direction[0], node[1] + direction[1]))
        if direction[0] == 0:
            if (self._is_blocked(graph, node, (1, 0))
                    and not self._is_blocked(graph, node, (1, direction[1]))):
                new_neighbors.append(
                    (node[0] + 1, node[1] + direction[1]))
            if (self._is_blocked(graph, node, (-1, 0))
                    and not self._is_blocked(graph, node, (-1, direction[1]))):
                new_neighbors.append(
                    (node[0] - 1, node[1] + direction[1]))
        elif direction[1] == 0:
            if (self._is_blocked(graph, node, (0, 1))
                    and not self._is_blocked(graph, node, (direction[0], 1))):
                new_neighbors.append(
                    (node[0] + direction[0], node[1] + 1))
            if (self._is_blocked(graph, node, (0, -1))
                    and not self._is_blocked(graph, node, (direction[0], -1))):
                new_neighbors.append(
                    (node[0] + direction[0], node[1] - 1))
        else:
            if not self._is_blocked(graph, node, (0, direction[1])):
                new_neighbors.append((node[0], node[1] + direction[1]))
            if not self._is_blocked(graph, node, (direction[0], 0)):
                new_neighbors.append((node[0] + direction[0], node[1]))
            if direction == (-1, -1):
                if (self._is_blocked(graph, node, (0, 1))
                        and not self._is_blocked(graph, node, (-1, 1))):
                    new_neighbors.append((node[0] - 1, node[1] + 1))
                if (self._is_blocked(graph, node, (1, 0))
                        and not self._is_blocked(graph, node, (1, -1))):
                    new_neighbors.append((node[0] + 1, node[1] - 1))
            elif direction == (-1, 1):
                if (self._is_blocked(graph, node, (0, -1))
                        and not self._is_blocked(graph, node, (-1, -1))):
                    new_neighbors.append((node[0] - 1, node[1] - 1))
                if (self._is_blocked(graph, node, (1, 0))
                        and not self._is_blocked(graph, node, (1, 1))):
                    new_neighbors.append((node[0] + 1, node[1] + 1))
            elif direction == (1, 1):
                if (self._is_blocked(graph, node, (0, -1))
                        and not self._is_blocked(graph, node, (1, -1))):
                    new_neighbors.append((node[0] + 1, node[1] - 1))
                if (self._is_blocked(graph, node, (-1, 0))
                        and not self._is_blocked(graph, node, (-1, 1))):
                    new_neighbors.append((node[0] - 1, node[1] + 1))
            elif direction == (1, -1):
                if (self._is_blocked(graph, node, (-1, 0))
                        and not self._is_blocked(graph, node, (-1, -1))):
                    new_neighbors.append((node[0] - 1, node[1] - 1))
                if (self._is_blocked(graph, node, (0, 1))
                        and not self._is_blocked(graph, node, (1, 1))):
                    new_neighbors.append((node[0] + 1, node[1] + 1))
        return new_neighbors

    def _jump(self, graph, node, direction, start, goal):

        # Calculates if there is jump point in defined direction.
        # First select neighbor node.
        n = (node[0] + direction[0], node[1] + direction[1])

        # If current node is wall or outside of bounds, return None.
        if self._is_blocked(graph, node, direction):
            return None

        # If neighbor node is goal node or forced neighbor, return neighbor node.
        if n == goal:
            return n
        if self._forced_neighbor(graph, n, direction):
            return n

        # If direction is diagonal, start two jumps to vertical
        # and horizontal directions from neighbor node.
        # Return jump point if it is found.
        if direction[0] != 0 and direction[1] != 0:
            if self._jump(graph, n, (direction[0], 0), start, goal) is not None:
                return n
            if self._jump(graph, n, (0, direction[1]), start, goal) is not None:
                return n
        return self._jump(graph, n, direction, start, goal)

    def _is_blocked(self, graph, node, direction):

        # Checks if node neighbor in specified direction is wall or outside of bounds.
        new_pos = (node[0] + direction[0], node[1] + direction[1])

        # Check if position is outside of graph.
        if new_pos[0] < 0 or new_pos[0] >= len(graph[0]):
            return True
        if new_pos[1] < 0 or new_pos[1] >= len(graph):
            return True

        # Check if position is blocked by wall.
        if not graph[new_pos[0]][new_pos[1]]:
            return True
        return False

    def _forced_neighbor(self, graph, node, direction):

        # Checks if node has forced neighbors according to JPS algorithm definition.
        # Directions are checked separately to improve performance.
        if direction[0] == 0:
            if (self._is_blocked(graph, node, (1, 0))
                    and not self._is_blocked(graph, node, (1, direction[1]))):
                return True
            if (self._is_blocked(graph, node, (-1, 0))
                    and not self._is_blocked(graph, node, (-1, direction[1]))):
                return True
        elif direction[1] == 0:
            if (self._is_blocked(graph, node, (0, 1))
                    and not self._is_blocked(graph, node, (direction[0], 1))):
                return True
            if (self._is_blocked(graph, node, (0, -1))
                    and not self._is_blocked(graph, node, (direction[0], -1))):
                return True
        else:
            if direction == (-1, -1):
                if (self._is_blocked(graph, node, (0, 1))
                        and not self._is_blocked(graph, node, (-1, 1))):
                    return True
                if (self._is_blocked(graph, node, (1, 0))
                        and not self._is_blocked(graph, node, (1, -1))):
                    return True
            elif direction == (-1, 1):
                if (self._is_blocked(graph, node, (0, -1))
                        and not self._is_blocked(graph, node, (-1, -1))):
                    return True
                if (self._is_blocked(graph, node, (1, 0))
                        and not self._is_blocked(graph, node, (1, 1))):
                    return True
            elif direction == (1, 1):
                if (self._is_blocked(graph, node, (-1, 0))
                        and not self._is_blocked(graph, node, (-1, 1))):
                    return True
                if (self._is_blocked(graph, node, (0, -1))
                        and not self._is_blocked(graph, node, (1, -1))):
                    return True
            elif direction == (1, -1):
                if (self._is_blocked(graph, node, (0, 1))
                        and not self._is_blocked(graph, node, (1, 1))):
                    return True
                if (self._is_blocked(graph, node, (-1, 0))
                        and not self._is_blocked(graph, node, (-1, -1))):
                    return True
        return False

    def heuristic(self, node, end):
        """Heuristic calculation.

        Args:
            node: start node coordinates
            end: end node coordinates

        Returns:
            Euclidean distance between start and end points.
        """
        return math.sqrt((node[0]-end[0])**2+(node[1]-end[1])**2)
