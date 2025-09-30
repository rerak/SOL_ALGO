
n = int(input())
max_lst = []
max_len = 0

for j in range(1, n+1):
    nl = [n, j]
    i = 0

    while True:
        a = nl[i] - nl[i+1]
        i += 1
        if a < 0:
            break
        nl.append(a)
    if max_len < len(nl):
        max_len = len(nl)
        max_lst = nl[:]
print(max_len)
print(*max_lst)