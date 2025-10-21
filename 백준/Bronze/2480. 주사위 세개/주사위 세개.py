a, b, c = map(int, input().split())

if a != b != c and a != c:
    print(max(a, b, c) * 100)
elif a == b == c and a == c:
    print(10000 + (a * 1000))
elif a == b:
    print(1000 + a * 100)
elif a == c:
    print(1000 + a * 100)
elif c == b:
    print(1000 + c * 100)