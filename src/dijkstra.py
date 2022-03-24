from heapq import heappush, heappop

class Dijkstra:
    def __init__(self):
        self.inf = 1e99

    def create_graph(self, map):
        n = len(map)
        m = len(map[0])
        graph = {}
        moves = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for i in range(n):
            for j in range(m):
                    graph[(i,j)] = []
        for i in range(n):
            for j in range(m):
                pos = (i, j)
                if map[i][j] == ".":
                    for move in moves:
                        new_pos = (i + move[0], j + move[1])
                        if 0 <= new_pos[0] < n and 0 <= new_pos[1] < m:
                            if map[new_pos[0]][new_pos[1]] == ".":
                                graph[pos].append(new_pos)
        return graph

    def calculate_distance(self, graph, start, end):
        distance = {}
        previous = {}
        ready = {}
        for i in graph:
            distance[i] = self.inf
            ready[i] = False
        distance[start] = 0
        heap = []
        heappush(heap, (0, start))
        while heap:
            d, x = heappop(heap)
            if ready[x]:
                continue
            ready[x] = True
            for y in graph[x]:
                old = distance[y]
                new = distance[x] + 1
                if new < old:
                    distance[y] = new
                    previous[y] = x
                    heappush(heap, (new, y))
        if distance[end] == self.inf:
            return -1
        route = [end]
        u = end
        while u != start:
            route.append(previous[u])
            u = previous[u]
        return route, distance[end]







            
