import unittest
import math
from dijkstra import Dijkstra


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        diag = math.sqrt(2)
        self.graph1 = {}
        self.graph1[(0, 0)] = [((1, 0), 1), ((0, 1), 1)]
        self.graph1[(1, 0)] = [((0, 0), 1), ((1, 0), diag),
                               ((2, 0), 1), ((2, 1), diag)]
        self.graph1[(2, 0)] = [((1, 0), 1), ((2, 1), 1)]
        self.graph1[(0, 1)] = [((0, 0), 1), ((1, 0), diag),
                               ((0, 2), 1), ((1, 2), diag)]
        self.graph1[(1, 1)] = []
        self.graph1[(2, 1)] = [((2, 0), 1), ((1, 0), diag),
                               ((2, 2), 1), ((1, 2), diag)]
        self.graph1[(0, 2)] = [((0, 1), 1), ((1, 2), 1)]
        self.graph1[(1, 2)] = [((0, 2), 1), ((0, 1), diag),
                               ((2, 2), 1), ((2, 1), diag)]
        self.graph1[(2, 2)] = [((2, 1), 1), ((1, 2), 1)]

        self.graph2 = {}
        self.graph2[(0, 0)] = [((1, 0), 1), ((0, 1), 1)]
        self.graph2[(1, 0)] = [((0, 0), 1), ((1, 0), diag),
                               ((2, 0), 1), ((2, 1), diag)]
        self.graph2[(2, 0)] = [((1, 0), 1), ((2, 1), 1)]
        self.graph2[(0, 1)] = []
        self.graph2[(1, 1)] = []
        self.graph2[(2, 1)] = []
        self.graph2[(0, 2)] = [((0, 1), 1), ((1, 2), 1)]
        self.graph2[(1, 2)] = [((0, 2), 1), ((0, 1), diag),
                               ((2, 2), 1), ((2, 1), diag)]
        self.graph2[(2, 2)] = [((2, 1), 1), ((1, 2), 1)]

    def test_calculate_distance_case1(self):
        dijkstra = Dijkstra()
        start = (0, 0)
        end = (2, 2)
        distance, route, visited = dijkstra.calculate_distance(
            self.graph1, start, end)
        self.assertAlmostEqual(distance, 2 + math.sqrt(2))

    def test_calculate_route_case1(self):
        dijkstra = Dijkstra()
        start = (0, 0)
        end = (2, 2)
        distance, route, visited = dijkstra.calculate_distance(
            self.graph1, start, end)
        route.sort()
        self.assertEqual(route, [(0, 0), (0, 1), (1, 2), (2, 2)])

    def test_calculate_visited_case1(self):
        dijkstra = Dijkstra()
        start = (0, 0)
        end = (2, 2)
        distance, route, visited = dijkstra.calculate_distance(
            self.graph1, start, end)
        visited.sort()
        self.assertEqual(
            visited, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)])

    def test_calculate_distance_case2(self):
        dijkstra = Dijkstra()
        start = (0, 0)
        end = (2, 2)
        distance, route, visited = dijkstra.calculate_distance(
            self.graph2, start, end)
        self.assertEqual(distance, -1)
