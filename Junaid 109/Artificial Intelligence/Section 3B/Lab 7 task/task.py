# lab 7 task
class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent 
        self.g = 0 
        self.h = 0
        self.f = 0 

    def __eq__(self, other):
        return self.name == other.name

def aStar(start, goal, data, heuristic):
    starting = []
    end = []  
    starting.append(start)
    while starting:
        curr_node = starting[0]
        for node in starting:
            if node.f < curr_node.f:
                curr_node = node
        starting.remove(curr_node)
        end.append(curr_node)
        if curr_node == goal:
            path = []
            while curr_node:
                path.append(curr_node.name)
                curr_node = curr_node.parent
            return path[::-1] 

        for i in data[curr_node.name]:
            x = Node(i, curr_node)
            if x in end:
                continue
            x.g = curr_node.g + 1 
            x.h = heuristic[x.name]
            x.f = x.g + x.h
            if addtoStart(starting, x):
                starting.append(x)

    return None

def addtoStart(starting, x):
    for node in starting:
        if x == node and x.g >= node.g:
            return False
    return True

data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}
startNode = Node('A')
goalnode = Node('G')
path = aStar(startNode, goalnode, data, heuristic)
if path:
    print(" -> ".join(path))
else:
    print("No path found.")
