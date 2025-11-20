def rain():
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                arr[r][c] -= 1

from collections import deque
def find_safe():
    safe = 0
    visited = [[0] * N for _ in range(N)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] or arr[i][j] == 0:
                continue
            safe += 1
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                if not visited[r][c]:
                    visited[r][c] = 1
                    for dr, dc in delta:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < N and 0 <= nc < N:
                            if not visited[nr][nc] and arr[nr][nc]:
                                q.append((nr, nc))
    return safe

N = int(input())    # 2 ~ 100
arr = [list(map(int, input().split())) for _ in range(N)]
max_safe = 1
while 1:
    for i in range(N):
        if sum(arr[i]):
            break
    else:
        break
    rain()
    safe = find_safe()
    if safe > max_safe:
        max_safe = safe
print(max_safe)