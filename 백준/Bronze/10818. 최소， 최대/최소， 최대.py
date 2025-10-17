N = int(input())
arr = list(map(int, input().split()))
arr.sort()
a = arr[0]
b = arr[N-1]

print(a, b)