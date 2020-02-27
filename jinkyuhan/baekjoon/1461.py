import sys

N, M = list(map(int, sys.stdin.readline().split()))
books = list(map(int, sys.stdin.readline().split()))

plus = []
minus = []

plus.append(0)
minus.append(0)

for book in books:
    if book >= 0:
        plus.append(book)
    else:
        minus.append(abs(book))

plus.sort()
minus.sort()

farrer, closer = [plus, minus] if max(plus) > max(minus) else [minus, plus]

closer_first_visit = (len(closer)-1) % M
farrer_first_visit = (len(farrer)-1) % M
total_distance = 0

if len(farrer) == 1 or len(closer) == 1: # 책이 + or - 한쪽만 있는 경우
    for i in range(farrer_first_visit, len(farrer) - M, M):
        total_distance = total_distance + 2 * farrer[i]
    total_distance = total_distance + farrer[len(farrer)-1]
else: # 책이 + and - 양쪽 다 있는 경우
    for i in range(closer_first_visit, len(closer), M):
        total_distance = total_distance + 2 * closer[i]
    for i in range(farrer_first_visit, len(farrer) - M, M):
        total_distance = total_distance + 2 * farrer[i]
    total_distance = total_distance + farrer[len(farrer)-1]

print(total_distance)
    
