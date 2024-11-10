from collections import defaultdict
import heapq as hq
import math

class GraphDijkstra:

    def __init__(self, V):
        self.V = V
        self.adj = [[float('inf')] * V for _ in range(V)]
        self.routes_coords_matrix = [[float('inf')] * V for _ in range(V)]

        for i in range(V):
            self.adj[i][i] = 0
            self.routes_coords_matrix[i][i] = 0

    def addEdge(self, u, v, w):
        self.adj[u][v] = w
        self.adj[v][u] = w

    def addRouteCoords(self, u, v, coords):
        self.routes_coords_matrix[u][v] = coords
        self.routes_coords_matrix[v][u] = coords

    def getRouteCoords(self, u, v):
        return self.routes_coords_matrix[u][v]

    def getMatrix(self):
        return self.adj


    def Dijkstra(self, S):
      n = self.V
      visited  = [False]*n
      path = [-1]*n
      cost = [math.inf]*n
      cost[S] = 0
      Q = [(0,S)]
      while Q:
        g,u = hq.heappop(Q)
        if not visited[u]:
          visited[u] = True
          for v in range(n):
            if not visited[v] and self.adj[u][v] > 0:
              f = g + self.adj[u][v]
              if f < cost[v]:
                cost[v] = f
                path[v] = u
                hq.heappush(Q,(f,v))
      return path,cost