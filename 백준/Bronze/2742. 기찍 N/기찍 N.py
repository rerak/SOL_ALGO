
N = int(input())
arr = []
for i in range(1, N+1):
    arr.append(i)

arr.sort(reverse=True)

for i in arr:
    print(i)