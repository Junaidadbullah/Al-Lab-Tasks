# Task2 (lab 5)PreOrder
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
visit=[]
def preorder(node):
    if node:
        visit.append(node.data)
        for i in node.children:
            preorder(i)

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

A.children = [B, C]
B.children = [D, E]
C.children = [F]
preorder(A)
print(f'visited{visit}')
