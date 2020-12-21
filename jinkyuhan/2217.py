import sys

N = int(sys.stdin.readline())
ropes = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse = True)

max_weight = -1
for k in range(N):
    max_weight = max(max_weight, (k+1) * ropes[k])

print(max_weight)