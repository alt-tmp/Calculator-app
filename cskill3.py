# DFS function
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': [],
    'E': []
}

# Starting DFS from node A
print("DFS Traversal starting from vertex A:")
visited = set()
dfs(graph, 'A', visited)

# Printing a custom message
print("\n Vedant Tayade")