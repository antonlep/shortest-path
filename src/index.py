from map_image import MapImage
from dijkstra import Dijkstra

def main():
    image = MapImage(256, 256)
    image_size = (512, 512)
    image.import_map('data/Berlin_0_256.map')
    image.save(image_size, "data/original")
    data = image.data
    dijkstra = Dijkstra()
    graph = dijkstra.create_graph(data)
    start = (9, 25)
    end = (245, 251)
    route, shortest_distance = dijkstra.calculate_distance(graph, start, end)
    print("shortest distance: ", shortest_distance)
    image.add_route(route)
    image.save(image_size, "data/route")

if __name__ == "__main__":
    main()
