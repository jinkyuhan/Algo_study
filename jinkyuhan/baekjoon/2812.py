import sys

N, K = list(map(int, sys.stdin.readline().split()))
num = sys.stdin.readline().split()[0]
while K > 0:
    for i in range(len(num) - 1):
        if int(num[i + 1]) > int(num[i]):
            num = num[:i] + num[i + 1:]
            K = K - 1
            break
        if i == len(num)-2:
            num = num[:-K]
            K = 0
            break

print(num)
