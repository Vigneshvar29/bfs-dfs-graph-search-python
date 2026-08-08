# BFS and DFS Graph Search in Python

This project demonstrates two fundamental graph traversal algorithms in Python:

- **Breadth-First Search (BFS)** – used to find the shortest route in a metro network.
- **Depth-First Search (DFS)** – used to explore a maze and find a treasure room.

## Project Overview

The project uses practical examples to understand how BFS and DFS work on graphs.

### BFS – Metro Route

A metro network is represented as a graph where:

- Stations are represented as nodes.
- Direct connections between stations are represented as edges.
- BFS is used to find the shortest route between two stations.

**Example:**

Central -> Park -> Airport
DFS – Maze Treasure Hunt

A maze is represented as a graph where:

Rooms are represented as nodes.
Connections between rooms are represented as edges.
DFS explores one path deeply before backtracking.

Example:

Entrance
    ↓
Hallway
    ↓
Kitchen
    ↓
Dining Room
    ↓
Treasure Room
Algorithms Used
Breadth-First Search (BFS)

BFS explores a graph level by level.

For an unweighted graph, BFS guarantees that the first path found to the destination uses the minimum number of edges.

Depth-First Search (DFS)

DFS explores as deeply as possible along one path before backtracking.

DFS can find a path if one exists, but it does not guarantee the shortest path.

Concepts Covered
Graphs
Adjacency lists
Breadth-First Search
Depth-First Search
Queue
Recursion
Visited nodes
Shortest path
Backtracking
Project Structure
bfs-dfs-graph-search-python/
│
├── bfs_metro_route.py
├── dfs_maze_treasure.py
└── README.md
Requirements
Python 3.x

No external packages are required.

How to Run
Run BFS
python bfs_metro_route.py

Output:

Shortest Route:
Central -> Park -> Airport
Run DFS
python dfs_maze_treasure.py

Output:

Robot starts searching...

Exploring: Entrance
Exploring: Hallway
Exploring: Kitchen
Exploring: Dining Room
Exploring: Treasure Room

Treasure Found!
BFS vs DFS
Feature	BFS	DFS
Search strategy	Level by level	Depth first
Main structure	Queue	Recursion / Stack
Shortest path	Yes, for unweighted graphs	No
Backtracking	No	Yes
Project application	Metro route	Maze search
Learning Outcome

This project helped me understand and implement BFS and DFS graph traversal algorithms in Python using practical problem scenarios.

Future Improvements
Add user input for source and destination stations
Display the number of stops
Visualize the metro network
Create a larger maze
Add an interactive interface
Compare BFS and DFS performance
Author

Vigneshvar K S
