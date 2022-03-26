from heapq import heappush, heappop

class Dijkstra:
    def __init__(self):
        self.inf = 1e99

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
            if x == end:
                break
            if ready[x]:
                continue
            ready[x] = True
            for y in graph[x]:
                old = distance[y[0]]
                new = distance[x] + y[1]
                if new < old:
                    distance[y[0]] = new
                    previous[y[0]] = x
                    heappush(heap, (new, y[0]))
        if distance[end] == self.inf:
            return [], -1, {}
        route = self.calculate_route(previous, start, end)
        visited = self.calculate_visited(ready)
        return route, distance[end], visited

    def calculate_route(self, previous, start, end):
        route = [end]
        u = end
        while u != start:
            route.append(previous[u])
            u = previous[u]
        return route

    def calculate_visited(self, ready):
        visited = []
        for key, value in ready.items():
            if value == True:
                visited.append(key)
        return visited








            
