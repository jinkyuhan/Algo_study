x, y, w, s = list(map(int, input().split()))
total_time = 0
# 대각선의 이동이 손해이기 때문에 항상 수직으로만 이동하는 경우
if s >= 2 * w:
    print((x + y) * w)
# 대각선의 이동이 경우에 따라서 이득인 경우
else:
    # 갈 수 있는데 까지는 대각선으로 이동
    total_time = total_time + min(x, y) * s
    if s >= w:
        print(abs(x-y) * w + total_time)
    else:
        print(abs(x-y) // 2 * s * 2 + abs(x-y) % 2 * w + total_time)
