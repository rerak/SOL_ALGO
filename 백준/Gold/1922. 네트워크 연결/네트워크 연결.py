
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)
    if a != b:
        parent[b] = a

N = int(input())
M = int(input())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()
parent = [i for i in range(N+1)]
mst_cnt = 0

for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        mst_cnt += c

print(mst_cnt)