from collections import deque

BLACK = 8
WHITE = 16
GRAY = 32

N, M, START = list(map(int, input().split()))
# sorting input
edges = [list(map(int, input().split())) for _ in range(M)]
edges = sorted(edges, key=lambda edge: (edge[0], edge[1]))

graph = [[] for _ in range(N + 1)]
color = [WHITE for _ in range(N + 1)]

for e in edges:
    from_vertex = e[0]
    to_vertex = e[1]
    graph[from_vertex].append({
        'to_vertex': to_vertex,
        'weight': 0
    })
    graph[to_vertex].append({
        'to_vertex': from_vertex,
        'weight': 0
    })


# DFS
def dfs(start):
    # visit, do something
    print(start, end=' ')
    color[start] = BLACK  # visit mark

    # recursion about all edges
    for u in graph[start]:
        v = u["to_vertex"]
        if color[v] == WHITE:
            dfs(v)


# BFS
def bfs(start):

    # enqueue root
    q = deque()
    q.append(start)

    # while queue isn't empty
    while q:
        # visit, do something
        u = q.popleft()
        color[u] = BLACK
        print(u, end=' ')
        # iterate about all edges
        for each_vertex in graph[u]:
            v = each_vertex["to_vertex"]
            if color[v] == WHITE:
                color[v] = GRAY
                q.append(v)


dfs(START)
color = [WHITE for _ in range(N + 1)]
print()
bfs(START)
