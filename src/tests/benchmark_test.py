import unittest
import random
from map_image import MapImage
from pathlib import Path
from dijkstra import Dijkstra
from a_star import AStar
from jps import JPS
from graph import Graph

THIS_DIR = Path(__file__).parent


class MockAlgorithm:
    def __init__(self, name):
        self.name = name


class TestBenchmark(unittest.TestCase):
    def setUp(self):
        test_map = str(THIS_DIR / 'Berlin_0_256.map')
        test_image = MapImage(
            (255, 0, 0), (0, 255, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), 1)
        test_image.read(test_map)
        self.graph = Graph(test_image)

    def test_benchmark(self):
        dijkstra = Dijkstra()
        a_star = AStar()
        jps = JPS()
        for i in range(20):
            start = (random.randint(0, 255), random.randint(0, 255))
            end = (random.randint(0, 255), random.randint(0, 255))
            d_distance, d_route, d_visited = dijkstra.calculate_distance(
                self.graph.graph, start, end)
            a_distance, a_route, a_visited = a_star.calculate_distance(
                self.graph.graph, start, end)
            j_distance, j_route, j_visited = jps.calculate_distance(
                self.graph.graph, start, end)
            self.assertAlmostEqual(d_distance, a_distance)
            self.assertAlmostEqual(d_distance, j_distance)
            self.assertGreaterEqual(len(d_visited), len(a_visited))
            self.assertGreaterEqual(len(a_visited), len(j_visited))
