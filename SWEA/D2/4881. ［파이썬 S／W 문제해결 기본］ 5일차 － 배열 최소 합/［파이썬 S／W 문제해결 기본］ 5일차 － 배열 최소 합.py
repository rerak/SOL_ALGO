def backtrack(idx, total):
    global min_sum

    if total >= min_sum:
        return

    if idx == N:
        min_sum = min(min_sum, total)
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = True
            backtrack(idx + 1, total + arr[idx][j])
            visited[j] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')
    visited = [False] * N
    backtrack(0, 0)

    print(f"#{tc} {min_sum}")