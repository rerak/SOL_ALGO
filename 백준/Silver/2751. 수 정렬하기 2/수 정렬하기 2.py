N = int(input())
arr = []
for _ in range(N):
    a = int(input())

    arr.append(a)
arr.sort()

for b in arr:
    print(b)