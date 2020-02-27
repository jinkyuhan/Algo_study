def solution(A):
    N = len(A)
    l_total = 0
    r_total = 0
    l_leader = None
    r_leader = None
    left_count = {}
    right_count = {}
    for i in range(N):
        right_count[str(A[i])] = right_count.get(str(A[i]), 0) + 1
        r_total += 1
        r_max = max(list(right_count.items()))
        r_leader = r_max if r_max > r_total/2 else None
    print(r_leader)


solution([4, 3, 4, 4, 4, 2])
