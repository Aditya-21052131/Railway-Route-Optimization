class Routes:
    def __init__(self, graph):
        self.graph = graph

    def find_optimized_route(self, origin, destination):
        dist = self.graph.dijkstra(origin)
        optimized_route = []
        current_station = destination
        while current_station != origin:
            optimized_route.append(current_station)
            for i in range(self.graph.V):
                if self.graph.graph[current_station][i] > 0 and dist[i] < dist[current_station]:
                    current_station = i
                    break
        optimized_route.append(origin)
        optimized_route.reverse()
        return optimized_route
