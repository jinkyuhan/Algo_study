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

while stack:
    this = stack.pop()

    if this not in dfs:
        dfs.append(this)

    for i in sorted(graph[this], reverse=True):
        if i not in dfs:
            stack.append(i)
print(' '.join([str(i) for i in dfs]))

#bfs
q = [v]
bfs = [v]

while q:
    this = q.pop(0)

    for i in sorted(graph[this]):
        if i not in bfs:
            q.append(i)
            bfs.append(i)
print(' '.join([str(i) for i in bfs]))