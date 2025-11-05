dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dust(arr):
    new_arr = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if (r, c) in position:
                new_arr[r][c] = -1
                continue
            spread = arr[r][c] // 5
            spread_cnt = 0
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue
                if new_arr[nr][nc] == -1:
                    continue
                new_arr[nr][nc] += spread
                spread_cnt += 1
            new_arr[r][c] += arr[r][c] - (spread * spread_cnt)
    return new_arr

def air(arr):
    upper_r = upper[0]
    for r in range(upper_r-1, 0, -1):
        arr[r][0] = arr[r-1][0]
    for c in range(C-1):
        arr[0][c] = arr[0][c+1]
    for r in range(upper_r):
        arr[r][C-1] = arr[r+1][C-1]
    for c in range(C-1, 0, -1):
        arr[upper_r][c] = arr[upper_r][c-1]
    arr[upper_r][1] = 0
    lower_r = lower[0]
    for r in range(lower_r+1, R-1):
        arr[r][0] = arr[r+1][0]
    for c in range(C-1):
        arr[R-1][c] = arr[R-1][c+1]
    for r in range(R-1, lower_r, -1):
        arr[r][C-1] = arr[r-1][C-1]
    for c in range(C-1, 0, -1):
        arr[lower_r][c] = arr[lower_r][c-1]
    arr[lower_r][1] = 0
    return arr

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
position = []
for r in range(R):
    for c in range(C):
        if A[r][c] == -1:
            position.append((r, c))
upper, lower = position[0], position[-1]
arr = A
for _ in range(T):
    arr = dust(arr)
    arr = air(arr)
result = 0
for r in range(R):
    for c in range(C):
        if arr[r][c] != -1:
            result += arr[r][c]
print(result)