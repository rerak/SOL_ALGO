N, M = map(int, input().split())
arr = list(map(int, input().split()))

max_cnt = 0
cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for x in range(j+1, N):
            cnt = arr[i]+arr[j]+arr[x]
            if cnt <= M:
                max_cnt = max(max_cnt,cnt)
print(max_cnt)