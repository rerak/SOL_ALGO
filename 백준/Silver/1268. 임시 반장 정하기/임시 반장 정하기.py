
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N
ans = 0

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for x in range(5):
            if arr[i][x] == arr[j][x]:
                visited[i] += 1
                break
# print(visited)
cnt = 0
max_cnt = 0
for y in range(N):
    cnt = visited[y]
    max_cnt = max(max_cnt, cnt)
print(visited.index(max_cnt)+1)