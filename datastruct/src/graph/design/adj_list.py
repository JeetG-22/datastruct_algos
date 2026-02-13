"""
Two Implementation Approaches:
1) Using graph nodes to represent each vertice in an adjancency list
2) Just using a hashmap to map each key (vertice) to its neighbors
"""
#graph node used for adj list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbours = []

#or just use a hashmap
adj_list = {"A": [], "B": []}

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

def create_graph(adj_list, edge_list):
    for src, dst in edge_list:
        if src not in adj_list:
            adj_list[src] = []
        if dst not in adj_list:
            adj_list[dst] = []
        adj_list[src].append(dst)

create_graph(adj_list, edges)
