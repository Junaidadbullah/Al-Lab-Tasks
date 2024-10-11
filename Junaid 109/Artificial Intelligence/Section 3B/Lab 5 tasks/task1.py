# Task 1(lab 5)
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
def dfs(start, goal):
    stack = [start]  
    visited = []  
    while stack:
        node = stack.pop()  
        if node not in visited: 
            visited.append(node.data)  
            if node == goal:
                print(f"Goal '{node.data}' found")
                print(visited)
                return
            for i in node.children:
                if i not in visited:
                    stack.append(i)
    print(visited)
    print("Goal not found.")
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

A.children = [B, C]
B.children = [D,E]
C.children = [F]


dfs(A, E)  
