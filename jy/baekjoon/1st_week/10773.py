import sys

k = int(input())
a = list(map(int, [sys.stdin.readline() for i in range(k)]))

stack = []
for i in a:
    if i != 0:
        stack.append(i)
    else:
        stack.pop()

print(sum(stack))

        