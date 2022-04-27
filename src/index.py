from map_image import MapImage
from graph import Graph
from input_parser import InputParser
from dijkstra import Dijkstra
from jps import JPS
from a_star import AStar

OBSTACLE_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 50, 150)
VISITED_COLOR = (200, 50, 25)
ROUTE_COLOR = (0, 0, 0)
START_COLOR = (255, 255, 0)
END_COLOR = (0, 255, 0)
SCALE_FACTOR = 1


def select_algorithm(algorithm_name):
    if algorithm_name == "a_star":
        return AStar()
    elif algorithm_name == "dijkstra":
        return Dijkstra()
    elif algorithm_name == "jps":
        return JPS()
    return None


def main():
    input_parser = InputParser()
    benchmark, algorithm_name, image_map, start, end = input_parser.parse_input_args()
    algorithm = select_algorithm(algorithm_name)
    image = MapImage(OBSTACLE_COLOR, BACKGROUND_COLOR, VISITED_COLOR,
                     ROUTE_COLOR, START_COLOR, END_COLOR, SCALE_FACTOR,
                     "data/" + image_map + ".map")
    graph = Graph(image)
    if benchmark:
        algorithm.run_benchmark(graph, image.name)
    else:
        shortest_distance, route, visited, el_time = algorithm.calculate_distance_and_time(
            graph, start, end)
        print("Shortest distance: ", shortest_distance)
        print("Time used: ", el_time)
        print("Number of visited nodes/jump points: ", len(visited))
        image.save_images(algorithm, route, visited)
        image.show_image(algorithm)


if __name__ == "__main__":
    main()
