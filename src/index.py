from map_image import MapImage
from algorithm import Algorithm
from graph import Graph
from input_parser import InputParser

OBSTACLE_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 50, 150)
VISITED_COLOR = (200, 50, 25)
ROUTE_COLOR = (0, 0, 0)
START_COLOR = (255, 255, 0)
END_COLOR = (0, 255, 0)
SCALE_FACTOR = 1


def main():
    input_parser = InputParser()
    benchmark, algorithm_name, image_map, start, end = input_parser.parse_input_args()
    algorithm = Algorithm(algorithm_name)
    image = MapImage(OBSTACLE_COLOR, BACKGROUND_COLOR, VISITED_COLOR,
                     ROUTE_COLOR, START_COLOR, END_COLOR, SCALE_FACTOR,
                     "data/" + image_map + ".map")
    graph = Graph(image)
    if benchmark:
        algorithm.run_benchmark(graph, image)
    else:
        shortest_distance, route, visited, el_time = algorithm.calculate_distance(
            graph, start, end)
        print("Shortest distance: ", shortest_distance)
        print("Time used: ", el_time)
        print("Number of visited nodes/jump points: ", len(visited))
        image.save_images(algorithm, route, visited)


if __name__ == "__main__":
    main()
