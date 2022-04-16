import math
from PIL import Image


class MapImage:
    """Class that has operations for importing map data,
        creating graph and exporting result as picture file.

    Args:
        fg_color: Obstacle color in RGB format
        bg_color: Background color in RGB format
    """

    def __init__(self, fg_color, bg_color):
        self.mode = 'RGB'
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.size = 0
        self.image = None
        self.data = []

    def import_map(self, i_map):
        """Imports map file and converts it to image format and to list.

        Args:
            i_map: Name of a map file.
        """
        with open(i_map, encoding="utf-8") as fil:
            self.size = len(fil.readlines())
        self.size -= 4

        self.image = Image.new(self.mode, (self.size, self.size))

        data = []
        with open(i_map, encoding="utf-8") as fil:
            for x, line in enumerate(fil):
                if x < 4:
                    continue
                x = x - 4
                row = []
                for y, symbol in enumerate(line):
                    if symbol == ".":
                        self.image.putpixel((y, x), self.bg_color)
                        row.append(symbol)
                    elif symbol == "@":
                        self.image.putpixel((y, x), self.fg_color)
                        row.append(symbol)
                data.append(row)

        self.data = list(map(list, zip(*data)))

    def create_graph(self):
        """Converts image file to graph.

        Returns:
            Graph as dictionary which includes neighboring nodes and their cost
            {(x,y): [((x2,y2), 1)]}
        """
        straight_cost = 1
        diagonal_cost = math.sqrt(2)
        n = len(self.data)
        m = len(self.data[0])
        graph = [[[]]*m for _ in range(n)]
        moves_straight = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        moves_diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for i in range(n):
            for j in range(m):
                neighbors = []
                if self.data[i][j] == ".":
                    for move in moves_straight:
                        new_pos = (i + move[0], j + move[1])
                        if 0 <= new_pos[0] < n and 0 <= new_pos[1] < m:
                            if self.data[new_pos[0]][new_pos[1]] == ".":
                                neighbors.append(((new_pos), straight_cost))
                    for move in moves_diagonal:
                        new_pos = (i + move[0], j + move[1])
                        if 0 <= new_pos[0] < n and 0 <= new_pos[1] < m:
                            if self.data[new_pos[0]][new_pos[1]] == ".":
                                neighbors.append(((new_pos), diagonal_cost))
                graph[i][j] = neighbors
        return graph

    def add_route(self, route, color):
        """Adds nodes in a route to image file.

        Args:
            route: List of nodes.
            color: Color in RGB format.
        """
        for i in route:
            self.image.putpixel((i[0], i[1]), color)

    def save(self, name, scale=1):
        """Saves image as png file.

        Args:
            scale: Output image scaling size.
            name: Output file name.
        """
        image = self.image.resize(
            (scale*self.size, scale*self.size), resample=0)
        image.save(name + '.png')
