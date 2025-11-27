def next_move(d1, d2, i, move):
    global min_move

    if i == M:
        if move < min_move:
            min_move = move
        return
    if move >= min_move:
        return
    
    next_move(closet[i], d2, i+1, move + abs(d1-closet[i]))
    next_move(d1, closet[i], i+1, move + abs(d2-closet[i]))


N = int(input())   # 벽장의 개수 3~20
d1, d2 = map(int, input().split())  # 열려있는 두개의 벽장
# doors = list(map(int, input().split()))
M = int(input())    # 사용할 벽장 순서 길이
closet = [int(input()) for _ in range(M)]   # 사용할 벽장 번호

min_move = float('inf')
next_move(d1, d2, 0, 0)
print(min_move)