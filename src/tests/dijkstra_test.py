import unittest
import math
from dijkstra import Dijkstra


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        diag = math.sqrt(2)
        self.graph = {}
        self.graph[(0, 0)] = [((1, 0), 1), ((0, 1), 1)]
        self.graph[(1, 0)] = [((0, 0), 1), ((1, 0), diag),
                              ((2, 0), 1), ((2, 1), diag)]
        self.graph[(2, 0)] = [((1, 0), 1), ((2, 1), 1)]
        self.graph[(0, 1)] = [((0, 0), 1), ((1, 0), diag),
                              ((0, 2), 1), ((1, 2), diag)]
        self.graph[(1, 1)] = []
        self.graph[(2, 1)] = [((2, 0), 1), ((1, 0), diag),
                              ((2, 2), 1), ((1, 2), diag)]
        self.graph[(0, 2)] = [((0, 1), 1), ((1, 2), 1)]
        self.graph[(1, 2)] = [((0, 2), 1), ((0, 1), diag),
                              ((2, 2), 1), ((2, 1), diag)]
        self.graph[(2, 2)] = [((2, 1), 1), ((1, 2), 1)]

    def test_calculate_distance_case1(self):
        dijkstra = Dijkstra()
        start = (0, 0)
        end = (2, 2)
        distance, route, visited = dijkstra.calculate_distance(
            self.graph, start, end)
        self.assertAlmostEqual(distance, 2 + math.sqrt(2))

    def test_calculate_route_case1(self):
        dijkstra = Dijkstra()
        start = (0, 0)
        end = (2, 2)
        distance, route, visited = dijkstra.calculate_distance(
            self.graph, start, end)
        route.sort()
        self.assertEqual(route, [(0, 0), (0, 1), (1, 2), (2, 2)])

    def test_calculate_visited_case1(self):
        dijkstra = Dijkstra()
        start = (0, 0)
        end = (2, 2)
        distance, route, visited = dijkstra.calculate_distance(
            self.graph, start, end)
        visited.sort()
        self.assertEqual(
            visited, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)])
