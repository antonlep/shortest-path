import unittest
import math
from map_image import MapImage
from pathlib import Path

THIS_DIR = Path(__file__).parent


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        simple_map = THIS_DIR / 'simple.map'
        empty_map = THIS_DIR / 'empty.map'
        self.simple_image = MapImage((255, 0, 0), (0, 255, 0))
        self.simple_image.import_map(simple_map)
        self.empty_image = MapImage((255, 0, 0), (0, 255, 0))
        self.empty_image.import_map(empty_map)

    def test_import_map(self):
        self.assertEqual(self.simple_image.data, [[".", ".", "."], [
                         ".", "@", "."], [".", ".", "."]])

    def test_import_map_no_obstacles(self):
        self.assertEqual(self.empty_image.data, [[".", "."], [
                         ".", "."]])

    def test_create_simple_graph(self):
        diag = math.sqrt(2)
        result = {(0, 0): [((0, 1), 1), ((1, 0), 1)], (0, 1): [((0, 0), 1), ((0, 2), 1), ((1, 0), diag), ((1, 2), diag)],
                  (0, 2): [((0, 1), 1), ((1, 2), 1)], (1, 0): [((0, 0), 1), ((2, 0), 1), ((0, 1), diag), ((2, 1), diag)],
                  (1, 1): [], (1, 2): [((0, 2), 1), ((2, 2), 1), ((0, 1), diag), ((2, 1), diag)], (2, 0): [((1, 0), 1), ((2, 1), 1)],
                  (2, 1): [((2, 0), 1), ((2, 2), 1), ((1, 0), diag), ((1, 2), diag)], (2, 2): [((1, 2), 1), ((2, 1), 1)]}
        graph = self.simple_image.create_graph()
        self.assertEqual(graph, result)

    def test_create_empty_graph(self):
        diag = math.sqrt(2)
        result = {(0, 0): [((0, 1), 1), ((1, 0), 1), ((1, 1), diag)],
                  (0, 1): [((0, 0), 1), ((1, 1), 1), ((1, 0), diag)],
                  (1, 0): [((0, 0), 1), ((1, 1), 1), ((0, 1), diag)],
                  (1, 1): [((0, 1), 1), ((1, 0), 1), ((0, 0), diag)]}
        graph = self.empty_image.create_graph()
        self.assertEqual(graph, result)

    def test_add_route(self):
        route = [(0, 1), (1, 1), (1, 2)]
        self.simple_image.add_route(route, (100, 100, 100))
        self.assertEqual(self.simple_image.image.getpixel(
            (1, 1)), (100, 100, 100))
        self.assertNotEqual(
            self.simple_image.image.getpixel((0, 0)), (100, 100, 100))
