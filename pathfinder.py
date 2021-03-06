import numpy as np
from queue import Queue, PriorityQueue
import time


class PathFinder3D:
    """A class to find the path between 2 cells of a 3D maze

    Args:
        maze(:obj:`numpy array`): The 3D maze should have zeros for usable cells
            and ones for walls.
        nb_move_directions(int, optional): The number of directions that can be taken
            in one move. Integer value between 1 and 3 (default is 1)

    """

    def __init__(self, maze, nb_move_directions=1) -> None:
        self.maze = np.array(maze, dtype=int)
        self.moves = self._create_move_list(nb_move_directions)
        self.solved = False
        self.N, self.M, self.K = self.maze.shape
        self.nb_move_directions = nb_move_directions

    def find_path(self, start, goal, alg='bfs'):
        """Compute the path between a strat and a goal cell in a 3D maze

        Args:
            start (list): Coordinates of the starting cell in the format [x, y, z]
            goal (list): Coordinates of the goal cell in the format [x, y, z]
            alg (str, optional): Two algorithms are available, 'bfs' for Breadth First Search 
                or 'a_star' for A* algorithm. Default value is 'bfs'.

        Returns:
            list: a list of coordinates [x, y, z] representing the path from the start cell to the goal.
                None if no path can be found.
        """
        self.solved = False
        self.visited = np.zeros(self.maze.shape)
        self.start = np.array(start).astype(int)
        self.goal = np.array(goal).astype(int)
        if alg == 'bfs':
            previous_cell_dict = self._solve_bfs()
        elif alg == 'a_star':
            self.distances = np.empty(self.maze.shape)
            self.distances.fill(np.inf)
            previous_cell_dict = self._solve_a_star()
        else:
            raise ValueError(
                f'alg parameter received an unexpected value {alg}')
        if self.solved:
            self.solution = self._reconstruct_path(previous_cell_dict)
        else:
            print('No path found between between the start and stop cells')
            self.solution = None
        return self.solution

    def _solve_bfs(self):
        """Performs a Breadth First Search to identify shortest path.

        This always returns the shortest path if it exists but can be long on 
        large scale mazes.

        Returns:
            dict: key is the destination cell, value is the previous cell following
            shortest path from the start cell
        """
        cells_queue = Queue()
        cells_queue.put(self.start)
        self.visited[tuple(self.start)] = 1
        previous_cell_dict = {}
        while not cells_queue.empty():
            current = cells_queue.get()
            if np.all(current == self.goal):
                self.solved = True
                break
            neighbour_list = self._find_neighbours(current)
            for neighbour in neighbour_list:
                cells_queue.put(neighbour)
                self.visited[tuple(neighbour)] = 1
                previous_cell_dict[tuple(neighbour)] = current
        return previous_cell_dict

    def _solve_a_star(self):
        """Performs A* algortihm to identify the path between start and goal cells.

        This algorithm uses the Manhattan distance as heuristic and is significantly
        faster than BFS. However, the solution is not guaranteed to be the shortest path.

        Returns:
            dict: key is the destination cell, value is the previous cell following
                shortest path from the start cell
        """
        cells_queue = PriorityQueue()
        cells_queue.put((0, self.start))
        previous_cell_dict = {}
        self.distances[tuple(self.start)] = 0
        while not cells_queue.empty():
            current = np.array(cells_queue.get()[1])
            if np.all(current == self.goal):
                self.solved = True
                break
            neighbour_list = self._find_neighbours(current)
            for neighbour in neighbour_list:
                neighbour_distance = self.distances[tuple(current)] + 1
                if neighbour_distance < self.distances[tuple(neighbour)]:
                    self.distances[tuple(neighbour)] = neighbour_distance
                    if self.nb_move_directions == 1:
                        priority = int(neighbour_distance +
                                       self._manhattan_distance(neighbour))
                    elif self.nb_move_directions == 2:
                        priority = int(neighbour_distance +
                                       self._diagonal_distance(neighbour))
                    else:
                        priority = int(neighbour_distance +
                                       self._euclidian_distance(neighbour))
                    cells_queue.put((priority, tuple(neighbour)))
                    previous_cell_dict[tuple(neighbour)] = current
        return previous_cell_dict

    def _reconstruct_path(self, prev):
        """Reconstruct path from a dictionnary {cell: previous_cell}

        Returns:
            list: a list of coordinates [x, y, z] representing the path from the start to the goal.

        """
        path = [self.goal]
        current_position = path[-1]
        while not np.all(current_position == self.start):
            current_position = prev[tuple(current_position)]
            path.append(current_position)
        path.reverse()
        return [list(cell) for cell in path]

    def _find_neighbours(self, position):
        """Find accessibles neighbours from a cell.

        It uses the list of moves defined when instanciating the PathFinder3D class.
        It also checks that the cells are within the grid and are not a wall.

        Args:
            position(:obj:`numpy array`): the [x, y, z] coordinates of the cell
                for which we are searching the neighbours

        Returns:
            list: a list of coordinates [x, y, z] of accessible neighbours.

        """
        neighbour_list = []
        for move in self.moves:
            neighbour = position + move
            if self._position_in_grid(neighbour) and self.maze[tuple(neighbour)] == 0 and self.visited[tuple(neighbour)] == 0:
                neighbour_list.append(neighbour)
        return neighbour_list

    def _position_in_grid(self, position):
        """Check if the given coordinates are within the grid boundaries

        Args:
            position(:obj:`numpy array`): the [x, y, z] coordinates of the cell to check

        Returns:
            bool: True if the cell is in the grid, False otherwise

        """
        return not(np.any(position < 0) or position[0] >= self.N or position[1] >= self.M or position[2] >= self.K)

    def _manhattan_distance(self, position):
        """Compute Manhattan distance between a cell and the goal.

        Args:
            position(:obj:`numpy array`): the [x, y, z] coordinates of the cell to check
                the Manhattan distance from the goal

        Returns:
            int: Manhattan distance between the input cell and the goal

        """
        return abs(position[0] - self.goal[0]) + abs(position[1] - self.goal[1]) + abs(position[2] - self.goal[2])

    def _euclidian_distance(self, position):
        """Compute Euclidian distance between a cell and the goal.

        Args:
            position(:obj:`numpy array`): the [x, y, z] coordinates of the cell to check
                the Euclidian distance from the goal

        Returns:
            int: Euclidian distance between the input cell and the goal

        """
        return np.linalg.norm(position-self.goal)

    def _diagonal_distance(self, position):
        """Compute Diagonal distance between a cell and the goal.

        Args:
            position(:obj:`numpy array`): the [x, y, z] coordinates of the cell to check
                the Diagonal distance from the goal

        Returns:
            int: Diagonal distance between the input cell and the goal

        """
        dx = abs(position[0]-self.goal[0])
        dy = abs(position[1]-self.goal[1])
        dz = abs(position[2]-self.goal[2])
        dmin = min(dx, dy, dz)
        dmax = max(dx, dy, dz)
        dmid = dx + dy + dz - dmin - dmax

        return (np.sqrt(3) - np.sqrt(2)) * dmin + (np.sqrt(2) - 1) * dmid + 1 * dmax

    def _create_move_list(self, nb_dimensions=1):
        """Compute the possible move list based on the nb of dimension moves allowed.

        Args:
            nb_dimensions(int, optional): number of dimension that can change at
                each move. Value between 1 and 3, default is 1.

        Returns:
            list: list of possible moves as a list of numpy arrays

        """
        move_list = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if 0 < abs(i)+abs(j) + abs(k) <= nb_dimensions:
                        move_list.append(np.array([i, j, k]))
        return move_list


if __name__ == "__main__":
    start_time = time.time()
    maze = np.zeros((7, 8, 10))
    maze[1, 0, 0] = 1
    maze[:-1, 2, :] = 1
    maze[3, :, 1:] = 1
    pf = PathFinder3D(maze, 1)
    print(pf.find_path([0, 1, 2], [5, 3, 6]))
