def solution(A):
    N = len(A)
    left_sum = A[0]
    right_sum = sum(A) - A[0]
    min_ = abs(left_sum - right_sum)
    for p in range(1, N - 1):
        left_sum += A[p]
        right_sum -= A[p]
        min_ = min(min_, abs(left_sum - right_sum))
    return min_