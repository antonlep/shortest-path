import unittest
import math
from graph import Graph


class MockImage:
    def __init__(self, data):
        self.data = data


class TestGraph(unittest.TestCase):

    def test_create_simple_graph(self):
        diag = math.sqrt(2)

        map = ["...", ".@.", "..."]

        result = [[[((0, 1), 1), ((1, 0), 1)],
                   [((0, 0), 1), ((0, 2), 1), ((1, 0), diag), ((1, 2), diag)],
                   [((0, 1), 1), ((1, 2), 1)]],
                  [[((0, 0), 1), ((2, 0), 1), ((0, 1), diag), ((2, 1), diag)], [],
                   [((0, 2), 1), ((2, 2), 1), ((0, 1), diag), ((2, 1), diag)]],
                  [[((1, 0), 1), ((2, 1), 1)], [((2, 0), 1), ((2, 2), 1), ((1, 0), diag), ((1, 2), diag)],
                   [((1, 2), 1), ((2, 1), 1)]]]
        img = MockImage(map)
        graph = Graph(img)
        self.assertEqual(graph.graph, result)

    def test_create_empty_graph(self):
        diag = math.sqrt(2)

        map = ["..", ".."]

        result = [[[((0, 1), 1), ((1, 0), 1), ((1, 1), diag)], [((0, 0), 1), ((1, 1), 1), ((1, 0), diag)]],
                  [[((0, 0), 1), ((1, 1), 1), ((0, 1), diag)], [((0, 1), 1), ((1, 0), 1), ((0, 0), diag)]]]
        img = MockImage(map)
        graph = Graph(img)
        self.assertEqual(graph.graph, result)
