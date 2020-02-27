import sys
from collections import deque

# 모든 점에 대해서 BFS.... Floyd-Warshall 로도 풀수 잇음

DEBUG = False
scan = sys.stdin.readline


def main():
    VISITED = 1
    VISITING = 0
    NO_VISITED = -1
    N = int(scan())
    adj_arr = [list(map(int, scan().strip().split())) for _ in range(N)]
    has_path = [[0 for _ in range(N)] for _ in range(N)]

    if DEBUG:
        print("input :")
        for li in adj_arr:
            print(li)

    q = deque()
    for i in range(N):
        is_visited = [NO_VISITED for _ in range(N)]
        q.append(i)
        while q:
            u = q.popleft()
            for v in range(N):
                if adj_arr[u][v] == 1 and is_visited[v] == NO_VISITED:
                    q.append(v)
                    is_visited[v] = VISITED
                    has_path[i][v] = 1

    for s in has_path:
        for d in s:
            print(d, end=' ')
        print("")


if __name__ == "__main__":
    main()
