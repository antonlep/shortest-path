import time
import csv
from a_star import AStar
from dijkstra import Dijkstra
from jps import JPS


class Algorithm:
    def __init__(self, name):
        self.name = name
        self.algorithm = self.select_algorithm(name)

    def select_algorithm(self, algorithm_name):
        algorithms = {"a_star": AStar(), "dijkstra": Dijkstra(), "jps": JPS()}
        return algorithms[algorithm_name]

    def calculate_distance(self, graph, start, end):
        start_time = time.time()
        print(graph.graph)
        shortest_distance, route, visited = self.algorithm.calculate_distance(
            graph.graph, start, end)
        end_time = time.time()
        return shortest_distance, route, visited, end_time-start_time

    def run_benchmark(self, graph, image):
        with open(
                f"data/{image.name}_{self.name}_results.csv", "w", encoding="utf-8") as output_file:
            writer = csv.writer(output_file)
            with open(f"data/{image.name}.map.scen", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter='\t')
                next(reader)
                for line in reader:
                    shortest_distance, _, visited, el_time = self.calculate_distance(
                        graph.graph, (int(line[4]), int(line[5])), (int(line[6]), int(line[7])))
                    writer.writerow((shortest_distance, el_time, len(visited)))
