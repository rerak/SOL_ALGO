
N, M = map(int, input().split())
arr = []
visited = [False] * (N + 1)

def backtrack():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            backtrack()
            arr.pop()
            visited[i] = False
backtrack()
