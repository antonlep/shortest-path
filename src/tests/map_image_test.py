import unittest
from map_image import MapImage
from pathlib import Path
from jps import JPS

THIS_DIR = Path(__file__).parent


class MockAlgorithm:
    def __init__(self, name):
        self.name = name


class TestMapImage(unittest.TestCase):
    def setUp(self):
        simple_map = str(THIS_DIR / 'simple.map')
        empty_map = str(THIS_DIR / 'empty.map')
        self.simple_image = MapImage(
            (255, 0, 0), (0, 255, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), 1)
        self.empty_image = MapImage(
            (255, 0, 0), (0, 255, 0), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), 1)
        self.simple_image.read(simple_map)
        self.empty_image.read(empty_map)

    def test_import_map(self):
        self.assertEqual(self.simple_image.data, [[".", ".", "."], [
                         ".", "@", "."], [".", ".", "."]])

    def test_import_map_no_obstacles(self):
        self.assertEqual(self.empty_image.data, [[".", "."], [
                         ".", "."]])

    def test_add_visited(self):
        route = [(0, 1), (1, 1), (1, 2)]
        self.simple_image.add_route(route, "visited")
        self.assertEqual(self.simple_image.image.getpixel(
            (1, 1)), (1, 1, 1))
        self.assertNotEqual(
            self.simple_image.image.getpixel((0, 0)), (1, 1, 1))

    def test_add_route(self):
        route = [(0, 1), (1, 1), (1, 2)]
        self.simple_image.add_route(route, "route")
        self.assertEqual(self.simple_image.image.getpixel(
            (1, 1)), (2, 2, 2))
        self.assertNotEqual(
            self.simple_image.image.getpixel((0, 0)), (2, 2, 2))

    def test_add_start(self):
        route = [(0, 1), (1, 1), (1, 2)]
        self.simple_image.add_route(route, "start")
        self.assertEqual(self.simple_image.image.getpixel(
            (1, 1)), (3, 3, 3))
        self.assertNotEqual(
            self.simple_image.image.getpixel((0, 0)), (3, 3, 3))

    def test_add_end(self):
        route = [(0, 1), (1, 1), (1, 2)]
        self.simple_image.add_route(route, "end")
        self.assertEqual(self.simple_image.image.getpixel(
            (1, 1)), (4, 4, 4))
        self.assertNotEqual(
            self.simple_image.image.getpixel((0, 0)), (4, 4, 4))

    def test_save_images_dijkstra(self):
        route = [(0, 0), (0, 1), (0, 2)]
        visited = [(1, 0), (1, 1), (1, 2)]
        algorithm = MockAlgorithm("dijkstra")
        self.simple_image.save_images(algorithm, route, visited)
        self.assertEqual(self.simple_image.image.getpixel(
            (0, 1)), (2, 2, 2))
        self.assertEqual(self.simple_image.image.getpixel(
            (1, 0)), (1, 1, 1))
        self.assertEqual(self.simple_image.image.getpixel(
            (0, 0)), (4, 4, 4))
        self.assertEqual(self.simple_image.image.getpixel(
            (0, 2)), (3, 3, 3))

    def test_save_images_jps(self):
        route = [(0, 0), (0, 1), (0, 2)]
        visited = [(1, 0), (1, 1), (1, 2)]
        algorithm = JPS()
        self.simple_image.save_images(algorithm, route, visited)
        self.assertEqual(self.simple_image.image.getpixel(
            (0, 1)), (2, 2, 2))
        self.assertEqual(self.simple_image.image.getpixel(
            (1, 0)), (1, 1, 1))
        self.assertEqual(self.simple_image.image.getpixel(
            (0, 0)), (4, 4, 4))
        self.assertEqual(self.simple_image.image.getpixel(
            (0, 2)), (3, 3, 3))
