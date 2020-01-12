import sys
from math import exp

N = int(sys.stdin.readline())
words = sys.stdin.readline().split()[0]
expert = ""
beginner = ""
count_alp = [0 for _ in range(26)]

for char in words:
    index = ord(char) - 97
    count_alp[index] = count_alp[index] + 1

for _ in range(N // 2):
    # expert's pick
    expert_pick = words[-1]
    words = words[:-1]
    expert = expert + expert_pick
    index = ord(expert_pick) - 97
    count_alp[index] = count_alp[index] - 1

    # beginner's pick
    for i in range(26):
        beginner_pick = ""
        if count_alp[i] > 0:
            count_alp[i] = count_alp[i] - 1
            beginner_pick = chr(i + 97)
            beginner = beginner + beginner_pick
            index = words.rfind(beginner_pick)
            words = words[:index] + words[index+1:]
            break

if beginner < expert:
    print("DA")
else:
    print("NE")
print(beginner)
