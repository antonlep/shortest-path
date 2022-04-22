import time
import csv
from a_star import AStar
from dijkstra import Dijkstra
from jps import JPS
from graph import Graph


class Algorithm:
    """Class that defines the distance calculation algorithm to be used.

    Args:
        name: Algorithm name [dijkstra | a_star | jps]
    """

    def __init__(self, name):
        self.name = name
        self.algorithm = self.__select_algorithm(name)

    def __select_algorithm(self, algorithm_name):
        algorithms = {"a_star": AStar(), "dijkstra": Dijkstra(), "jps": JPS()}
        return algorithms[algorithm_name]

    def calculate_distance(self, graph, start, end):
        """Calculates distance from start to end.

        Args:
            graph: 2D-list which includes neighboring nodes and their cost
            start: Tuple with x, y coordinates of start point
            end: Tuple with x, y coordinates of end point

        Returns:
            Tuple of shortest distance (float), shortest route (list), visited nodes (list) and time used (float)
        """
        start_time = time.time()
        shortest_distance, route, visited = self.algorithm.calculate_distance(
            graph.graph, start, end)
        end_time = time.time()
        return shortest_distance, route, visited, end_time-start_time

    def run_benchmark(self, graph, image_name):
        """Calculates benchmark case.

        Args:
            graph: Graph object to be calculated.
            image_name: Name of image to be calculated.
        """
        with open(
                f"data/{image_name}_{self.name}_results.csv", "w", encoding="utf-8") as output_file:
            writer = csv.writer(output_file)
            with open(f"data/{image_name}.map.scen", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter='\t')
                next(reader)
                for line in reader:
                    shortest_distance, _, visited, el_time = self.calculate_distance(
                        graph.graph, (int(line[4]), int(line[5])), (int(line[6]), int(line[7])))
                    writer.writerow((shortest_distance, el_time, len(visited)))
