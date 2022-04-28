import time
import csv
import math
from abc import abstractmethod


class Algorithm:
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

    def run_benchmark(self, graph, image_name):
        """Calculates benchmark case.

        Args:
            graph: Graph object to be calculated.
            image_name: Name of image to be calculated.
        """
        total_time = 0
        number_of_cases = 0
        with open(
            f"data/{image_name}_{type(self).__name__}_results.csv",
                "w", encoding="utf-8") as output_file:
            writer = csv.writer(output_file)
            with open(f"data/{image_name}.map.scen", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter='\t')
                next(reader)
                for line in reader:
                    shortest_distance, _, visited, el_time = self.calculate_distance_and_time(
                        graph, (int(line[4]), int(line[5])), (int(line[6]), int(line[7])))
                    writer.writerow((shortest_distance, el_time, len(visited)))
                    total_time += el_time
                    number_of_cases += 1
        print("Number of cases: ", number_of_cases)
        print("Calculation time: ", total_time)

    @abstractmethod
    def calculate_distance(self, graph, start, end):
        pass

    def heuristic(self, node, end):
        """Heuristic calculation.

        Args:
            node: start node coordinates
            end: end node coordinates

        Returns:
            Euclidean distance between start and end points.
        """
        return math.sqrt((node[0]-end[0])**2+(node[1]-end[1])**2)
