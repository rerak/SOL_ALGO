def find_max_cnt(r, c, way):
    global cnt

    if r == N-1 and c == N-1:
        cnt += 1
        return

    if way == 0:
        if c == N-1:
            return
        if 0 <= r < N and 0 <= c+1 < N and arr[r][c+1] == 0:
            find_max_cnt(r, c+1, 0)
        if 0 <= r+1 < N and 0 <= c+1 < N and arr[r+1][c+1] == 0:
            if arr[r][c+1] == 0 and arr[r+1][c] == 0:
                find_max_cnt(r+1, c+1, 2)

    elif way == 1:
        if r == N-1:
            return
        if 0 <= r+1 < N and 0 <= c < N and arr[r+1][c] == 0:
            find_max_cnt(r+1, c, 1)
        if 0 <= r+1 < N and 0 <= c+1 < N and arr[r+1][c+1] == 0:
            if arr[r][c+1] == 0 and arr[r+1][c] == 0:
                find_max_cnt(r+1, c+1, 2)

    elif way == 2:
        if 0 <= r < N and 0 <= c+1 < N and arr[r][c+1] == 0:
            find_max_cnt(r, c+1, 0)
        if 0 <= r+1 < N and 0 <= c < N and arr[r+1][c] == 0:
            find_max_cnt(r+1, c, 1)
        if 0 <= r+1 < N and 0 <= c+1 < N and arr[r+1][c+1] == 0:
            if arr[r][c+1] == 0 and arr[r+1][c] == 0:
                find_max_cnt(r+1, c+1, 2)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
find_max_cnt(0, 1, 0)
print(cnt)