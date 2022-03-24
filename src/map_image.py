from PIL import Image

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

    def add_route(self, route):
        for i in route:
            self.im.putpixel((i[0], i[1]), (255, 0, 0))

    def save(self, size, name):
        im = self.im.resize(size)
        im.save(name + '.png')
