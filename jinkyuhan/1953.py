import sys

scan = sys.stdin.readline

n = int(scan())
haters = [[] for _ in range(n + 1)]
blue = []
white = []
for i in range(1, n + 1):
    haters[i] += list(map(int, scan().split()))[1:]
    if i in blue:
        blue.append(i)
        white += haters[i]
    else:
        white.append(i)
        blue += haters[i]

white = set(sorted(white))
blue = set(sorted(blue))

print(len(white))
for player in white:
    print(player, end=' ')
print()
print(len(blue))
for player in blue:
    print(player, end=' ')
