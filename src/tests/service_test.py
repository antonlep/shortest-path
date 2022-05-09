import unittest
from service import Service


class MockAlgorithm:

    def run_benchmark(self, a, b, c):
        return 1, 2

    def calculate_distance_and_time(self, a, b, c):
        return 1, 2, [1, 2], 4


class MockImage:
    def __init__(self, name):
        self.name = name

    def save_images(self, a, b, c):
        pass

    def show_image(self, a):
        pass


class MockGraph:
    pass


class TestService(unittest.TestCase):
    def test_benchmark(self):
        image = MockImage("test")
        algorithm = MockAlgorithm()
        graph = MockGraph()
        service = Service()
        cases, tot_time = service.run_benchmark(image, algorithm, graph)
        self.assertEqual(cases, 1)
        self.assertEqual(tot_time, 2)

    def test_calculate_distance(self):
        image = MockImage("test")
        algorithm = MockAlgorithm()
        graph = MockGraph()
        service = Service()
        start = (0, 0)
        end = (10, 10)
        dist, tot_time, visited = service.calculate_distance(
            graph, algorithm, image, start, end)
        self.assertEqual(dist, 1)
        self.assertEqual(tot_time, 4)
        self.assertEqual(visited, 2)

    def test_algorithm_a_star(self):
        service = Service()
        alg = service.select_algorithm("a_star")
        self.assertEqual(alg.__class__.__name__, "AStar")

    def test_algorithm_dijkstra(self):
        service = Service()
        alg = service.select_algorithm("dijkstra")
        self.assertEqual(alg.__class__.__name__, "Dijkstra")

    def test_algorithm_jps(self):
        service = Service()
        alg = service.select_algorithm("jps")
        self.assertEqual(alg.__class__.__name__, "JPS")

    def test_algorithm_none(self):
        service = Service()
        alg = service.select_algorithm("test")
        self.assertEqual(alg, None)
