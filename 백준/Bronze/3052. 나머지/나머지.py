
arr = []
brr = []
for _ in range(10):
    a = int(input())
    arr.append(a)

for i in range(10):
    b = arr[i] % 42
    brr.append(b)

brr.sort()
cnt = 1
for j in range(9):
    if brr[j] != brr[j+1]:
        cnt += 1

print(cnt)