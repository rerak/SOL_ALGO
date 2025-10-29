H, W = map(int, input().split())
arr = [list(map(str,input().strip())) for _ in range(H)]

for i in range(H):
    cnt = -1
    for j in range(W):
        if arr[i][j] == 'c':
            cnt = 0
            arr[i][j] = cnt
        else:
            if cnt >= 0:
                cnt += 1
                arr[i][j] = cnt
            else:
                cnt = -1
                arr[i][j] = cnt

for x in arr:
    print(*x)
