# 애초에 가능한 input 인지 검사
def is_promise(key, lock):
    lock_hole_count = 0
    for row in lock:
        lock_hole_count += row.count(0)

    key_spin_count = 0
    for row in key:
        key_spin_count += row.count(1)

    # 만약 lock 의 구멍 수보다 key 의 돌기 수가 작으면 무조건 실패
    if lock_hole_count > key_spin_count:
        return False

    return True


# key 를 우측 90도 회전
def rotate_matrix(size, matrix):
    result = [[-1 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[j][size - 1 - i] = matrix[i][j]
    return result


# key 와 lock 을 바탕으로 background 를 그림
def draw_background(key, key_start, lock):
    key_size = len(key)
    lock_size = len(lock)
    bg_size = 2 * key_size + lock_size - 2
    background = [[0 for _ in range(bg_size)] for _ in range(bg_size)]
    lock_start = key_size - 1
    for i in range(lock_size):
        for j in range(lock_size):
            background[lock_start + i][lock_start + j] += lock[i][j]
    for i in range(key_size):
        for j in range(key_size):
            background[key_start[0] + i][key_start[1] + j] += key[i][j]
    return background


# 그려진 background 를 바탕으로 자물쇠 잠금해제 가능여부 판독
def can_open(key, lock, background):
    key_size = len(key)
    lock_size = len(lock)
    lock_start = key_size - 1
    lock_end = lock_size + key_size - 1
    for i in range(lock_start, lock_end):
        for j in range(lock_start, lock_end):
            if background[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = True
    if not is_promise(key, lock):
        return False
    n, m = [len(lock), len(key)]
    for _ in range(4):
        key = rotate_matrix(m, key)
        for i in range(n + m - 1):
            for j in range(n + m - 1):
                key_start = (i, j)
                background = draw_background(key, key_start, lock)
                if can_open(key, lock, background):
                    # print(answer)
                    return answer
    answer = False
    # print(answer)
    return answer


if __name__ == "__main__":
    solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
