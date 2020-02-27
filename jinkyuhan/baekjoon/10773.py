N = int(input())
total = []
for _ in range(N):
    num = int(input())
    if num == 0:
        total.pop()
    else:
        total.append(num)
print(sum(total))
