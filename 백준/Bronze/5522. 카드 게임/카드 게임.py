arr = []
for _ in range(5):
    a = int(input())
    arr.append(a)

cnt = 0
for i in arr:
    cnt += i

print(cnt)