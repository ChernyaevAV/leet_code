class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary to store graph

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def print_arr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Этот шаг нужен для выявления отрицательных весов и циклов
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        self.print_arr(dist)


if __name__ == '__main__':
    g = Graph(5)
    vertices = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2),
                (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]
    for item in vertices:
        g.add_edge(*item)
    g.bellman_ford(0)
