def solution(X, Y, D):
    dist = Y-X
    return dist//D if dist % D == 0 else dist//D+1