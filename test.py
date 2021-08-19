import numpy as np
import time

from pathfinder import PathFinder3D


def given_maze(alg='bfs'):
    start = [0, 0, 0]
    goal = [2, 3, 3]
    maze = [[[0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 0], [0, 0, 1, 0]],
            [[1, 0, 1, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]],
            [[1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 0, 1], [0, 0, 1, 0]]]
    my_pathfinder = PathFinder3D(maze)
    return my_pathfinder.find_path(start, goal, alg=alg)


def test_wall(alg='bfs'):
    maze = np.zeros((5, 5, 5))
    maze[:, 2, :] = 1
    start = [0, 0, 0]
    goal = [0, 4, 0]
    my_pathfinder = PathFinder3D(maze)
    return my_pathfinder.find_path(start, goal, alg=alg)


def test_2_passing_walls(alg='bfs'):
    maze = np.zeros((5, 5, 5))
    maze[:-1, 1, :] = 1
    maze[1:, 3, :] = 1
    start = [0, 0, 0]
    goal = [0, 4, 0]
    my_pathfinder = PathFinder3D(maze)
    return my_pathfinder.find_path(start, goal, alg=alg)


def test_single_holes(alg='bfs'):
    maze = np.zeros((5, 5, 5))
    maze[:, 1, :] = 1
    maze[3, 1, 3] = 0
    maze[:, 3, :] = 1
    maze[1, 3, 4] = 0
    start = [0, 0, 0]
    goal = [0, 4, 0]
    my_pathfinder = PathFinder3D(maze)
    return my_pathfinder.find_path(start, goal, alg=alg)


def test_cornered(alg='bfs'):
    maze = np.zeros((7, 7, 1))
    maze[1, 1:5, :] = 1
    maze[5, 1:5, :] = 1
    maze[2:5, 4, :] = 1
    start = [3, 2, 0]
    goal = [6, 6, 0]
    my_pathfinder = PathFinder3D(maze)
    return my_pathfinder.find_path(start, goal, alg=alg)


def create_big_maze(start, goal, percentage_walls=0.2, nb_dim=1):
    maze = np.zeros((40, 50, 60))
    maze[np.random.random(size=(40, 50, 60)) < percentage_walls] = 1
    maze[tuple(start)] = 0
    maze[tuple(goal)] = 0
    my_pathfinder = PathFinder3D(maze, nb_dim)
    return my_pathfinder


if __name__ == "__main__":
    # simple tests where the shortest path is known
    print("Subject maze: ", given_maze(), "\n")
    print("Maze with a blocking wall: ", test_wall())
    print("\n2 passing walls: ", test_2_passing_walls())
    print("\nStarting cell is cornered, need to go backwards: ", test_cornered())
    print("\nBFS with single holes in  2 walls: ", test_single_holes())
    print("\nA* with single holes in  2 walls: ", test_single_holes('a_star'))

    # test on large scale maze with 1 dimension moves
    start = [12, 2, 34]
    goal = [31, 45, 1]
    walls_percent = 0.2
    my_path_finder = create_big_maze(
        start, goal, percentage_walls=walls_percent, nb_dim=1)
    start_time = time.time()
    solution = my_path_finder.find_path(start, goal, alg='bfs')
    end_time = time.time()
    print(f'\n====== Walls percentage: {walls_percent*100}% ======')
    print('\n###### With moves dimension = 1 ######')
    print(f'BFS time: {end_time-start_time:.2f}s')
    if solution:
        print('BFS solution length:', len(solution))
    start_time = time.time()
    solution = my_path_finder.find_path(start, goal, alg='a_star')
    end_time = time.time()
    print(f'A* time: {end_time-start_time:.2f}s')
    if solution:
        print('A* solution length:', len(solution))

    # test on large scale maze with 2 dimension moves
    my_path_finder = create_big_maze(
        start, goal, percentage_walls=walls_percent, nb_dim=2)
    start_time = time.time()
    solution = my_path_finder.find_path(start, goal, alg='bfs')
    end_time = time.time()
    print('\n###### With moves dimension = 2 ######')
    print(f'BFS time: {end_time-start_time:.2f}s')
    if solution:
        print('BFS solution length:', len(solution))
    start_time = time.time()
    solution = my_path_finder.find_path(start, goal, alg='a_star')
    end_time = time.time()
    print(f'A* time: {end_time-start_time:.2f}s')
    if solution:
        print('A* solution length:', len(solution))

    # test on large scale maze with 3 dimension moves
    my_path_finder = create_big_maze(
        start, goal, percentage_walls=walls_percent, nb_dim=3)
    start_time = time.time()
    solution = my_path_finder.find_path(start, goal, alg='bfs')
    end_time = time.time()
    print('\n###### With moves dimension = 3 ######')
    print(f'BFS time: {end_time-start_time:.2f}s')
    if solution:
        print('BFS solution length:', len(solution))
    start_time = time.time()
    solution = my_path_finder.find_path(start, goal, alg='a_star')
    end_time = time.time()
    print(f'A* time: {end_time-start_time:.2f}s')
    if solution:
        print('A* solution length:', len(solution))
