from map_image import MapImage
from input_parser import InputParser
from textui import TextUI
from service import Service

OBSTACLE_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 50, 150)
VISITED_COLOR = (200, 50, 25)
ROUTE_COLOR = (0, 0, 0)
START_COLOR = (255, 255, 0)
END_COLOR = (0, 255, 0)
SCALE_FACTOR = 2


def main():
    service = Service()
    input_parser = InputParser()
    image = MapImage(OBSTACLE_COLOR, BACKGROUND_COLOR, VISITED_COLOR,
                     ROUTE_COLOR, START_COLOR, END_COLOR, SCALE_FACTOR)
    ctype, algorithm_name, image_map, start, end = input_parser.parse_input_args()

    # Start textUI if selected.
    if ctype == "start":
        txt_ui = TextUI(service, image)
        txt_ui.start()

    # If textUI not selected, use command line arguments instead.
    else:
        image.read("data/" + image_map + ".map")
        algorithm = service.select_algorithm(algorithm_name)

        # Calculate benchmark case.
        if ctype == "benchmark":
            number_of_cases, total_time = service.run_benchmark(
                image, algorithm)
            print("Number of cases: ", number_of_cases)
            print("Calculation time: ", total_time)

        # Calculate shortest distance for one case.
        else:
            shortest_distance, route, el_time, visited = service.calculate_distance(
                algorithm, image, start, end)
            print("Shortest distance: ", shortest_distance)
            print("Time used: ", el_time)
            print("Number of visited nodes/jump points: ", visited)
            service.show_image(image, algorithm, route, visited)


if __name__ == "__main__":
    main()
