from collections import defaultdict
import heapq

class GraphPrim:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.adj = [[] for _ in range(V)]

    def addEdge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def PrimMST(self):
        mst_edges_all = []
        total_cost = 0
        visited = [False] * self.V

        for start_node in range(self.V):
            if not visited[start_node]:
                mst_edges = []
                component_cost = 0
                min_heap = [(0, start_node, -1)]

                while min_heap:
                    weight, u, parent = heapq.heappop(min_heap)
                    if visited[u]:
                        continue
                    visited[u] = True
                    if parent != -1:
                        mst_edges.append((parent, u, weight))
                        component_cost += weight

                    for v, w in self.adj[u]:
                        if not visited[v]:
                            heapq.heappush(min_heap, (w, v, u))

                mst_edges_all.extend(mst_edges)
                total_cost += component_cost

        return mst_edges_all, total_cost