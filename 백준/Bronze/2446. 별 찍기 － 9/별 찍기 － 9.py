N = int(input())
for i in range(N):
    print(' ' * i + '*' * (2*N-2*i-1))

for j in range(2, N+1):
    print(' '*(N-j) + '*' * (2*j-1))