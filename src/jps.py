import queue
import math
from distance import Distance


class JPS(Distance):
    """Class that calculates shortest distance with JPS algorithm.

    """

    def calculate_distance(self, graph, start, end):
        """Calculates shortest distance with JPS algorithm.

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
            neighbors = graph[x]
            successors = []
            if first_node:
                natural_neighbors = neighbors
                first_node = False
            else:
                natural_neighbors = self.prune(previous[x], x, neighbors)
            for neighbor, _ in natural_neighbors:
                direction = (neighbor[0] - x[0], neighbor[1] - x[1])
                n = self.jump(graph, x, direction, start, end)
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

    def prune(self, parent, node, neighbors):
        mask = []
        direction = (node[0] - parent[0], node[1] - parent[1])
        if direction[0] >= 1:
            direction = (1, direction[1])
        if direction[0] <= -1:
            direction = (-1, direction[1])
        if direction[1] >= 1:
            direction = (direction[0], 1)
        if direction[1] <= -1:
            direction = (direction[0], -1)
        mask.append((node[0] + direction[0], node[1] + direction[1]))
        if direction[0] == 0:
            if (node[0] + 1, node[1]) not in neighbors:
                mask.append((node[0] + 1, node[1] + direction[1]))
            if (node[0] - 1, node[1]) not in neighbors:
                mask.append((node[0] - 1, node[1] + direction[1]))
        elif direction[1] == 0:
            if (node[0], node[1] + 1) not in neighbors:
                mask.append((node[0] + direction[0], node[1] + 1))
            if (node[0], node[1] - 1) not in neighbors:
                mask.append((node[0] + direction[0], node[1] - 1))
        else:
            mask.append((node[0], node[1] + direction[1]))
            mask.append((node[0] + direction[0], node[1]))
            if direction == (-1, -1):
                if (node[0], node[1] + 1) not in neighbors:
                    mask.append((node[0] - 1, node[1] + 1))
                if (node[0] + 1, node[1]) not in neighbors:
                    mask.append((node[0] + 1, node[1] - 1))
            if direction == (-1, 1):
                if (node[0], node[1] - 1) not in neighbors:
                    mask.append((node[0] - 1, node[1] - 1))
                if (node[0] + 1, node[1]) not in neighbors:
                    mask.append((node[0] + 1, node[1] + 1))
            if direction == (1, 1):
                if (node[0] - 1, node[1]) not in neighbors:
                    mask.append((node[0] - 1, node[1] + 1))
                if (node[0], node[1] - 1) not in neighbors:
                    mask.append((node[0] + 1, node[1] - 1))
            if direction == (1, -1):
                if (node[0], node[1] + 1) not in neighbors:
                    mask.append((node[0] + 1, node[1] + 1))
                if (node[0] - 1, node[1]) not in neighbors:
                    mask.append((node[0] - 1, node[1] - 1))
        return [x for x in neighbors if x[0] in mask]

    def jump(self, graph, node, direction, start, goal):
        graph_size = math.sqrt(len(graph))
        n = (node[0] + direction[0], node[1] + direction[1])
        if n[0] < 0 or n[1] < 0 or n[0] >= graph_size or n[1] >= graph_size or not graph[n]:
            return None
        if n == goal:
            return n
        if self.forced_neighbor(n, direction, graph[n]):
            return n
        if direction[0] != 0 and direction[1] != 0:
            if self.jump(graph, n, (direction[0], 0), start, goal) is not None:
                return n
            if self.jump(graph, n, (0, direction[1]), start, goal) is not None:
                return n
        return self.jump(graph, n, direction, start, goal)

    def forced_neighbor(self, node, direction, neighbors):
        neighbors = [n[0] for n in neighbors]
        if direction[0] == 0:
            if ((node[0] + 1, node[1]) not in neighbors and (node[0] + 1, node[1] + direction[1]) in neighbors):
                return True
            if (node[0] - 1, node[1]) not in neighbors and (node[0] - 1, node[1] + direction[1]) in neighbors:
                return True
        elif direction[1] == 0:
            if (node[0], node[1] + 1) not in neighbors and (node[0] + direction[0], node[1] + 1) in neighbors:
                return True
            if (node[0], node[1] - 1) not in neighbors and (node[0] + direction[0], node[1] - 1) in neighbors:
                return True
        else:
            if direction == (-1, -1):
                if (node[0], node[1] + 1) not in neighbors and (node[0] - 1, node[1] + 1) in neighbors:
                    return True
                if (node[0] + 1, node[1]) not in neighbors and (node[0] + 1, node[1] - 1) in neighbors:
                    return True
            if direction == (-1, 1):
                if (node[0], node[1] - 1) not in neighbors and (node[0] - 1, node[1] - 1) in neighbors:
                    return True
                if (node[0] + 1, node[1]) not in neighbors and (node[0] + 1, node[1] + 1) in neighbors:
                    return True
            if direction == (1, 1):
                if (node[0] - 1, node[1]) not in neighbors and (node[0] - 1, node[1] + 1) in neighbors:
                    return True
                if (node[0], node[1] - 1) not in neighbors and (node[0] + 1, node[1] - 1) in neighbors:
                    return True
            if direction == (1, -1):
                if (node[0], node[1] + 1) not in neighbors and (node[0] + 1, node[1] + 1) in neighbors:
                    return True
                if (node[0] - 1, node[1]) not in neighbors and (node[0] - 1, node[1] - 1) in neighbors:
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
