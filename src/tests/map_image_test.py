import unittest
from map_image import MapImage
from pathlib import Path

THIS_DIR = Path(__file__).parent


class TestMapImage(unittest.TestCase):
    def setUp(self):
        simple_map = str(THIS_DIR / 'simple.map')
        empty_map = str(THIS_DIR / 'empty.map')
        self.simple_image = MapImage(
            (255, 0, 0), (0, 255, 0), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), 1, simple_map)
        self.empty_image = MapImage(
            (255, 0, 0), (0, 255, 0), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), 1, empty_map)

    def test_import_map(self):
        self.assertEqual(self.simple_image.data, [[".", ".", "."], [
                         ".", "@", "."], [".", ".", "."]])

    def test_import_map_no_obstacles(self):
        self.assertEqual(self.empty_image.data, [[".", "."], [
                         ".", "."]])

    def test_add_route(self):
        route = [(0, 1), (1, 1), (1, 2)]
        self.simple_image.add_route(route, "visited")
        self.assertEqual(self.simple_image.image.getpixel(
            (1, 1)), (1, 1, 1))
        self.assertNotEqual(
            self.simple_image.image.getpixel((0, 0)), (1, 1, 1))
