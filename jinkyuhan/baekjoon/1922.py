N = int(input())
M = int(input())

INF = 9999999
network = [[] for _ in range(N + 1)]

for _ in range(M):
    _u, _v, _w = list(map(int, input().split()))
    network[_u].append([_v, _w])
    network[_v].append([_u, _w])


def prim(start):
    is_visited = [False for _ in range(N + 1)]
    distance = [INF for _ in range(N + 1)]  # 현재 집합에 포함된 각 vertex의 nearest와의 거리

    # 시작점 초기화
    distance[start] = 0

    for _ in range(N):
        _min = INF
        for i in range(1, N + 1):
            if is_visited[i] is False and distance[i] < _min:
                _min = distance[i]
                u = i

        is_visited[u] = True

        for edge in network[u]:
            v = edge[0]
            w = edge[1]
            if is_visited[v] is False and w < distance[v]:
                distance[v] = w
    print(sum(distance[1:N + 1]))


prim(1)
