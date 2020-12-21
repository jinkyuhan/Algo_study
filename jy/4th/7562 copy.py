import sys
r = sys.stdin.readline


def bfs(src: tuple, dst: tuple, l: int, visited: list, count: list) -> None:
    from collections import deque
    q = deque()
    q.appendleft(src)

    while q:
        this = q.pop()
        this_x, this_y = this
        if this == dst:
            break
        visited[this_x][this_y] = 1

        next_list = [(this_x-2, this_y+1), (this_x-1, this_y+2), (this_x+1, this_y+2), (this_x+2, this_y+1),
                     (this_x-2, this_y-1), (this_x-1, this_y-2), (this_x+1, this_y-2), (this_x+2, this_y-1)]
        for each in next_list:
            each_x, each_y = each
            if 0 <= each_x < l and 0 <= each_y < l and visited[each_x][each_y] == 0:
                count[each_x][each_y] = count[this_x][this_y] + 1
                visited[each_x][each_y] = 1
                q.appendleft(each)

if __name__ == "__main__":
    test = int(r())
    l_list = []
    src_list = []
    dst_list = []

    for i in range(test):
        l_list.append(int(r()))
        src_list.append(tuple(map(int, r().split())))
        dst_list.append(tuple(map(int, r().split())))

    for i in range(test):
        l = l_list[i]
        src = src_list[i]
        dst = dst_list[i]

        if src == dst:
            print(0)
            continue

        visited = [[0 for _ in range(l)] for _ in range(l)]
        count = [[0 for _ in range(l)] for _ in range(l)]

        bfs(src, dst, l, visited, count)

        print(count[dst[0]][dst[1]])
