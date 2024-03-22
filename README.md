# Romanian-map-problem
find the path from any city to Bucharest on the Romanian map, with A* algorithm and Greedy best-first search (GBFS) algorithm
![image](https://github.com/AhmedAlaa612/Romanian-map-problem/assets/53920535/1f2e7da4-235b-4a8c-8500-31de2e3ad56e)


## Algorithms Implemented
1. **A* Algorithm**: A search algorithm that finds the shortest path from the start node to the goal node by using a combination of the cost to reach the node and an estimate of the cost from the node to the goal.
   - often finds the shortest path
   - implemented in findAstar() funciton in the code
2. **Greedy Best First Search (GBFS)**: A search algorithm that selects the node that appears to be the closest to the goal according to a heuristic function.
   - doesn't always find the shortest path
   - implemented in findGBFS() function in the code

## How to Use
1. **Set Start and Goal Points**:
   - Set the start point in the main function (default is Arad).
     >If you wish to change the goal point, you'll need to provide heuristics between the goal point and each point on the map.

2. **Run the Code**:
   - After setting the start point and, if needed, the goal point, execute the code.

## OUTPUT
you can use the function **printPath(path, algorithm)** that takes list of city opbjects (a path) and Name of the algorithm used,
and prints the path and the distance of that path 
```
A* path: total distance (418)
Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
------------------------------------------
GBFS path: total distance (450)
Arad -> Sibiu -> Fagaras -> Bucharest
------------------------------------------
```

