# by Ahmed Ismail 22010002
import queue
romania_map = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu_Vilcea', 80)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu_Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Rimnicu_Vilcea', 146), ('Pitesti', 138)],
    'Pitesti': [('Rimnicu_Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}
heuristics = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu_Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}
class city:
    def __init__(self, name, cost, parent, parent_distance):
        self.name = name
        self.cost = cost
        self.parent = parent
        self.parent_distance = parent_distance
    def __lt__(self, other):
        return self.cost < other.cost

def findAstar(start, goal):
    """A* search"""
    pq = queue.PriorityQueue()
    path = []
    pq.put(city(start, heuristics[start],None, 0))
    while not pq.empty():
        current = pq.get()
        path.append(current)
        if (current.name == goal): return path
        for nighbor in romania_map[current.name]:
            if nighbor[0] not in path:
                pq.put(city(nighbor[0],(heuristics[nighbor[0]]+ nighbor[1] + current.cost - heuristics[current.name]), current, nighbor[1]))
    return path

def findGBFS(start, goal):
    """greedy best first search"""
    pq = queue.PriorityQueue()
    path = []
    pq.put(city(start, heuristics[start],  None, 0))
    while not pq.empty():
        current = pq.get()
        path.append(current)
        if (current.name == goal): return path
        for nighbor in romania_map[current.name]:
            if nighbor[0] not in path:
                pq.put((city(nighbor[0],heuristics[nighbor[0]], current, nighbor[1])))
    return path

def countDistance(path):
    """returns the distance of the path"""
    distance = 0
    for city in path:
        distance += city.parent_distance
    return distance

def printPath(path, algorithm):
    """prints the path from start to goal"""
    c = path[-1]
    final = []
    while c:
        final.append(c)
        c = c.parent
    final.reverse()
    print(algorithm,f'path: total distance ({countDistance(final)})')
    for city in final:
        if city != final[-1]:
            print(city.name, '->', end=' ')
        else:
            print(city.name)
    print('------------------------------------------')

def main():
    start = 'Arad'
    goal = 'Bucharest'
    printPath(findAstar(start, goal), 'A*')
    printPath(findGBFS(start, goal), 'GBFS')

if __name__ == '__main__':
    main()