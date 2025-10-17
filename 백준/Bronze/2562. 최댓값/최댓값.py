
result = []

for i in range(9):
    arr = int(input())
    result.append((arr, i+1))

a = max(result)

print(a[0])
print(a[1])