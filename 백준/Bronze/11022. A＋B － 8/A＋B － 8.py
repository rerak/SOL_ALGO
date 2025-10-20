N = int(input())
for nc in range(1, N+1):
    A, B = map(int, input().split())

    print(f"Case #{nc}: {A} + {B} = {A+B}")