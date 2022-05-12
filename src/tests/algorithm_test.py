import unittest
import math
from algorithm import Algorithm
from pathlib import Path

THIS_DIR = Path(__file__).parent


class MockGraph:
    def __init__(self, data):
        self.graph = data


class MockDijkstra(Algorithm):
    pass


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

    def test_default_behavior(self):
        dist = Algorithm()
        start = (0, 0)
        end = (1, 1)
        graph = {}
        self.assertEqual(dist.calculate_distance(
            graph, start, end), (None, [], []))

    def test_calculate_route(self):
        dist = Algorithm()
        start = (0, 0)
        end = (1, 1)
        previous = {(1, 1): (3, 3), (3, 3): (0, 0)}
        route = dist._calculate_route(previous, start, end)
        self.assertEqual(
            route, [(1, 1), (2, 2), (3, 3), (2, 2), (1, 1), (0, 0)])

    def test_calculate_default_distance(self):
        graph = MockGraph(self.graph)
        alg = MockDijkstra()
        start = (0, 0)
        end = (1, 1)
        dist, route, visited, tim = alg.calculate_distance_and_time(
            graph, start, end)
        self.assertEqual(dist, None)

    def test_benchmark(self):
        graph = MockGraph(self.graph)
        alg = MockDijkstra()
        infile = str(THIS_DIR / 'simple.map.scen')
        outfile = str(THIS_DIR / 'simple.csv')
        cases, el_time = alg.run_benchmark(graph, infile, outfile)
        self.assertEqual(cases, 2)
