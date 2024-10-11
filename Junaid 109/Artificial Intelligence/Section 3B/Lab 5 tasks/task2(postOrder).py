# Task2 (lab 5)PostOrder
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
visit=[]
def postorder(node):
    if node:
        for i in node.children:
            postorder(i)
        visit.append(node.data)
        
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

A.children = [B, C]
B.children = [D, E]
C.children = [F]
postorder(A)
print(f'visited{visit}')
