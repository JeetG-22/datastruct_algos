from collections import deque
from design.adj_list import adj_list

#shortest path from source to destination
def bfs(node, target):
    q = deque(node)
    visited = set()
    length = 0

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node == target:
                return length
            for neighbour in adj_list[node]:
                if neighbour in visited:
                    continue
                q.append(neighbour)
                visited.add(neighbour)
        length += 1
    return length

print(adj_list)
print(f"Shortest Path From A to E: {bfs('A', 'E')}")