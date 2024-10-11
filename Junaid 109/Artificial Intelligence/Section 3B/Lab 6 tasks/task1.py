# Lab 6 task 1
visit = []  
def bfs(data, start, goal):
    queue = [start]   
    while queue:
        node = queue.pop(0)  
        if node not in visit:
            visit.append(node)   
            if node == goal:
                print(f"Goal '{goal}' found")
                return
            for i in data[node]:
                if i not in visit:
                    queue.append(i) 

    print("Goal not found.")
Data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G':[]
}
bfs(Data, 'A', 'G')
print(visit)
