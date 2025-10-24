
A = 9
arr = []
B = 0
for _ in range(A):
    N = int(input())
    B += N
    arr.append(N)
arr.sort()

brr= []

result = 0
for i in range(A):
    for j in range(i+1, A):
        if(len(brr)==2):
            continue
        if B - arr[i] - arr[j] == 100:
            brr.append(arr[i])
            brr.append(arr[j])

for a in arr:
    if a in brr:
        continue
    print(a)