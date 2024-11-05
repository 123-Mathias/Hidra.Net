from collections import defaultdict
import heapq

class GraphPrim:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.adj = [[] for _ in range(V)]  # Lista de adyacencia

    # Adds an edge to an undirected graph
    def addEdge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    # The modified function to find MSTs for each connected component
    def PrimMST(self):
        mst_edges_all = []  # Lista para almacenar los bordes de todos los MSTs
        total_cost = 0  # Costo total de todos los MSTs
        visited = [False] * self.V  # Mantener seguimiento de vértices visitados

        # Ejecutar Prim en cada componente no visitado
        for start_node in range(self.V):
            if not visited[start_node]:  # Si el nodo no ha sido visitado, es un nuevo componente
                mst_edges = []  # Lista para almacenar los bordes del MST del componente actual
                component_cost = 0  # Costo del MST del componente actual
                min_heap = [(0, start_node, -1)]  # (peso, nodo, nodo padre)

                while min_heap:
                    weight, u, parent = heapq.heappop(min_heap)  # Obtener el borde con el peso mínimo
                    if visited[u]:
                        continue
                    visited[u] = True
                    if parent != -1:  # Si no es el nodo raíz
                        mst_edges.append((parent, u, weight))  # Agregar borde al MST
                        component_cost += weight  # Sumar el peso al costo del componente actual

                    for v, w in self.adj[u]:
                        if not visited[v]:
                            heapq.heappush(min_heap, (w, v, u))  # Agregar bordes al heap

                # Agregar resultados del componente actual a los resultados generales
                mst_edges_all.extend(mst_edges)
                total_cost += component_cost

        return mst_edges_all, total_cost