N = int(input())
for i in range(N):
    print('*' * (i+1) + ' ' * (2*N - 2*i-2) + '*' * (i+1))

for j in range(1, N):
    print('*' * (N-j) + ' ' * (2*j) + '*' * (N-j))