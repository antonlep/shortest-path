from os import listdir
from os.path import isfile, join
from dijkstra import Dijkstra
from a_star import AStar
from jps import JPS
from graph import Graph


class TextUI:
    """Command line user interface.

    Args:
        service: Service object
        image: MapImage object
    """

    def __init__(self, service, image):
        self.commands = {
            "c": "calculate shortest distance",
            "b": "run benchmark",
            "q": "quit"
        }
        self.algorithms = {
            "d": Dijkstra(),
            "a": AStar(),
            "j": JPS()
        }
        self.maps = self._read_files(".map")
        self.scenarios = self._read_files(".map.scen")
        self.service = service
        self.image = image

    def start(self):
        """Launches the UI.
        """
        print("Shortest path calculation")
        while True:
            self._print_instruction()
            command = self._read("command: ")
            if not command in self.commands:
                print("incorrect command")
                self._print_instruction()
                continue
            if command == "c":
                self._calculate_distance()
            elif command == "b":
                self._run_benchmark()
            elif command == "q":
                break

    def _read(self, instruction):
        command = input(instruction)
        return command

    def _print_instruction(self):
        for k, v in self.commands.items():
            print(k, ":", v)

    def _calculate_distance(self):
        print("--------------------")
        algorithm = self._select_algorithm()
        print("--------------------")
        s_map = self._select_map()
        print("--------------------")
        startx = self._input_coord("start point x-coord: ")
        print("--------------------")
        starty = self._input_coord("start point y-coord: ")
        print("--------------------")
        endx = self._input_coord("end point x-coord: ")
        print("--------------------")
        endy = self._input_coord("end point y-coord: ")
        print("--------------------")
        self.image.read("data/" + s_map + ".map")
        graph = Graph(self.image)
        try:
            shortest_distance, el_time, visited = self.service.calculate_distance(
                graph, algorithm, self.image, (startx, starty), (endx, endy))
        except Exception as excep:
            print(excep)
        print("Shortest distance: ", shortest_distance)
        print("Time used: ", el_time)
        print("Number of visited nodes/jump points: ", visited)
        print("--------------------")

    def _select_algorithm(self):
        while True:
            print("Select algorithm:")
            _ = [print(k, ":", v.__class__.__name__)
                 for k, v in self.algorithms.items()]
            algorithm = input("algorithm: ")
            if algorithm not in self.algorithms:
                print("incorrecct algorithm")
                continue
            return self.algorithms[algorithm]

    def _select_map(self):
        while True:
            print("Select map:")
            _ = [print(k, ":", v) for k, v in self.maps.items()]
            s_map = input("map: ")
            if s_map not in self.maps:
                print("incorrect map")
                continue
            return self.maps[s_map]

    def _select_scenario(self):
        while True:
            print("Select scenario")
            _ = [print(k, ":", v) for k, v in self.scenarios.items()]
            scenario = input("scenario: ")
            if scenario not in self.scenarios:
                print("incorrect scenario")
                continue
            return self.scenarios[scenario]

    def _input_coord(self, name):
        while True:
            coord = input(name)
            try:
                coord = int(coord)
                return coord
            except:
                print("incorrect value")
                continue

    def _run_benchmark(self):
        print("--------------------")
        algorithm = self._select_algorithm()
        print("--------------------")
        scenario = self._select_scenario()
        print("--------------------")
        self.image.read("data/" + scenario + ".map")
        graph = Graph(self.image)
        try:
            number_of_cases, total_time = self.service.run_benchmark(
                scenario, algorithm, graph)
        except Exception as excep:
            print(excep)
        print("Number of cases: ", number_of_cases)
        print("Calculation time: ", total_time)
        print("--------------------")

    def _read_files(self, ending):
        files = [f for f in listdir("data/") if isfile(join("data/", f))]
        files = {f.split(".")[0] for f in files if f.endswith(ending)}
        d_files = {str(i): f for i, f in enumerate(files)}
        return d_files
