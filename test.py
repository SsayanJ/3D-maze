import numpy as np
import time

from bfs import PathFinder3D


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


def test_cornered(alg='bfs'):
    maze = np.zeros((7, 7, 1))
    maze[1, 1:5, :] = 1
    maze[5, 1:5, :] = 1
    maze[2:5, 4, :] = 1
    start = [3, 2, 0]
    goal = [6, 6, 0]
    my_pathfinder = PathFinder3D(maze)
    return my_pathfinder.find_path(start, goal, alg=alg)


def test_big_maze(alg='bfs'):
    maze = np.zeros((40, 50, 60))
    maze[1, 1:5, :] = 1
    maze[5, 1:5, :] = 1
    maze[2:5, 4, :] = 1
    start = [12, 2, 34]
    goal = [31, 45, 1]
    my_pathfinder = PathFinder3D(maze)
    return my_pathfinder.find_path(start, goal, alg=alg)


def test_big_maze2(alg='bfs'):
    maze = np.zeros((40, 50, 60))
    maze[np.random.random(size=(40, 50, 60)) > 0.8] = 1
    start = [3, 2, 14]
    goal = [39, 45, 1]
    maze[tuple(start)] = 0
    maze[tuple(goal)] = 0
    my_pathfinder = PathFinder3D(maze, 3)
    return my_pathfinder.find_path(start, goal, alg=alg)


if __name__ == "__main__":
    print(test_wall())
    print(test_2_passing_walls())
    print(test_cornered())
    start_time = time.time()
    solution = test_big_maze2()
    print(solution)
    end_time = time.time()
    print('BFS time:', end_time-start_time)
    if solution:
        print('BFS solution length:', len(solution))
    start_time = time.time()
    solution = test_big_maze2(alg='a*')
    print(solution)
    end_time = time.time()
    print('A* time:', end_time-start_time)
    if solution:
        print('A* solution length:', len(solution))
