import numpy as np
import math

def calculate_distance(coord1, coord2):
    """Calculate the Euclidean distance between two coordinates."""
    lat1, lon1, lat2, lon2 = map(math.radians, [coord1[0], coord1[1], coord2[0], coord2[1]])

    a = math.sin((lat2 - lat1) / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 6371000   # Radio de la Tierra en metros
    distance = R * c
    return distance

def prim(hydrant_coords):
    """Implement Prim's algorithm to find the minimum spanning tree."""
    n = len(hydrant_coords)
    visited = [False] * n
    min_edges = [(0, 0)]  # (cost, to_node)
    total_cost = 0
    connections = []

    while len(connections) < n - 1:
        # Get the minimum edge from the visited set
        while min_edges:
            cost, to_node = min_edges.pop(0)
            if not visited[to_node]:
                visited[to_node] = True
                total_cost += cost
                connections.append(to_node)
                break

        # Add edges from the new node to the min_edges
        for next_node in range(n):
            if not visited[next_node]:
                distance = calculate_distance(hydrant_coords[to_node], hydrant_coords[next_node])
                min_edges.append((distance, next_node))
                min_edges.sort()  # Keep the edges sorted by cost

    return connections