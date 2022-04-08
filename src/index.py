import sys
import time
from map_image import MapImage
from dijkstra import Dijkstra
from a_star import AStar
from jps import JPS

OBSTACLE_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 255)
VISITED_COLOR = (100, 0, 0)
ROUTE_COLOR = (0, 0, 0)
SCALE_FACTOR = 20


def main():
    algorithm = sys.argv[1]
    image_map = sys.argv[2]
    start = (int(sys.argv[3]), int(sys.argv[4]))
    end = (int(sys.argv[5]), int(sys.argv[6]))
    image = MapImage(OBSTACLE_COLOR, BACKGROUND_COLOR)
    image.import_map("data/" + image_map + ".map")
    image.save("data/" + image_map + "_original", SCALE_FACTOR)
    graph = image.create_graph()
    if algorithm == "a_star":
        alg = AStar()
    elif algorithm == "dijkstra":
        alg = Dijkstra()
    elif algorithm == "jps":
        alg = JPS()
    start_time = time.time()
    shortest_distance, route, visited = alg.calculate_distance(
        graph, start, end)
    end_time = time.time()
    print("Shortest distance: ", shortest_distance)
    print("Time used: ", end_time - start_time)
    if algorithm == "jps":
        image.add_route(route, ROUTE_COLOR)
        image.add_route(visited, VISITED_COLOR)
    else:
        image.add_route(visited, VISITED_COLOR)
        image.add_route(route, ROUTE_COLOR)
    image.save("data/" + image_map + "_route", SCALE_FACTOR)


if __name__ == "__main__":
    main()
