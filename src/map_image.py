from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from jps import JPS


class MapImage:
    """Class that has operations for importing map data,
        creating graph and exporting result as picture file.

    Args:
        fg_color: Obstacle color in RGB format
        bg_color: Background color in RGB format
        visited_color: Visited nodes color in RGB format
        route_color: Route color in RGB format
        start_color: Start point color in RGB format
        end_color: End point color in RGB format
        scale_factor: For scaling up output image
    """

    def __init__(self, fg_color, bg_color, visited_color,
                 route_color, start_color, end_color, scale_factor):
        self.mode = 'RGB'
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.visited_color = visited_color
        self.route_color = route_color
        self.start_color = start_color
        self.end_color = end_color
        self.scale_factor = scale_factor
        self.image, self.data, self.size = None, None, None
        self.name = ""

    def read(self, i_map):
        """Imports map file and converts it to image format and to list.

        Args:
            i_map: Name of a map file.
        """
        with open(i_map, encoding="utf-8") as fil:
            size = len(fil.readlines())
        size -= 4

        image = Image.new(self.mode, (size, size))

        data = []
        with open(i_map, encoding="utf-8") as fil:
            for x, line in enumerate(fil):
                if x < 4:
                    continue
                x = x - 4
                row = []
                for y, symbol in enumerate(line):
                    if symbol == ".":
                        image.putpixel((y, x), self.bg_color)
                        row.append(symbol)
                    elif symbol == "@":
                        image.putpixel((y, x), self.fg_color)
                        row.append(symbol)
                data.append(row)

        data = list(map(list, zip(*data)))
        self.image = image
        self.data = data
        self.size = size
        self.name = i_map.replace('/', '.').split('.')[1]

    def add_route(self, route, input_type):
        """Adds nodes in a route to image file.

        Args:
            route: List of nodes.
            input_type: Node type ("route" | "visited" | "start" | "end")
        """
        if input_type == "route":
            for i in route:
                self.image.putpixel((i[0], i[1]), self.route_color)
        elif input_type == "visited":
            for i in route:
                self.image.putpixel((i[0], i[1]), self.visited_color)
        elif input_type == "start":
            for i in route:
                self.image.putpixel((i[0], i[1]), self.start_color)
        elif input_type == "end":
            for i in route:
                self.image.putpixel((i[0], i[1]), self.end_color)

    def save(self, name):
        """Saves image as png file.

        Args:
            name: Output file name.
        """
        image = self.image.resize(
            (self.scale_factor*self.size, self.scale_factor*self.size), resample=0)
        image.save(name + '.png')

    def save_images(self, algorithm, route, visited):
        """Adds route, start point and end points to image and saves it.

        Args:
            algorithm: Algorithm object.
            route: List of nodes in shortest path.
            visited: List of visited nodes.
        """
        self.save("data/" + self.name + "_original")
        if isinstance(algorithm, JPS):
            self.add_route(route, "route")
            self.add_route(visited, "visited")
        else:
            self.add_route(visited, "visited")
            self.add_route(route, "route")
        self.add_route([route[-1]], "start")
        self.add_route([route[0]], "end")
        self.save("data/" + self.name + f"_{type(algorithm).__name__}")

    def show_image(self, algorithm):
        """Display image in separate window.
        """
        img = mpimg.imread("data/" + self.name +
                           f"_{type(algorithm).__name__}.png")
        _ = plt.imshow(img)
        plt.show()
