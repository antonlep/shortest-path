import unittest
import math
from algorithm import Algorithm
from graph import Graph


class MockGraph:
    def __init__(self, data):
        self.graph = data


class TestAlgorithm(unittest.TestCase):

    def setUp(self):
        diag = math.sqrt(2)
        self.graph = [[[]]*3 for _ in range(3)]
        self.graph[0][0] = [((1, 0), 1), ((0, 1), 1)]
        self.graph[1][0] = [((0, 0), 1), ((1, 0), diag),
                            ((2, 0), 1), ((2, 1), diag)]
        self.graph[2][0] = [((1, 0), 1), ((2, 1), 1)]
        self.graph[0][1] = [((0, 0), 1), ((1, 0), diag),
                            ((0, 2), 1), ((1, 2), diag)]
        self.graph[1][1] = []
        self.graph[2][1] = [((2, 0), 1), ((1, 0), diag),
                            ((2, 2), 1), ((1, 2), diag)]
        self.graph[0][2] = [((0, 1), 1), ((1, 2), 1)]
        self.graph[1][2] = [((0, 2), 1), ((0, 1), diag),
                            ((2, 2), 1), ((2, 1), diag)]
        self.graph[2][2] = [((2, 1), 1), ((1, 2), 1)]

    def test_select_algorithm(self):
        alg1 = Algorithm("dijkstra")
        alg2 = Algorithm("a_star")
        alg3 = Algorithm("jps")
        self.assertEqual("dijkstra", alg1.name)
        self.assertEqual("a_star", alg2.name)
        self.assertEqual("jps", alg3.name)

    def test_calculate_distance(self):
        alg = Algorithm("dijkstra")
        start = (0, 0)
        end = (2, 2)
        graph = MockGraph(self.graph)
        distance, route, visited, time = alg.calculate_distance(
            graph, start, end)
        self.assertAlmostEqual(distance, 2 + math.sqrt(2))
