
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))[1:]

    N = len(arr)
    num = 0
    for i in range(1, N):
        for j in range(i):
            if arr[i] < arr[j]:
                num += 1
    print(f"{tc} {num}")