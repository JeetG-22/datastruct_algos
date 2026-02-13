from design.adj_list import adj_list

#count all possible paths from source to destination
def dfs(node, dst, visited):
    if node == dst:
        return 1
    if node in visited:
        return 0
    
    count = 0
    visited.add(node)
    for neighbour in adj_list[node]:
        count += dfs(neighbour, dst, visited)
    visited.remove(node)
    return count


 
print(adj_list)
print(f"# Of Paths From A to E: {dfs('A', 'E', set())}")


    
