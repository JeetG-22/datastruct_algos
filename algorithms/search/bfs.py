from collections import deque

#layer-layer graph search for finding the minimum path 

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)
    
V = 5
graph = [[] for i in range(V)]
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 3)
add_edge(graph, 1, 4)
add_edge(graph, 2, 4)




