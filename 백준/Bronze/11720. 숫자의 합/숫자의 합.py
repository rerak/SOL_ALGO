N = int(input())
arr = list(map(int, input()))

hap = 0
for i in range(N):
    hap += arr[i]

print(hap)