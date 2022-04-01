import math
from PIL import Image


class MapImage:
    """Class that has operations for importing map data,
        creating graph and exporting result as picture file.

    Args:
        width: Input map width
        height: Input map height
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.mode = 'RGB'
        self.image = Image.new(self.mode, (self.width, self.height))
        self.data = []
        self.map = None

    def import_map(self, i_map):
        """Imports map file and converts it to image format and list.

        Args:
            map: Name of a map file.
        """
        self.map = i_map
        data = []
        with open(i_map, encoding="utf-8") as fil:
            for x, line in enumerate(fil):
                if x < 4:
                    continue
                x = x - 4
                row = []
                for y, symbol in enumerate(line):
                    if symbol == ".":
                        self.image.putpixel((y, x), (0, 0, 155))
                        row.append(symbol)
                    elif symbol == "@":
                        self.image.putpixel((y, x), (0, 255, 0))
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
        graph = {}
        moves_straight = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        moves_diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for i in range(n):
            for j in range(m):
                graph[(i, j)] = []
        for i in range(n):
            for j in range(m):
                pos = (i, j)
                if self.data[i][j] == ".":
                    for move in moves_straight:
                        new_pos = (i + move[0], j + move[1])
                        if 0 <= new_pos[0] < n and 0 <= new_pos[1] < m:
                            if self.data[new_pos[0]][new_pos[1]] == ".":
                                graph[pos].append(((new_pos), straight_cost))
                    for move in moves_diagonal:
                        new_pos = (i + move[0], j + move[1])
                        if 0 <= new_pos[0] < n and 0 <= new_pos[1] < m:
                            if self.data[new_pos[0]][new_pos[1]] == ".":
                                diag1 = (i, j + move[1])
                                diag2 = (i + move[0], j)
                                if (self.data[diag1[0]][diag1[1]] == "."
                                        and self.data[diag2[0]][diag2[1]] == "."):
                                    graph[pos].append(
                                        ((new_pos), diagonal_cost))
        return graph

    def add_route(self, route, color):
        """Adds nodes in a route to image file.

        Args:
            route: List of nodes.
            color: Color in RGB format.
        """
        for i in route:
            self.image.putpixel((i[0], i[1]), color)

    def save(self, size, name):
        """Saves image as png file.

        Args:
            size: Output image size.
            name: Output file name.
        """
        image = self.image.resize(size)
        image.save(name + '.png')
