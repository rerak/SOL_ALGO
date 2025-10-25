
def count(arr):
    cnt = 0
    for lst in arr:
        for i in range(1, len(lst)):
            if lst[i-1] !=lst[i]:
                cnt+=1
    return cnt


arr = [[0] * 102 for _ in range(102)]
N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    A1, B1 = A+10, B+10

    for i in range(A, A1):
        for j in range(B, B1):
            arr[i][j] = 1

arr_t = list(zip(*arr))
ans = count(arr) + count(arr_t)

print(ans)