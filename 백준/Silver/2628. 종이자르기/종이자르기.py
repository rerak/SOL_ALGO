N, M = map(int, input().split())
K = int(input())

brr = [0, N]
crr = [0, M]
drr = []
err = []
for _ in range(K):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        brr.append(arr[1])
    else:
        crr.append(arr[1])

brr.sort(reverse=True)
crr.sort(reverse=True)

for i in range(len(brr)-1):
    drr.append(brr[i]-brr[i+1])

for j in range(len(crr)-1):
    err.append(crr[j]-crr[j+1])

max_cnt = 0
cnt = 0
for a in range(len(drr)):
    for b in range(len(err)):
        cnt = drr[a]*err[b]
        max_cnt = max(max_cnt, cnt)
print(max_cnt)
