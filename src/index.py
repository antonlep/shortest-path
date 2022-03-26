from map_image import MapImage
from dijkstra import Dijkstra
import sys

def main():
    map = sys.argv[1]
    start = (int(sys.argv[2]), int(sys.argv[3]))
    end = (int(sys.argv[4]), int(sys.argv[5]))
    image = MapImage(256, 256)
    output_size = (512, 512)
    image.import_map("data/" + map + ".map")
    image.save(output_size, "data/" + map + "_original")
    graph = image.create_graph()
    dijkstra = Dijkstra()
    shortest_distance, route, visited = dijkstra.calculate_distance(graph, start, end)
    print("shortest distance: ", shortest_distance)
    image.add_route(visited, (100,0,0))
    image.add_route(route, (0,0,0))
    image.save(output_size, "data/" + map + "_route")

if __name__ == "__main__":
    main()
