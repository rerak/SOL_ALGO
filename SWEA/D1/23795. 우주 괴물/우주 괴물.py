
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                for di, dj in delta:
                    for k in range(1, N):
                        ni, nj = di * k + i, dj * k + j
                        if not (0<= ni < N and 0<= nj < N):
                            break
                        if arr[ni][nj] == 1:
                            break
                        if arr[ni][nj] == 0:
                            arr[ni][nj] = 1

    cnt = 0
    for q in arr:
        for p in q:
            if p == 0:
                cnt += 1

    print(f"#{tc} {cnt}")