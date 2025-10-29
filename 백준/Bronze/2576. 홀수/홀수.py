
N = 7
ans = []
for _ in range(N):
    arr = list(map(int, input().split()))

    for i in arr:
        if i % 2 == 1:
            ans.append(i)

if not ans:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))