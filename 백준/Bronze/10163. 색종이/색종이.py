N = int(input()) # 색종이 갯수
arr = [[0]*1001 for _ in range(1001)]
for t in range(1, N+1):
    a, b, c, d = map(int, input().split())
    for i in range(b, b+d):
        for j in range(a, a+c):
            arr[i][j] = t
cnt = [0] * (N+1)
for lst in arr:
    for n in lst:
        cnt[n] += 1
print(*cnt[1:], sep='\n')