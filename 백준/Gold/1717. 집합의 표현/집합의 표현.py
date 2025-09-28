
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)
    if a != b:
        parent[b] = a

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
    k, s, g = map(int, input().split())

    if k == 0:
        union(s, g)
    else:
        if find(s) == find(g):
            print('YES')
        else:
            print('NO')