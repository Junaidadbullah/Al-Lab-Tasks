# Lab 6 task 2
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []  
visited = []  
def bfs(start, goal):
    queue = [start]  
    while queue:
        node = queue.pop(0) 
        if node not in visited:
            visited.append(node)  
            if node.data == goal:
                print(f"Goal '{goal}' found")
                return       
            for i in node.children:
                if i not in visited:
                    queue.append(i) 
    print("Goal not found.")

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

A.children = [B, C]
B.children = [D, E]
C.children = [F]
bfs(A,'E')
print(visited)