<!-- markdownlint-disable -->

# <kbd>module</kbd> `pathfinder`

---

## <kbd>class</kbd> `PathFinder3D`

A class to find the path between 2 cells of a 3D maze

**Args:**

- <b>`maze`</b> (:obj:`numpy array`): The 3D maze should have zeros for usable cells and ones for walls.
- <b>`nb_move_directions`</b> (int, optional): The number of directions that can be taken in one move. Integer value between 1 and 3 (default is 1)

### <kbd>method</kbd> `PathFinder3D.__init__`

```python
__init__(maze, nb_move_directions=1) → None
```

---

### <kbd>method</kbd> `PathFinder3D.create_move_list`

```python
create_move_list(nb_dimensions=1)
```

Compute the possible move list based on the nb of dimension moves allowed.

**Args:**

- <b>`nb_dimensions`</b> (int, optional): number of dimension that can change at each move. Value between 1 and 3, default is 1.

**Returns:**

- <b>`int`</b>: Manhattan distance between the input cell and the goal

---

### <kbd>method</kbd> `PathFinder3D.find_neighbours`

```python
find_neighbours(position)
```

Find accessibles neighbours from a cell.

It uses the list of moves defined when instanciating the PathFinder3D class. It also checks that the cells are within the grid and are not a wall.

**Args:**

- <b>`position`</b> (:obj:`numpy array`): the [x, y, z] coordinates of the cell for which we are searching the neighbours

**Returns:**

- <b>`list`</b>: a list of coordinates [x, y, z] of accessible neighbours.

---

### <kbd>method</kbd> `PathFinder3D.find_path`

```python
find_path(start, goal, alg='bfs')
```

Compute the path between a strat and a goal cell in a 3D maze

**Args:**

- <b>`start`</b> (list): Coordinates of the starting cell in the format [x, y, z]
- <b>`goal`</b> (list): Coordinates of the goal cell in the format [x, y, z]
- <b>`alg`</b> (str): Optional. Two algorithms are available, 'bfs' for Breadth First Search or 'a_star' for A\* algorithm. Default value is 'bfs'.

**Returns:**

- <b>`list`</b>: a list of coordinates [x, y, z] representing the path from the start cell to the goal. None if no path can be found.

---

### <kbd>method</kbd> `PathFinder3D.manhattan_distance`

```python
manhattan_distance(position)
```

Compute Manhattan distance between a cell and the goal.

**Args:**

- <b>`position`</b> (:obj:`numpy array`): the [x, y, z] coordinates of the cell to check

**Returns:**

- <b>`int`</b>: Manhattan distance between the input cell and the goal

---

### <kbd>method</kbd> `PathFinder3D.position_in_grid`

```python
position_in_grid(position)
```

Check if the given coordinates are within the grid boundaries

**Args:**

- <b>`position`</b> (:obj:`numpy array`): the [x, y, z] coordinates of the cell to check

**Returns:**

- <b>`bool`</b>: True if the cell is in the grid, False otherwise

---

### <kbd>method</kbd> `PathFinder3D.reconstruct_path`

```python
reconstruct_path(prev)
```

Reconstruct path from a dictionnary {cell: previous_cell}

**Returns:**

- <b>`list`</b>: a list of coordinates [x, y, z] representing the path from the start to the goal.

---

### <kbd>method</kbd> `PathFinder3D.solve_a_star`

```python
solve_a_star()
```

Performs A\* algortihm to identify the path between start and goal cells.

This algorithm uses the Manhattan distance as heuristic and is significantly faster than BFS. However, the solution is not guaranteed to be the shortest path.

**Returns:**

- <b>`dict`</b>: key is the destination cell, value is the previous cell following shortest path from the start cell

---

### <kbd>method</kbd> `PathFinder3D.solve_bfs`

```python
solve_bfs()
```

Performs a Breadth First Search to identify shortest path.

This always returns the shortest path if it exists but can be long on large scale mazes.

**Returns:**

- <b>`dict`</b>: key is the destination cell, value is the previous cell following shortest path from the start cell

---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
