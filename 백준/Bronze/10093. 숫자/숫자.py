
N, M = map(int, input().split())
ans = []
cnt = 0
if N <= M:
    for i in range(M-N-1):
        cnt += 1
    for i in range(N+1, M):
        ans.append(i)
if N >= M:
    for i in range(N-M-1):
        cnt += 1
    for i in range(M+1, N):
        ans.append(i)
print(cnt)
print(*ans)