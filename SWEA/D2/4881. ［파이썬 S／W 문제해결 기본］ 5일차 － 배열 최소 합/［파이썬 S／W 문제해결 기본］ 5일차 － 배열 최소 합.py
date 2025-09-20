
def dfs(depth, total, used):
    global min_sum

    if total >= min_sum:
        return

    if depth == N:
        min_sum = min(min_sum, total)
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            dfs(depth + 1, total + arr[depth][i], used)
            used[i] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = float('inf')
    used = [False] * N
    dfs(0, 0, used)
    print(f"#{tc} {min_sum}")