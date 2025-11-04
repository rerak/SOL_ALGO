from collections import deque

def find_next_fish(sr, sc):
    dist = [[-1] * N for _ in range(N)]
    min_dist = float('inf')

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    q = deque()
    q.append((sr, sc))
    dist[sr][sc] = 0

    new_fish_lst = []

    while q:
        r, c = q.popleft()

        if dist[r][c] >= min_dist:
            continue

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if arr[nr][nc] > size or dist[nr][nc] != -1:
                continue

            new_dist = dist[r][c] + 1
            dist[nr][nc] = new_dist
            q.append((nr, nc))

            if arr[nr][nc] <= 0 or arr[nr][nc] >= size:
                continue

            min_dist = min(min_dist, new_dist)
            new_fish_lst.append((new_dist, nr, nc))

    best_fish_lst = [fish for fish in new_fish_lst if fish[0] == min_dist]

    if not best_fish_lst:
        return None, None, None

    best_fish_lst.sort()
    return best_fish_lst[0][1], best_fish_lst[0][2], best_fish_lst[0][0]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

curr_r, curr_c, size = 0, 0, 2
for r in range(N):
    for c in range(N):
        if arr[r][c] == 9:
            curr_r, curr_c = r, c
            arr[r][c] = 0

total_time = 0
eat_cnt = 0

while True:
    next_r, next_c, min_d = find_next_fish(curr_r, curr_c)
    if next_r is None:
        break

    total_time += min_d
    curr_r, curr_c = next_r, next_c

    arr[curr_r][curr_c] = 0
    eat_cnt += 1

    if eat_cnt == size:
        size += 1
        eat_cnt = 0

print(total_time)