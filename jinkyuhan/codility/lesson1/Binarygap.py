def solution(N):
    bin_N = bin(N)[2:]
    one_pos = []
    for i in range(len(bin_N)):
        if bin_N[i] == '1':
            one_pos.append(i)
    if len(one_pos) < 2:
        print(0)
        return 0

    max_ = one_pos[1] - one_pos[0]
    for i in range(2, len(one_pos)):
        max_ = max(max_, one_pos[i] - one_pos[i-1])

    print(max_-1)


solution(15)
