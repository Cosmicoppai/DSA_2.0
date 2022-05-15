"""
Dijkstra Implementation in python
"""
from collections import defaultdict
from typing import Tuple, Dict
import heapq


class Graph:
    distances: Dict[int, Tuple[int, int]]

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_node(self, start_node: int, to_node: int, distance: int) -> None:
        self.graph[start_node].append((to_node, distance))

    def print_shortest_distances(self, source: int):
        self.dijkstra(source)
        for node, value in self.distances.items():
            print(source, "-> ", node, value)

    def dijkstra(self, source: int) -> None:
        distances = {source: 0}
        heap = []
        heapq.heappush(heap, (0, source))
        visited = set()

        for node in self.graph:
            if node != source:
                distances[node] = float('inf')

        while heap:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            for adj_node, adj_node_cost in self.graph[node]:
                if adj_node in visited:
                    continue
                new_dist = distances[node] + adj_node_cost
                if distances[adj_node] > new_dist:
                    distances[adj_node] = new_dist
                    heapq.heappush(heap, (new_dist, adj_node))
        self.distances = distances


if __name__ == "__main__":
    g = Graph(3)
    g.add_node(1, 2, 1)
    g.add_node(1, 3, 2)
    g.add_node(2, 3, 5)
    g.add_node(3, 1, 2)
    g.print_shortest_distances(1)
