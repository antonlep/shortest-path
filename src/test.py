import sys
import time
import math
from map_image import MapImage
from dijkstra import Dijkstra
from a_star import AStar
from jps import JPS

OBSTACLE_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 255)
VISITED_COLOR = (100, 0, 0)
ROUTE_COLOR = (0, 0, 0)
SCALE_FACTOR = 2


OBSTACLE_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 255)
VISITED_COLOR = (100, 0, 0)
ROUTE_COLOR = (0, 0, 0)
SCALE_FACTOR = 2


def main():
    alg = JPS()
    neighbors = [((101, 199), 1), ((99, 198), 1.4142135623730951), ((
        99, 200), 1.4142135623730951), ((101, 198), 1.4142135623730951)]

    parent = (99, 198)
    node = (100, 199)
    print(alg.prune(parent, node, neighbors))

    # shortest_distance, route, visited = alg.calculate_distance(
    #     graph, start, end)
    # end_time = time.time()
    # print("Shortest distance: ", shortest_distance)
    # print("Time used: ", end_time - start_time)
    # image.add_route(visited, VISITED_COLOR)
    # image.add_route(route, ROUTE_COLOR)
    # image.save("data/" + image_map + "_route", SCALE_FACTOR)


if __name__ == "__main__":
    main()
