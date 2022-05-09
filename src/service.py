from a_star import AStar
from jps import JPS
from dijkstra import Dijkstra


class Service:
    """ Class that includes methods for executing calculation cases.
    """

    def run_benchmark(self, image, algorithm, graph):
        """Calculates benchmark case with several calculation points. 
            Prints results to command line and to .csv file.

        Args:
            image: MapImage object
            algorithm: Calculation algorithm as Algorithm object
            graph: Case to be calculated as Graph object
        """
        image_map = image.name
        input_file = f"data/{image_map}.map.scen"
        output_file = f"data/{image_map}_{algorithm.__class__.__name__}_results.csv"
        number_of_cases, total_time = algorithm.run_benchmark(
            graph, input_file, output_file)
        return number_of_cases, total_time

    def calculate_distance(self, graph, algorithm, image, start, end):
        """Calculates shortest path in a graph between two points.

        Args:
            graph: Case to be calculated as Graph object
            algorithm: Calculation algorithm as Algorithm object
            image: MapImage object
            start: Tuple with x, y coordinates of start point
            end: Tuple with x, y coordinates of start point
        """
        shortest_distance, route, visited, el_time = algorithm.calculate_distance_and_time(
            graph, start, end)
        image.save_images(algorithm, route, visited)
        image.show_image(algorithm)
        return shortest_distance, el_time, len(visited)

    def select_algorithm(self, algorithm_name):
        """Creates Algorithm object according to input string.

        Args:
            algorithm_name: a_star | dijkstra | jps

        Returns:
            Algorithm object
        """
        if algorithm_name == "a_star":
            return AStar()
        elif algorithm_name == "dijkstra":
            return Dijkstra()
        elif algorithm_name == "jps":
            return JPS()
        return None
