a, b, c, d, e = map(int, input().split())

result = a**2 + b**2 + c**2 + d**2 + e**2
sol = result % 10

print(sol)