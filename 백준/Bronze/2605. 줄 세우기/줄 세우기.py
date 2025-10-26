
N = int(input())
arr = list(map(int, input().split()))

brr = []

for i in range(1, N+1):
    brr.insert(arr[i-1], i)
brr.reverse()
print(*brr)