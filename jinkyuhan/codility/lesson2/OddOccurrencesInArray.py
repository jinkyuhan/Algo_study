def solution(A):
    cnt = {}
    for num in A:
        key_ = str(num)
        if not (key_ in cnt):
            cnt[key_] = 1
        else:
            cnt[key_] += 1
    result = list(cnt.items())
    for item in result:
        if item[1] % 2 == 1:
            return int(item[0])