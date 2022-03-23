from PIL import Image

class MapImage:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.mode = 'RGB'
        self.im = Image.new(self.mode, (self.width, self.height))

    def import_map(self, map):
        self.map = map
        with open(map) as f:
            for x, line in enumerate(f):
                if x < 4:
                    continue
                x = x - 4
                for y, symbol in enumerate(line):
                    if symbol == ".":
                        self.im.putpixel((x, y), (0, 0, 155))
                    elif symbol == "@":
                        self.im.putpixel((x, y), (0, 255, 0))

    def resize(self, width, height):
        self.im = self.im.resize((width, height))

    def save(self):
        name = self.map.split()[0]
        self.im.save(name + '.png')
