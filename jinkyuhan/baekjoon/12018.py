import sys


class Course:
    def __init__(self):
        self.P = 0
        self.L = 0
        self.mileages = []


N, M = list(map(int, sys.stdin.readline().split()))
courses = [Course() for _ in range(N)]
count = 0

for c in courses:
    c.P, c.L = list(map(int, sys.stdin.readline().split()))
    c.mileages = list(map(int, sys.stdin.readline().split()))
    c.mileages.sort()

#  신청인원 < 정원

if len(courses) > 0:
    for c in courses:
        if M < 1:
            break
        if c.P < c.L:
            M = M - 1
            count = count + 1
            courses.remove(c)

if len(courses) > 0:
    # 신청인원 == 정원
    for c in sorted(courses, key=lambda x: x.mileages[0]):
        if M < c.mileages[0]:
            break
        if c.P == c.L:
            M = M - c.mileages[0]
            count = count + 1
            courses.remove(c)

if len(courses) > 0:
    # 신청인원 > 정원
    for c in sorted(courses, key=lambda x: x.mileages[c.P - c.L + 1]):
        if M < c.mileages[c.P - c.L + 1]:
            break
        if c.P > c.L:
            M = M - c.mileages[c.P - c.L + 1]
            count = count + 1

print(count)
