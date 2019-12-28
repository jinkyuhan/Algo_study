from collections import deque

BLACK = 8
WHITE = 16
GRAY = 32

N, M, START = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
color = [WHITE for _ in range(N + 1)]

# make adjacency list
for _ in range(M):
    from_vertex, to_vertex = list(map(int, input().split()))
graph[from_vertex].append({
    "to_vertex": to_vertex,
    "weight": 0
})
graph[to_vertex].append({
    "to_vertex": from_vertex,
    "weight": 0
})


# DFS
def dfs(start):
    # visit, do something
    print(start, end=' ')
    color[start] = BLACK  # visit mark

    # recursion about all sorted edges
    for u in sorted(graph[start], key=lambda edge: edge["to_vertex"]):  # sorted by to_vertex
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
        for each_vertex in sorted(graph[u], key=lambda edge: edge["to_vertex"]):  # sorted by to_vertex
            v = each_vertex["to_vertex"]
            if color[v] == WHITE:
                color[v] = GRAY
                q.append(v)


dfs(START)
color = [WHITE for _ in range(N + 1)]
print()
bfs(START)
