import sys

scan = sys.stdin.readline


def solution(A, K):
    K = K % len(A)
    result = A[-K:] + A[:-K]
    return result


solution([1, 2, 3, 4], 4)
