
arr = [[0] * 100 for _ in range(100)]

N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    A1, B1 = A+10, B+10


    for i in range(A, A1):
        for j in range(B, B1):
            arr[i][j] = 1
cnt = 0
for a in arr:
    for b in a:
        if b == 1:
            cnt += 1
print(cnt)