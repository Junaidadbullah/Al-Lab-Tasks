# Task2 (lab 5)inorder
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
visit=[]
def inorder(node): 
    if node:
        if node.children:
            inorder(node.children[0])
        visit.append(node.data)
        for i in node.children[1:]:
            inorder(i)
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')

A.children = [B, C]
B.children = [D, E]
C.children = [F,G]
inorder(A)
print(f'visited{visit}')
