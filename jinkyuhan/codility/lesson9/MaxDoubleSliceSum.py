def solution(A):
    if len(A) < 4:
        return 0
    left_max = [0 for _ in range(len(A))]
    right_max = [0 for _ in range(len(A))]
    for i in range(len(A)):
        left_max[i] = max(0, left_max[i] +A[i])
        