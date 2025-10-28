
arr = [list(map(int, input().split())) for _ in range(3)]

total = 0

for i in arr:
    cnt = 0
    for j in i:
        if j == 0:
            cnt += 1
    total = cnt

    if total == 1:
        print('A')
    elif total == 2:
        print('B')
    elif total == 3:
        print('C')
    elif total == 4:
        print('D')
    elif total == 0:
        print('E')
