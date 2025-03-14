import numpy as np
import re
import json

ARRIVE_AT_DESTINATION_HEALTH = 666
GAME_OVER_HEALTH = 0
OBSTACLE_VALUE = 1

def _parse_map(map_string, map_size, reversal_nodes=[]):
    width, height = map_size
    filtered_chars = re.sub(r'[^a-zA-Z]', '', map_string)
    
    binary_map = [bin(ord(c))[2:].zfill(8) for c in filtered_chars]
    
    flat_map = []
    for binary_str in binary_map:
        first_half = int(binary_str[:4], 2)
        second_half = int(binary_str[4:], 2)
        flat_map.extend([first_half % 2, second_half % 2])
    
    while len(flat_map) < width * height:
        flat_map.append(0)
    
    flat_map = flat_map[:width * height]
    
    grid = np.array(flat_map).reshape((height, width))
    
    for x, y in reversal_nodes:
        if 0 <= x < height and 0 <= y < width:
            grid[y, x] ^= 1
    
    return grid

def _load_maze_from_json(maze_level_name):
    with open("./src/game/maze_level/" + maze_level_name + ".json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return {
        "maze_level_name": data.get("maze_level_name", "Unknown Level"),
        "map_size": tuple(data.get("map_size", [10, 10])),
        "starting_position": tuple(data.get("starting_position", [0, 0])),
        "end_position": tuple(data.get("end_position", [0, 0])),
        "map": _parse_map(data.get("map", ""), tuple(data.get("map_size", [10, 10])), data.get("reversal_node", []))
    }

def hit_obstacle(position, maze_level_name):
    x, y = position
    maze_data = _load_maze_from_json(maze_level_name)  # You can replace this with the actual level you're working with
    grid = maze_data["map"]
    
    # Check if the position is within the bounds of the grid
    if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:
        # Return True if there's an obstacle (1) at the position, False if free space (0)
        return grid[y, x] == OBSTACLE_VALUE
    else:
        # Position is out of bounds
        return True

def game_over(health):
    return health in {GAME_OVER_HEALTH, ARRIVE_AT_DESTINATION_HEALTH}

def arrive_at_destination(maze_level_name, current_position):
    with open("./src/game/maze_level/" + maze_level_name + ".json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    end_position = tuple(data.get("end_position", [0, 0]))
    return tuple(current_position) == end_position
