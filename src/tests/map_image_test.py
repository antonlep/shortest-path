import unittest
from unittest.mock import patch, mock_open
from map_image import MapImage
from pathlib import Path

THIS_DIR = Path(__file__).parent


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        my_data_path = THIS_DIR / 'simple.map'
        self.image = MapImage(3, 3)
        self.image.import_map(my_data_path)

    def test_import_map(self):
        self.assertEqual(self.image.data, [[".", ".", "."], [
                         ".", "@", "."], [".", ".", "."]])

    def test_create_graph(self):
        result = {(0, 0): [((0, 1), 1), ((1, 0), 1)], (0, 1): [((0, 0), 1), ((0, 2), 1), ((1, 0), 1.4142135623730951), ((1, 2), 1.4142135623730951)],
                  (0, 2): [((0, 1), 1), ((1, 2), 1)], (1, 0): [((0, 0), 1), ((2, 0), 1), ((0, 1), 1.4142135623730951), ((2, 1), 1.4142135623730951)],
                  (1, 1): [], (1, 2): [((0, 2), 1), ((2, 2), 1), ((0, 1), 1.4142135623730951), ((2, 1), 1.4142135623730951)],
                  (2, 0): [((1, 0), 1), ((2, 1), 1)], (2, 1): [((2, 0), 1), ((2, 2), 1), ((1, 0), 1.4142135623730951), ((1, 2), 1.4142135623730951)],
                  (2, 2): [((1, 2), 1), ((2, 1), 1)]}
        graph = self.image.create_graph()
        self.assertAlmostEqual(graph, result)

    def test_add_route(self):
        route = [(0, 1), (1, 1), (1, 2)]
        self.image.add_route(route, (100, 100, 100))
        self.assertEqual(self.image.im.getpixel((1, 1)), (100, 100, 100))
        self.assertNotEqual(self.image.im.getpixel((0, 0)), (100, 100, 100))
