
N = 5

arr = []
for _ in range(N):
    a = list(map(int, input().split()))
    for i in a:
        arr.append(i)
arr.sort()
cnt = 0
for j in arr:
    cnt += j
evg = cnt//N
cen = arr[N//2]

print(evg)
print(cen)