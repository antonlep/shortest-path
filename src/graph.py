import math


class Graph:
    """Class that converts map file from image to graph format.

    Args:
        image: MapImage object to be converted.
    """

    def __init__(self, image):
        self.graph = self.create_graph(image)

    def create_graph(self, image):
        """Converts image file to graph.

        Returns:
            Graph as 2D list which includes neighboring nodes and their cost
        """
        straight_cost = 1
        diagonal_cost = math.sqrt(2)
        n = len(image.data)
        m = len(image.data[0])
        graph = [[[]]*m for _ in range(n)]
        moves_straight = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        moves_diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for i in range(n):
            for j in range(m):
                neighbors = []
                if image.data[i][j] == ".":
                    for move in moves_straight:
                        new_pos = (i + move[0], j + move[1])
                        if 0 <= new_pos[0] < n and 0 <= new_pos[1] < m:
                            if image.data[new_pos[0]][new_pos[1]] == ".":
                                neighbors.append(((new_pos), straight_cost))
                    for move in moves_diagonal:
                        new_pos = (i + move[0], j + move[1])
                        if 0 <= new_pos[0] < n and 0 <= new_pos[1] < m:
                            if image.data[new_pos[0]][new_pos[1]] == ".":
                                neighbors.append(((new_pos), diagonal_cost))
                graph[i][j] = neighbors
        return graph
