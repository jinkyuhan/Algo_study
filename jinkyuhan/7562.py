import sys
from collections import deque

DEBUG = False
DIRECTION = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
BLACK = "1"  # visited
GRAY = "0"  # visiting
WHITE = "-1"  # no visited yet
INF = 90001


def bfs(size, start, dest):
    # Set constants
    is_visit = [[WHITE for _ in range(size)] for _ in range(size)]
    distance = [[INF for _ in range(size)] for _ in range(size)]
    parent = [[(-1, -1) for _ in range(size)] for _ in range(size)]
    q = deque()

    distance[start[1]][start[0]] = 0
    q.appendleft(start)
    while q:
        knight = q.pop()
        is_visit[knight[1]][knight[0]] = BLACK
        if knight == dest:
            break
        for direction in DIRECTION:
            pos = (knight[0] + direction[0], knight[1] + direction[1])
            if 0 <= pos[1] < size and 0 <= pos[0] < size and is_visit[pos[1]][pos[0]] == WHITE:
                distance[pos[1]][pos[0]] = distance[knight[1]][knight[0]] + 1
                parent[pos[1]][pos[0]] = (knight[0], knight[1])
                is_visit[pos[1]][pos[0]] = GRAY
                q.appendleft(pos)

    print(distance[dest[1]][dest[0]])

    if DEBUG:
        print("colors: ")
        for c in is_visit:
            print(c)

        print("distance: ")
        for d in distance:
            print(d)

        print("parent: ")
        for p in parent:
            print(p)


def main():
    scan = sys.stdin.readline
    TEST_CASE_CNT = int(scan())
    size = []
    start = []
    dest = []
    # Scan all the test-case
    for _ in range(TEST_CASE_CNT):
        size.append(int(scan()))
        start.append(tuple(map(int, scan().strip().split())))
        dest.append(tuple(map(int, scan().strip().split())))
    # BFS for each test-case
    for i in range(TEST_CASE_CNT):
        bfs(size[i], start[i], dest[i])


if __name__ == "__main__":
    main()
