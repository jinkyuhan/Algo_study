import sys


def go_walk(li, m):
    mod = len(li) % m

    if mod == 0:
        s = 0
        idx = m-1
        while idx < len(li):
            s += 2 * li[idx]
            idx += m
        return s
    else:
        s1, s2 = 0, 0
        idx = mod - 1
        while idx < len(li):
            s1 += 2 * li[idx]
            idx += m
        idx = m-1
        while idx < len(li):
            s2 += 2 * li[idx]
            idx += m
        s2 += 2 * li[-1]
        return min(s1, s2)


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    books = sorted(list(map(int, sys.stdin.readline().split())))

    positive = []
    negative = []
    for i in books:
        if i < 0:
            negative.insert(0, abs(i))
        elif i > 0:
            positive.append(i)

    total_walk = 0
    if len(positive) > 0:
        total_walk += go_walk(positive, m)
    if len(negative) > 0:
        total_walk += go_walk(negative, m)

    if len(positive) == 0:
        last = negative[-1]
    elif len(negative) == 0:
        last = positive[-1]
    else:
        last = max(positive[-1], negative[-1])
    total_walk -= last
    print(total_walk)
