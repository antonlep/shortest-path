import unittest
from distance import Distance


class TestDistance(unittest.TestCase):
    def test_default_behavior(self):
        dist = Distance()
        start = (0, 0)
        end = (1, 1)
        graph = {}
        self.assertEqual(dist.heuristic(start, end), None)
        self.assertEqual(dist.calculate_distance(graph, start, end), None)
