import unittest
import pytest
import sys
from unittest.mock import patch
from input_parser import InputParser


class TestInputParser(unittest.TestCase):

    def test_no_args(self):
        input_parser = InputParser()
        testargs = []
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            with patch.object(sys, 'argv', testargs):
                benchmark, algorithm_name, image_map, start, end = input_parser.parse_input_args()
        self.assertEqual(pytest_wrapped_e.type, SystemExit)

    def test_only_benchmark(self):
        input_parser = InputParser()
        testargs = ["prog", "benchmark"]
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            with patch.object(sys, 'argv', testargs):
                benchmark, algorithm_name, image_map, start, end = input_parser.parse_input_args()
        self.assertEqual(pytest_wrapped_e.type, SystemExit)

    def test_wrong_args(self):
        input_parser = InputParser()
        testargs = ["prog", "dijkstra", "berlin"]
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            with patch.object(sys, 'argv', testargs):
                benchmark, algorithm_name, image_map, start, end = input_parser.parse_input_args()
        self.assertEqual(pytest_wrapped_e.type, SystemExit)

    def test_benchmark(self):
        input_parser = InputParser()
        testargs = ["prog", "benchmark", "dijkstra", "berlin"]
        with patch.object(sys, 'argv', testargs):
            benchmark, algorithm_name, image_map, start, end = input_parser.parse_input_args()
        self.assertEqual(algorithm_name, "dijkstra")
        self.assertEqual(image_map, "berlin")

    def test_correct_args(self):
        input_parser = InputParser()
        testargs = ["prog", "dijkstra", "berlin", "1", "2", "3", "4"]
        with patch.object(sys, 'argv', testargs):
            benchmark, algorithm_name, image_map, start, end = input_parser.parse_input_args()
        self.assertEqual(algorithm_name, "dijkstra")
        self.assertEqual(image_map, "berlin")
        self.assertEqual(start, (1, 2))
        self.assertEqual(end, (3, 4))
