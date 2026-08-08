maze = {
    "Entrance": ["Hallway", "Storage"],
    "Hallway": ["Kitchen", "Living Room"],
    "Kitchen": ["Dining Room"],
    "Dining Room": ["Treasure Room"],
    "Living Room": ["Bedroom"],
    "Bedroom": ["Bathroom"],
    "Bathroom": [],
    "Storage": ["Garage"],
    "Garage": ["Workshop"],
    "Workshop": [],
    "Treasure Room": []
}

visited = []


def dfs(room):
    if room not in visited:
        print("Exploring:", room)
        visited.append(room)

        if room == "Treasure Room":
            print("\nTreasure Found!")
            return True

        for next_room in maze[room]:
            if dfs(next_room):
                return True

    return False


print("Robot starts searching...\n")
dfs("Entrance")
