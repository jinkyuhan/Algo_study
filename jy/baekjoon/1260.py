n, m, v = map(int, input().split())
graph = {}

for i in range(m):
    v1, v2 = map(int, input().split())
    
    if v1 not in graph:
        graph[v1] = []
    graph[v1].append(v2)
    
    if v2 not in graph:
        graph[v2] = []
    graph[v2].append(v1)

#dfs
stack = [v]
dfs = []

while len(dfs) < len(graph):
    this = stack.pop()

    for i in sorted(graph[this], reverse=True):
        if i not in dfs:
            stack.append(i)

    if this not in dfs:
        dfs.append(this)
print(dfs)

#bfs
import queue
q = queue.Queue()
q.put(v)
bfs = []

while len(bfs) < len(graph):
    this = q.get()

    for i in sorted(graph[this]):
        if i not in bfs:
            q.put(i)
    
    if this not in bfs:
        bfs.append(this)
print(bfs)