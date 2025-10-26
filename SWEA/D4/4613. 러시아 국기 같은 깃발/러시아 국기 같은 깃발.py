
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    total = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for x in range(i+1):
                cnt += arr[x].count('W')
            for x in range(i+1, j+1):
                cnt += arr[x].count('B')
            for x in range(j+1, N):
                cnt += arr[x].count('R')
            total = max(total, cnt)
    print(f"#{tc} {N*M -total}")