N = int(input())
for i in range(N):
    print(' '*(N-i-1) + '*' * (2*i+1))

for j in range(1, N):
    print(' '* j + ('*' * (2*(N-j)-1)))