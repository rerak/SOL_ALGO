def find_min_diff(cnt, idx):
    global min_diff

    if cnt == N//2:
        team_start = 0
        team_link = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team_start += S[i][j]
                elif not visited[i] and not visited[j]:
                    team_link += S[i][j]
        min_diff = min(min_diff, abs(team_start-team_link))
        return

    for n in range(idx, N):
        if not visited[n]:
            visited[n] = True
            find_min_diff(cnt+1, n+1)
            visited[n] = False


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
min_diff = float('inf')
find_min_diff(0, 0)

print(min_diff)