import queue
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
        if not graph:
            return -1, [], []
        n = len(graph)
        m = len(graph[0])

        # Check if start and end points are outside of graph.
        if (not graph or end[0] < 0 or end[0] >= m or end[1] < 0 or end[1] >= n
                or start[0] < 0 or start[0] >= m or start[1] < 0 or start[1] >= n):
            return -1, [], []

        # Create and initialize dictionary for distance (from start node) and closed (visited) nodes.
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
        f_cost = self.heuristic(start, end)
        open_list.put((f_cost, start))
        first_node = True

        # Loop until there are no unvisited nodes to process.
        while not open_list.empty():

            # Take next node from queue.
            # If it is end node, break from the loop.
            # If it is already processed, skip rest of the loop and take next node.
            # Nodes are ordered according to estimated distance from start to end.
            _, x = open_list.get()
            if x == end:
                break
            if closed[x]:
                continue
            closed[x] = True

            # Select node neighbors.
            neighbors = graph[x[0]][x[1]]
            successors = []

            # If node is start point, select all neighbor nodes.
            # Otherwise, select only neighbors that are
            # natural neighbors according to JPS algorithm.
            if first_node:
                natural_neighbors = [s[0] for s in neighbors]
                first_node = False
            else:
                natural_neighbors = self.prune(
                    graph, previous[x], x)

            # Go through neighbors and check if jump point exists in each direction.
            # If jump point is found, put it to the list.
            for neighbor in natural_neighbors:
                d = (neighbor[0] - x[0], neighbor[1] - x[1])
                n = self.jump(graph, x, d, start, end)
                if n is not None:
                    successors.append(n)

            # Go through found jump points. If distance through the current node to jump point
            # is smaller than already exists for jump point, calculate estimated distance
            # from start to end through that jump point and put to PriorityQueue.
            for successor in successors:
                old = distance[successor]
                new = distance[x] + self.heuristic(x, successor)
                if new < old:
                    distance[successor] = new
                    previous[successor] = x
                    f_cost = new + self.heuristic(successor, end)
                    open_list.put((f_cost, successor))

        # If list has been gone through and no end point found, return -1.
        if distance[end] == self.inf:
            return -1, [], []

        # Build lists for shortest route and visited nodes and return those.
        route = self.calculate_route(previous, start, end)
        visited = self.calculate_visited(closed)
        return distance[end], route, visited

    def prune(self, graph, parent, node):
        """Removes unnecessary neighbor nodes (according to JPS algorithm).

        Args:
            graph: 2D-list which includes neighboring nodes and their cost
            parent: Previous node
            node: Current node

        Returns:
            List of nodes, from which unneccessary nodes have been removed
        """
        new_neighbors = []
        d = (node[0] - parent[0], node[1] - parent[1])

        # If direction is bigger than one, reduce to one.
        if d[0] >= 1:
            d = (1, d[1])
        elif d[0] <= -1:
            d = (-1, d[1])
        if d[1] >= 1:
            d = (d[0], 1)
        elif d[1] <= -1:
            d = (d[0], -1)

        # Select new neighbors according to JPS algorithm.
        # Directions are checked separately to improve performance.
        if not self.is_blocked(graph, node, d):
            new_neighbors.append(
                (node[0] + d[0], node[1] + d[1]))
        if d[0] == 0:
            if (self.is_blocked(graph, node, (1, 0))
                    and not self.is_blocked(graph, node, (1, d[1]))):
                new_neighbors.append(
                    (node[0] + 1, node[1] + d[1]))
            if (self.is_blocked(graph, node, (-1, 0))
                    and not self.is_blocked(graph, node, (-1, d[1]))):
                new_neighbors.append(
                    (node[0] - 1, node[1] + d[1]))
        elif d[1] == 0:
            if (self.is_blocked(graph, node, (0, 1))
                    and not self.is_blocked(graph, node, (d[0], 1))):
                new_neighbors.append(
                    (node[0] + d[0], node[1] + 1))
            if (self.is_blocked(graph, node, (0, -1))
                    and not self.is_blocked(graph, node, (d[0], -1))):
                new_neighbors.append(
                    (node[0] + d[0], node[1] - 1))
        else:
            if not self.is_blocked(graph, node, (0, d[1])):
                new_neighbors.append((node[0], node[1] + d[1]))
            if not self.is_blocked(graph, node, (d[0], 0)):
                new_neighbors.append((node[0] + d[0], node[1]))
            if d == (-1, -1):
                if (self.is_blocked(graph, node, (0, 1))
                        and not self.is_blocked(graph, node, (-1, 1))):
                    new_neighbors.append((node[0] - 1, node[1] + 1))
                if (self.is_blocked(graph, node, (1, 0))
                        and not self.is_blocked(graph, node, (1, -1))):
                    new_neighbors.append((node[0] + 1, node[1] - 1))
            elif d == (-1, 1):
                if (self.is_blocked(graph, node, (0, -1))
                        and not self.is_blocked(graph, node, (-1, -1))):
                    new_neighbors.append((node[0] - 1, node[1] - 1))
                if (self.is_blocked(graph, node, (1, 0))
                        and not self.is_blocked(graph, node, (1, 1))):
                    new_neighbors.append((node[0] + 1, node[1] + 1))
            elif d == (1, 1):
                if (self.is_blocked(graph, node, (0, -1))
                        and not self.is_blocked(graph, node, (1, -1))):
                    new_neighbors.append((node[0] + 1, node[1] - 1))
                if (self.is_blocked(graph, node, (-1, 0))
                        and not self.is_blocked(graph, node, (-1, 1))):
                    new_neighbors.append((node[0] - 1, node[1] + 1))
            elif d == (1, -1):
                if (self.is_blocked(graph, node, (-1, 0))
                        and not self.is_blocked(graph, node, (-1, -1))):
                    new_neighbors.append((node[0] - 1, node[1] - 1))
                if (self.is_blocked(graph, node, (0, 1))
                        and not self.is_blocked(graph, node, (1, 1))):
                    new_neighbors.append((node[0] + 1, node[1] + 1))
        return new_neighbors

    def jump(self, graph, node, d, start, goal):
        """Calculates if there is jump point in defined direction.

        Args:
            graph: 2D-list which includes neighboring nodes and their cost
            node: Current node
            d: Move direction
            start: Tuple with x, y coordinates of start point
            goal: Tuple with x, y coordinates of end point

        Returns:
            Jump point node if it exists, otherwise None
        """
        # Select neighbor node.
        n = (node[0] + d[0], node[1] + d[1])

        # If current node is wall or outside of bounds, return None.
        if self.is_blocked(graph, node, d):
            return None

        # If neighbor node is goal node or forced neighbor, return neighbor node.
        if n == goal:
            return n
        if self.forced_neighbor(graph, n, d):
            return n

        # If direction is diagonal, start two jumps to vertical and horizontal directions from neighbor node.
        # Return jump point if it is found.
        if d[0] != 0 and d[1] != 0:
            if self.jump(graph, n, (d[0], 0), start, goal) is not None:
                return n
            if self.jump(graph, n, (0, d[1]), start, goal) is not None:
                return n

        return self.jump(graph, n, d, start, goal)

    def is_blocked(self, graph, node, d):
        """Checks if node neighbor in specified direction is wall or outside of bounds.

        Args:
            graph: 2D-list which includes neighboring nodes and their cost
            node: Current node
            d: Move direction

        Returns:
            True if blocked, False otherwise
        """
        new_pos = (node[0] + d[0], node[1] + d[1])

        # Check if position is outside of graph.
        if new_pos[0] < 0 or new_pos[0] >= len(graph[0]):
            return True
        if new_pos[1] < 0 or new_pos[1] >= len(graph):
            return True

        # Check if position is blocked by wall.
        if not graph[new_pos[0]][new_pos[1]]:
            return True
        return False

    def forced_neighbor(self, graph, node, d):
        """Checks if node has forced neighbors according to JPS algorithm definition.

        Args:
            graph: 2D-list which includes neighboring nodes and their cost
            node: Current node
            d: Move direction

        Returns:
            True if node has forced neighbors, False otherwise
        """
        # Each direction is checked separately to improve performance.
        if d == (0, 1):
            if (self.is_blocked(graph, node, (1, 0))
                    and not self.is_blocked(graph, node, (1, 1))):
                return True
            if (self.is_blocked(graph, node, (-1, 0))
                    and not self.is_blocked(graph, node, (-1, 1))):
                return True
        elif d == (0, -1):
            if (self.is_blocked(graph, node, (1, 0))
                    and not self.is_blocked(graph, node, (1, -1))):
                return True
            if (self.is_blocked(graph, node, (-1, 0))
                    and not self.is_blocked(graph, node, (-1, -1))):
                return True
        elif d == (1, 0):
            if (self.is_blocked(graph, node, (0, 1))
                    and not self.is_blocked(graph, node, (1, 1))):
                return True
            if (self.is_blocked(graph, node, (0, -1))
                    and not self.is_blocked(graph, node, (1, -1))):
                return True
        elif d == (-1, 0):
            if (self.is_blocked(graph, node, (0, 1))
                    and not self.is_blocked(graph, node, (1, 1))):
                return True
            if (self.is_blocked(graph, node, (0, -1))
                    and not self.is_blocked(graph, node, (1, -1))):
                return True
        elif d == (-1, -1):
            if (self.is_blocked(graph, node, (0, 1))
                    and not self.is_blocked(graph, node, (-1, 1))):
                return True
            if (self.is_blocked(graph, node, (1, 0))
                    and not self.is_blocked(graph, node, (1, -1))):
                return True
        elif d == (-1, 1):
            if (self.is_blocked(graph, node, (0, -1))
                    and not self.is_blocked(graph, node, (-1, -1))):
                return True
            if (self.is_blocked(graph, node, (1, 0))
                    and not self.is_blocked(graph, node, (1, 1))):
                return True
        elif d == (1, 1):
            if (self.is_blocked(graph, node, (-1, 0))
                    and not self.is_blocked(graph, node, (-1, 1))):
                return True
            if (self.is_blocked(graph, node, (0, -1))
                    and not self.is_blocked(graph, node, (1, -1))):
                return True
        elif d == (1, -1):
            if (self.is_blocked(graph, node, (0, 1))
                    and not self.is_blocked(graph, node, (1, 1))):
                return True
            if (self.is_blocked(graph, node, (-1, 0))
                    and not self.is_blocked(graph, node, (-1, -1))):
                return True
        return False
