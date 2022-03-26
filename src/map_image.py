from PIL import Image
import math


class MapImage:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.mode = 'RGB'
        self.im = Image.new(self.mode, (self.width, self.height))
        self.data = []

    def import_map(self, map):
        self.map = map
        data = []
        with open(map) as f:
            for x, line in enumerate(f):
                if x < 4:
                    continue
                x = x - 4
                row = []
                for y, symbol in enumerate(line):
                    if symbol == ".":
                        self.im.putpixel((x, y), (0, 0, 155))
                        row.append(symbol)
                    elif symbol == "@":
                        self.im.putpixel((x, y), (0, 255, 0))
                        row.append(symbol)
                data.append(row)
        self.data = data

    def create_graph(self):
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
                                graph[pos].append(((new_pos), diagonal_cost))
        return graph

    def add_route(self, route, color):
        for i in route:
            self.im.putpixel((i[0], i[1]), color)

    def save(self, size, name):
        im = self.im.resize(size)
        im.save(name + '.png')
