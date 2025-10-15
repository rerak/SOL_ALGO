
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    speed = 0
    distance = 0

    for _ in range(N):
        arr = list(map(int, input().split()))

        if arr[0] == 0:   # 유지
            pass
        elif arr[0] == 1:  # 가속
            speed += arr[1]
        elif arr[0] == 2:  # 감속
            speed = max(0, speed - arr[1])

        distance += speed

    print(f"#{tc} {distance}")

