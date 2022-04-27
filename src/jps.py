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
        if (not graph or end[0] < 0 or end[0] >= m or end[1] < 0 or end[1] >= n
                or start[0] < 0 or start[0] >= m or start[1] < 0 or start[1] >= n):
            return -1, [], []
        distance = {}
        previous = {}
        closed = {}
        for i in range(m):
            for j in range(n):
                distance[(i, j)] = self.inf
                closed[(i, j)] = False
        distance[start] = 0
        open_list = queue.PriorityQueue()
        f_cost = self.heuristic(start, end)
        open_list.put((f_cost, start))
        first_node = True
        while not open_list.empty():
            _, x = open_list.get()
            if x == end:
                break
            if closed[x]:
                continue
            closed[x] = True
            neighbors = graph[x[0]][x[1]]
            successors = []
            if first_node:
                natural_neighbors = [s[0] for s in neighbors]
                first_node = False
            else:
                natural_neighbors = self.prune(
                    graph, previous[x], x)
            for neighbor in natural_neighbors:
                d = (neighbor[0] - x[0], neighbor[1] - x[1])
                n = self.jump(graph, x, d, start, end)
                if n is not None:
                    successors.append(n)
            for successor in successors:
                old = distance[successor]
                new = distance[x] + self.heuristic(x, successor)
                if new < old:
                    distance[successor] = new
                    previous[successor] = x
                    f_cost = new + self.heuristic(successor, end)
                    open_list.put((f_cost, successor))
        if distance[end] == self.inf:
            return -1, [], []
        route = self.calculate_route(previous, start, end)
        visited = self.calculate_visited(closed)
        return distance[end], route, visited

    def prune(self, graph, parent, node):
        """Removes unnecessary neighbor nodes.

        Args:
            graph: 2D-list which includes neighboring nodes and their cost
            parent: Previous node
            node: Current node

        Returns:
            List of nodes, from which unneccessary nodes have been removed
        """
        new_neighbors = []
        d = (node[0] - parent[0], node[1] - parent[1])
        if d[0] >= 1:
            d = (1, d[1])
        elif d[0] <= -1:
            d = (-1, d[1])
        if d[1] >= 1:
            d = (d[0], 1)
        elif d[1] <= -1:
            d = (d[0], -1)
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
            if ((not self.is_blocked(graph, node, (0, d[1]))
                    or not self.is_blocked(graph, node, (d[0], 0)))
                    and not self.is_blocked(graph, node, d)):
                new_neighbors.append(
                    (node[0]+d[0], node[1] + d[1]))
            if (self.is_blocked(graph, node, (-d[0], 0))
                    and not self.is_blocked(graph, node, (0, d[1]))):
                new_neighbors.append(
                    (node[0] - d[0], node[1] + d[1]))
            if (self.is_blocked(graph, node, (0, -d[1]))
                    and not self.is_blocked(graph, node, (d[0], 0))):
                new_neighbors.append(
                    (node[0] + d[0], node[1] - d[1]))
        return new_neighbors

    def jump(self, graph, node, d, start, goal):
        """Calculates if there is jump point in defined d.

        Args:
            graph: 2D-list which includes neighboring nodes and their cost
            node: Current node
            d: Move d
            start: Tuple with x, y coordinates of start point
            goal: Tuple with x, y coordinates of end point

        Returns:
            Jump point node if it exists, otherwise None
        """
        n = (node[0] + d[0], node[1] + d[1])
        if self.is_blocked(graph, node, d):
            return None
        if n == goal:
            return n
        if self.forced_neighbor(graph, n, d):
            return n
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
        if new_pos[0] < 0 or new_pos[0] >= len(graph[0]):
            return True
        if new_pos[1] < 0 or new_pos[1] >= len(graph):
            return True
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
        if d[0] == 0:
            if (self.is_blocked(graph, node, (1, 0))
                    and not self.is_blocked(graph, node, (1, d[1]))):
                return True
            if (self.is_blocked(graph, node, (-1, 0))
                    and not self.is_blocked(graph, node, (-1, d[1]))):
                return True
        elif d[1] == 0:
            if (self.is_blocked(graph, node, (0, 1))
                    and not self.is_blocked(graph, node, (d[0], 1))):
                return True
            if (self.is_blocked(graph, node, (0, -1))
                    and not self.is_blocked(graph, node, (d[0], -1))):
                return True
        else:
            if (not self.is_blocked(graph, node, (-d[0], d[1]))
                and self.is_blocked(graph, node, (-d[0], 0))
                or not self.is_blocked(graph, node, (d[0], -d[1]))
                    and self.is_blocked(graph, node, (0, -d[1]))):
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
