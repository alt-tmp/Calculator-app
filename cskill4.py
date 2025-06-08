from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print(f"BFS Traversal starting from vertex {start}:")
    
    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Enqueue all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Graph representation using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

# Call BFS
bfs(graph, 'A')

# Custom message
print("\n Vedant")