import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    x = find(a)
    y = find(b)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

G = int(input())
P = int(input())

parent = [x for x in range(G+1)]

plane = 0
for _ in range(P):
    gate = int(input())
    if plane == P:  # 다 한 경우
        continue

    boarding_number = find(gate)

    if boarding_number == 0:
        break

    union(boarding_number, boarding_number-1)
    plane += 1

print(plane)