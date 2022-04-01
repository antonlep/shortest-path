import sys
import time
from map_image import MapImage
from dijkstra import Dijkstra
from a_star import AStar


def main():
    algorithm = sys.argv[1]
    image_map = sys.argv[2]
    start = (int(sys.argv[3]), int(sys.argv[4]))
    end = (int(sys.argv[5]), int(sys.argv[6]))
    image = MapImage(256, 256)
    output_size = (512, 512)
    image.import_map("data/" + image_map + ".map")
    image.save(output_size, "data/" + image_map + "_original")
    graph = image.create_graph()
    # dijkstra = Dijkstra()
    # shortest_distance, route, visited = dijkstra.calculate_distance(
    #     graph, start, end)
    if algorithm == "a_star":
        alg = AStar()
    elif algorithm == "dijkstra":
        alg = Dijkstra()
    start_time = time.time()
    shortest_distance, route, visited = alg.calculate_distance(
        graph, start, end)
    end_time = time.time()
    print("Shortest distance: ", shortest_distance)
    print("Time used: ", end_time - start_time)
    image.add_route(visited, (100, 0, 0))
    image.add_route(route, (0, 0, 0))
    image.save(output_size, "data/" + image_map + "_route")

    diag = 1.4
    graph2 = {}
    graph2[(0, 0)] = [((1, 0), 1), ((0, 1), 1)]
    graph2[(1, 0)] = [((0, 0), 1), ((1, 0), diag),
                      ((2, 0), 1), ((2, 1), diag)]
    graph2[(2, 0)] = [((1, 0), 1), ((2, 1), 1)]
    graph2[(0, 1)] = []
    graph2[(1, 1)] = []
    graph2[(2, 1)] = []
    graph2[(0, 2)] = [((0, 1), 1), ((1, 2), 1)]
    graph2[(1, 2)] = [((0, 2), 1), ((0, 1), diag),
                      ((2, 2), 1), ((2, 1), diag)]
    graph2[(2, 2)] = [((2, 1), 1), ((1, 2), 1)]

    shortest_distance, route, visited = alg.calculate_distance(
        graph2, (0, 0), (2, 2))


if __name__ == "__main__":
    main()
