def solution(A):
    min_value = A[0]
    min_idx = 0
    for i in range(len(A)):
        if min_value > A[i]:
            min_value = A[i]
            min_idx = i
    max_profit = 0
    for j in range(min_idx, len(A)):
        max_profit = max(max_profit, A[j]-min_value)
    
    return max_profit
