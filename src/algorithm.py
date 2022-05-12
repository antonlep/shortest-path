import time
import csv
import queue
from abc import abstractmethod


class Algorithm:
    def __init__(self):
        self.inf = 1e99

    def _initialize_data_structures(self, graph, start, end):

        # Create PriorityQueue for storing open (unvisited) nodes
        open_list = queue.PriorityQueue()

        # Create dictionary for distance (from start node)
        # and closed (visited) nodes.
        distance = {}
        previous = {}
        closed = {}
        first_node = True

        if not graph:
            return distance, previous, closed, open_list, first_node

        n = len(graph)
        m = len(graph[0])

        # Check if start and end points are outside of graph.
        if (not graph or end[0] < 0 or end[0] >= m or end[1] < 0 or end[1] >= n
                or start[0] < 0 or start[0] >= m or start[1] < 0 or start[1] >= n):
            return distance, previous, closed, open_list, first_node

        # Initialize dictionaries to default value.
        for i in range(m):
            for j in range(n):
                distance[(i, j)] = self.inf
                closed[(i, j)] = False

        # Put start node to queue.
        distance[start] = 0
        f_cost = self.heuristic(start, end)
        open_list.put((f_cost, start))
        first_node = True

        return distance, previous, closed, open_list, first_node

    def _take_next_node(self, open_list, closed, end):

        # Take next node from queue and check if it is end node or already processed.
        _, x = open_list.get()
        if x == end:
            return x, closed, True, False
        if closed[x]:
            return x, closed, False, True
        closed[x] = True

        return x, closed, False, False

    def _go_through_node_neighbors_and_update(
            self, graph, distance, previous, x, end, open_list):

        # Go through neighbor nodes. If distance through the current node to neighbor node
        # is smaller than already exists for neighbor node, put neighbor node to PriorityQueue.
        for neighbor, dist in graph[x[0]][x[1]]:
            old = distance[neighbor]
            new = distance[x] + dist
            if new < old:
                distance[neighbor] = new
                previous[neighbor] = x
                f_cost = new + self.heuristic(neighbor, end)
                open_list.put((f_cost, neighbor))
        return distance, previous, open_list

    def _go_through_jump_points_and_update(
            self, graph, distance, previous, x, start, end, open_list, first_node):

        # Go through all directions from current node and check if jump points exist.
        # First select node neighbors.
        neighbors = graph[x[0]][x[1]]
        successors = []

        # If node is start point, select all neighbor nodes.
        # Otherwise, select only neighbors that are
        # natural neighbors according to JPS algorithm.
        if first_node:
            natural_neighbors = [s[0] for s in neighbors]
            first_node = False
        else:
            natural_neighbors = self._prune(
                graph, previous[x], x)

        # Go through neighbors and check if jump point exists in each direction.
        # If jump point is found, put it to the list.
        for neighbor in natural_neighbors:
            direction = (neighbor[0] - x[0], neighbor[1] - x[1])
            n = self._jump(graph, x, direction, start, end)
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

        return distance, previous, open_list, first_node

    def _calculate_route(self, previous, start, end):

        # Calculate route from start to end using previous node dictionary.
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

    def _calculate_visited(self, ready):

        # Transform visited node dictionary to a list of visited nodes.
        visited = []
        for key, value in ready.items():
            if value:
                visited.append(key)
        return visited

    def calculate_distance_and_time(self, graph, start, end):
        """Calculates distance from start to end.

        Args:
            graph: 2D-list which includes neighboring nodes and their cost
            start: Tuple with x, y coordinates of start point
            end: Tuple with x, y coordinates of end point

        Returns:
            Tuple of shortest distance (float), shortest route (list),
            visited nodes (list) and time used (float)
        """
        start_time = time.time()
        shortest_distance, route, visited = self.calculate_distance(
            graph.graph, start, end)
        end_time = time.time()
        return shortest_distance, route, visited, end_time-start_time

    def run_benchmark(self, graph, input_file, out_file):
        """Calculates benchmark case.

        Args:
            graph: Graph object to be calculated.
            input_file: Name of scenario file to be calculated.
            out_file: Name of output text file.
        """
        total_time = 0
        number_of_cases = 0
        with open(out_file, "w", encoding="utf-8") as output_file:
            writer = csv.writer(output_file)
            with open(input_file, encoding="utf-8") as file:
                reader = csv.reader(file, delimiter='\t')
                next(reader)
                for line in reader:
                    shortest_distance, _, visited, el_time = self.calculate_distance_and_time(
                        graph, (int(line[4]), int(line[5])), (int(line[6]), int(line[7])))
                    writer.writerow((shortest_distance, el_time, len(visited)))
                    total_time += el_time
                    number_of_cases += 1
        return number_of_cases, total_time

    @abstractmethod
    def calculate_distance(self, graph, start, end):
        return None, [], []

    @abstractmethod
    def heuristic(self, node, end):
        return 0

    def _prune(self, graph, parent, node):
        return graph, parent, node

    def _jump(self, graph, node, direction, start, goal):
        return graph, node, direction, start, goal
