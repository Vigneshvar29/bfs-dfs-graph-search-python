from collections import deque

metro = {
    "Central": ["Park", "Museum"],
    "Park": ["Central", "City Mall", "Airport"],
    "Museum": ["Central", "Library"],
    "City Mall": ["Park"],
    "Library": ["Museum", "Airport"],
    "Airport": ["Park", "Library"]
}


def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        station = path[-1]

        if station == goal:
            return path

        if station not in visited:
            visited.add(station)

            for neighbor in graph[station]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


start = "Central"
goal = "Airport"

path = bfs_shortest_path(metro, start, goal)

print("Shortest Route:")
print(" -> ".join(path))
