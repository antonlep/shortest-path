import sys


class InputParser:
    """Class that parses command line arguments.
    """

    def parse_input_args(self):
        """Parses command line arguments.

        Returns:
            Tuple of calculation type (string), algorithm name (string),
            image file name (string), start point (tuple) and end point (tuple)
        """
        ctype = None
        algorithm = ""
        image_map = ""
        start = None
        end = None
        if len(sys.argv) <= 1:
            print("Incorrect input arguments.")
            print(
                """Positional arguments to use: [ dijkstra | a_star | jps]
                  [map name] [start point x-coord] [start point y-coord]
                  [end point x-coord] [end_point y-coord]""")
            sys.exit()
        elif sys.argv[1] == "benchmark":
            ctype = "benchmark"
            try:
                algorithm = sys.argv[2]
                image_map = sys.argv[3]
            except:
                print("Incorrect input arguments.")
                print(
                    "Positional arguments to use: benchmark [ dijkstra | a_star | jps] [ map name]")
                sys.exit()
        elif sys.argv[1] == "start":
            ctype = "start"
        else:
            ctype = "calculation"
            try:
                algorithm = sys.argv[1]
                image_map = sys.argv[2]
                start = (int(sys.argv[3]), int(sys.argv[4]))
                end = (int(sys.argv[5]), int(sys.argv[6]))
            except:
                print("Incorrect input arguments.")
                print(
                    """Positional arguments to use: [ dijkstra | a_star | jps]
                      [map name] [start point x-coord] [start point y-coord]
                      [end point x-coord] [end_point y-coord]""")
                sys.exit()
        return ctype, algorithm, image_map, start, end
