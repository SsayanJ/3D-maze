# 3D-maze

Find shortest path in a 3D maze

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

### <kbd>method</kbd> `PathFinder3D.find_path`

```python
find_path(start, goal, alg='bfs')
```

Compute the path between a strat and a goal cell in a 3D maze

**Args:**

- <b>`start`</b> (list): Coordinates of the starting cell in the format [x, y, z]
- <b>`goal`</b> (list): Coordinates of the goal cell in the format [x, y, z]
- <b>`alg`</b> (str, optional): Two algorithms are available, 'bfs' for Breadth First Search or 'a*' for A* algorithm.

**Returns:**

- <b>`list`</b>: a list of coordinates [x, y, z] representing the path from the start cell to the goal. None if no path can be found.
