import sys
import time
import csv
from map_image import MapImage
from dijkstra import Dijkstra
from a_star import AStar
from jps import JPS

OBSTACLE_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 50, 150)
VISITED_COLOR = (200, 50, 25)
ROUTE_COLOR = (0, 0, 0)
START_COLOR = (255, 255, 0)
END_COLOR = (0, 255, 0)
SCALE_FACTOR = 1


def parse_input_args():
    benchmark = False
    start = None
    end = None
    if sys.argv[1] == "benchmark":
        benchmark = True
        algorithm = sys.argv[2]
        image_map = sys.argv[3]
    else:
        algorithm = sys.argv[1]
        image_map = sys.argv[2]
        start = (int(sys.argv[3]), int(sys.argv[4]))
        end = (int(sys.argv[5]), int(sys.argv[6]))
    return benchmark, algorithm, image_map, start, end


def save_images(algorithm, route, image, image_map, visited):
    image.save("data/" + image_map + "_original", SCALE_FACTOR)
    if algorithm == "jps":
        image.add_route(route, ROUTE_COLOR)
        image.add_route(visited, VISITED_COLOR)
    else:
        image.add_route(visited, VISITED_COLOR)
        image.add_route(route, ROUTE_COLOR)
    image.add_route([route[-1]], START_COLOR)
    image.add_route([route[0]], END_COLOR)
    image.save("data/" + image_map + f"_{algorithm}", SCALE_FACTOR)


def main():
    algorithms = {"a_star": AStar(), "dijkstra": Dijkstra(), "jps": JPS()}
    benchmark, algorithm, image_map, start, end = parse_input_args()
    alg = algorithms[algorithm]
    image = MapImage(OBSTACLE_COLOR, BACKGROUND_COLOR)
    image.import_map("data/" + image_map + ".map")
    graph = image.create_graph()
    if benchmark:
        output_file = open(f"data/{image_map}_{algorithm}_results.csv", "w")
        writer = csv.writer(output_file)
        with open(f"data/{image_map}.map.scen") as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader)
            for line in reader:
                start_time = time.time()
                shortest_distance, route, visited = alg.calculate_distance(
                    graph, (int(line[4]), int(line[5])), (int(line[6]), int(line[7])))
                end_time = time.time()
                writer.writerow((shortest_distance, end_time -
                                start_time, len(visited)))
        output_file.close()
    else:
        start_time = time.time()
        shortest_distance, route, visited = alg.calculate_distance(
            graph, start, end)
        end_time = time.time()
        print("Shortest distance: ", shortest_distance)
        print("Time used: ", end_time - start_time)
        print("Number of visited nodes/jump points: ", len(visited))
        save_images(algorithm, route, image, image_map, visited)


if __name__ == "__main__":
    main()
