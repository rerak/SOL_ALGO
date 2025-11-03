def cleaner(r, c, d):
    global cnt

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1

    check = 1
    for _ in range(4):
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        if not arr[nr][nc]:
            cleaner(nr, nc, d)
            check = 0
            return

    if check == 1:
        d = (d + 2) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        if arr[nr][nc] != 1:
            cleaner(nr, nc, (d+2)%4)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
cleaner(r, c, d)

print(cnt)