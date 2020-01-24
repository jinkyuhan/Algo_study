
CONNECTED = 1
NO_CONNECTED= 0
VISITED = 8
NO_VISITED = 16

is_visited = []

def solution(n, computers):
    global is_visited
    is_visited = [NO_VISITED for _ in range(n)]
    answer = 0
    for com in range(n):
        if is_visited[com] == NO_VISITED:
            dfs(n, com, computers)
            answer +=1
    return answer

def dfs(n, u, computers):
    global is_visited
    is_visited[u] = VISITED

    for v in range(n):
        if is_visited[v] == NO_VISITED and computers[u][v] == CONNECTED:
            dfs(n, v, computers)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))