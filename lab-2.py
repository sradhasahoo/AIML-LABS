from collections import deque

graph = {
    "Alice": ["Charlie", "David"],
    "Charlie": ["Alice", "Emma"],
    "David": ["Alice", "Emma", "Fred"],
    "Emma": ["Bob", "Charlie", "David"],
    "Fred": ["Bob", "David"],
    "Bob": ["Emma", "Fred"]
}

for node in graph:
    graph[node] = sorted(graph[node])

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    print("\n========== BREADTH FIRST SEARCH ==========")

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            print(f"\nCurrent Node : {node}")
            print("Queue :", list(queue))
            print("Visited :", list(visited))

            if node == goal:
                print("\nGoal Found!")
                return path

            for neighbor in graph[node]:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    return None

def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()

    print("\n========== DEPTH FIRST SEARCH ==========")

    while stack:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            print(f"\nCurrent Node : {node}")
            print("Stack :", stack)
            print("Visited :", list(visited))

            if node == goal:
                print("\nGoal Found!")
                return path

           
            
            for neighbor in sorted(graph[node], reverse=True):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)

    return None

source = "Alice"
goal = "Bob"

bfs_path = bfs(graph, source, goal)
print("\nShortest Path using BFS:")
print(" -> ".join(bfs_path))

dfs_path = dfs(graph, source, goal)
print("\nPath found using DFS:")
print(" -> ".join(dfs_path))