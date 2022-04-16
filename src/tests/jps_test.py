import unittest
import math
from jps import JPS


class TestJPS(unittest.TestCase):
    def setUp(self):
        diag = math.sqrt(2)
        self.graph1 = [[[]]*3 for _ in range(3)]
        self.graph1[0][0] = [((1, 0), 1), ((0, 1), 1)]
        self.graph1[1][0] = [((0, 0), 1), ((1, 0), diag),
                             ((2, 0), 1), ((2, 1), diag)]
        self.graph1[2][0] = [((1, 0), 1), ((2, 1), 1)]
        self.graph1[0][1] = [((0, 0), 1), ((1, 0), diag),
                             ((0, 2), 1), ((1, 2), diag)]
        self.graph1[1][1] = []
        self.graph1[2][1] = [((2, 0), 1), ((1, 0), diag),
                             ((2, 2), 1), ((1, 2), diag)]
        self.graph1[0][2] = [((0, 1), 1), ((1, 2), 1)]
        self.graph1[1][2] = [((0, 2), 1), ((0, 1), diag),
                             ((2, 2), 1), ((2, 1), diag)]
        self.graph1[2][2] = [((2, 1), 1), ((1, 2), 1)]

        self.graph2 = [[[]]*3 for _ in range(3)]
        self.graph2[0][0] = [((1, 0), 1), ((0, 1), 1)]
        self.graph2[1][0] = [((0, 0), 1), ((1, 0), diag),
                             ((2, 0), 1), ((2, 1), diag)]
        self.graph2[2][0] = [((1, 0), 1), ((2, 1), 1)]
        self.graph2[0][1] = []
        self.graph2[1][1] = []
        self.graph2[2][1] = []
        self.graph2[0][2] = [((0, 1), 1), ((1, 2), 1)]
        self.graph2[1][2] = [((0, 2), 1), ((0, 1), diag),
                             ((2, 2), 1), ((2, 1), diag)]
        self.graph2[2][2] = [((2, 1), 1), ((1, 2), 1)]

        self.empty_graph = []

    def test_empty_graph(self):
        alg = JPS()
        start = (0, 0)
        end = (2, 2)
        distance, route, visited = alg.calculate_distance(
            self.empty_graph, start, end)
        self.assertEqual(distance, -1)
        self.assertEqual(route, [])
        self.assertEqual(visited, [])

    def test_calculate_distance_case1(self):
        alg = JPS()
        start = (0, 0)
        end = (2, 2)
        distance, route, visited = alg.calculate_distance(
            self.graph1, start, end)
        self.assertAlmostEqual(distance, 2 + math.sqrt(2))

    def test_calculate_route_case1(self):
        alg = JPS()
        start = (0, 0)
        end = (2, 2)
        distance, route, visited = alg.calculate_distance(
            self.graph1, start, end)
        route.sort()
        self.assertEqual(route, [(0, 0), (0, 1), (1, 2), (2, 2)])

    def test_calculate_visited_case1(self):
        alg = JPS()
        start = (0, 0)
        end = (2, 2)
        distance, route, visited = alg.calculate_distance(
            self.graph1, start, end)
        visited.sort()
        self.assertEqual(
            visited,  [(0, 0), (0, 1), (1, 0), (1, 2), (2, 1)])

    def test_calculate_distance_case2(self):
        alg = JPS()
        start = (0, 0)
        end = (2, 2)
        distance, route, visited = alg.calculate_distance(
            self.graph2, start, end)
        self.assertEqual(distance, -1)

    def test_start_not_in_graph(self):
        alg = JPS()
        start = (5, 5)
        end = (2, 2)
        distance, route, visited = alg.calculate_distance(
            self.graph1, start, end)
        self.assertEqual(distance, -1)
        self.assertEqual(route, [])
        self.assertEqual(visited, [])

    def test_end_not_in_graph(self):
        alg = JPS()
        start = (0, 0)
        end = (5, 5)
        distance, route, visited = alg.calculate_distance(
            self.graph1, start, end)
        self.assertEqual(distance, -1)
        self.assertEqual(route, [])
        self.assertEqual(visited, [])

    def test_heuristic(self):
        alg = JPS()
        start = (0, 0)
        end = (4, 6)
        result = alg.heuristic(start, end)
        self.assertEqual(result, math.sqrt(4**2 + 6**2))

    def test_prune1(self):
        alg = JPS()
        parent = (2, 0)
        node = (0, 0)
        new_neighbors = alg.prune(self.graph1, parent, node)
        self.assertEqual(new_neighbors, [])

    def test_prune2(self):
        alg = JPS()
        parent = (0, 2)
        node = (0, 0)
        new_neighbors = alg.prune(self.graph1, parent, node)
        self.assertEqual(new_neighbors, [])

    def test_prune3(self):
        alg = JPS()
        parent = (2, 0)
        node = (2, 1)
        new_neighbors = alg.prune(self.graph1, parent, node)
        self.assertEqual(new_neighbors, [(2, 2), (1, 2)])

    def test_prune4(self):
        alg = JPS()
        parent = (0, 2)
        node = (1, 2)
        new_neighbors = alg.prune(self.graph1, parent, node)
        self.assertEqual(new_neighbors, [(2, 2), (2, 1)])

    def test_prune5(self):
        alg = JPS()
        parent = (1, 2)
        node = (0, 1)
        new_neighbors = alg.prune(self.graph1, parent, node)
        self.assertEqual(new_neighbors, [(0, 0), (1, 0)])

    def test_prune6(self):
        alg = JPS()
        parent = (0, 1)
        node = (1, 0)
        new_neighbors = alg.prune(self.graph1, parent, node)
        self.assertEqual(new_neighbors, [(2, 0), (2, 1)])

    def test_prune7(self):
        alg = JPS()
        parent = (2, 1)
        node = (1, 0)
        new_neighbors = alg.prune(self.graph1, parent, node)
        self.assertEqual(new_neighbors, [(0, 0), (0, 1)])

    def test_prune8(self):
        alg = JPS()
        parent = (2, 1)
        node = (1, 2)
        new_neighbors = alg.prune(self.graph1, parent, node)
        self.assertEqual(new_neighbors, [(0, 2), (0, 1)])

    def test_forced_neighbor1(self):
        alg = JPS()
        node = (2, 1)
        direction = (0, -1)
        forced = alg.forced_neighbor(self.graph1, node, direction)
        self.assertEqual(forced, True)

    def test_forced_neighbor2(self):
        alg = JPS()
        node = (2, 1)
        direction = (0, -1)
        forced = alg.forced_neighbor(self.graph1, node, direction)
        self.assertEqual(forced, True)

    def test_forced_neighbor3(self):
        alg = JPS()
        node = (1, 2)
        direction = (1, 0)
        forced = alg.forced_neighbor(self.graph1, node, direction)
        self.assertEqual(forced, True)
