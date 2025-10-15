
T = int(input())
day_ends = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())

    start = sum(day_ends[:m1])+d1
    
    end = sum(day_ends[:m2]) + d2

    result = end - start + 1
    print(f"#{tc} {result}")