N = int(input())
arr = list(map(int, input().split()))
M = max(arr)

total = 0
result = 0
for i in arr:
    total += i / M * 100

result = total / N
print(result)