
arr = []

for _ in range(5):
    a = int(input())
    arr.append(a)

brr = []
for i in arr:
    if i <= 40:
        i = 40
    brr.append(i)
cnt = 0
for j in brr:
    cnt += j

print(cnt // 5)
