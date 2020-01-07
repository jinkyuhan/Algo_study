import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    rope = [int(sys.stdin.readline()) for _ in range(n)]

    rope_asc = sorted(rope)
    this_idx = 0    # x th rope -> n-x ropes are stronger
    max_weight = 0

    while this_idx < n:
        this_weight = rope_asc[this_idx]
        k = n - this_idx
        wi = this_weight * k

        if max_weight < wi:
            max_weight = wi
        this_idx += 1

    print(max_weight)
