def solution(A):
    N = len(A)
    is_missed = [True for _ in range(N + 2)]
    for num in A:
        is_missed[num] = False
    for i in range(1, len(is_missed)):
        if is_missed[i]:
            return i


print(solution([1, 3, 2, 4]))
