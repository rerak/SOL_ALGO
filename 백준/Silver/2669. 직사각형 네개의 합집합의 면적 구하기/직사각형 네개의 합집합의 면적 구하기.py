box = [[0] * 101 for _ in range(101)]
max_size =0
for _ in range(4):
    r1, c1, r2, c2 = map(int, input().split())

    for i in range(r1, r2):
        for j in range(c1, c2):
            box[i][j] = 1


    size = 0
    for i in range(101):
        for j in range(101):
            size += box[i][j]
    max_size = max(max_size, size)
print(max_size)