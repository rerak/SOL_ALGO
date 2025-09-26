
def hamsu(small, big):
    total = 0
    a = len(small)
    b = len(big)
    for i in range(b-a+1):
        cnt = 0
        for j in range(a):
            cnt += small[j] * big[i+j]
        total = max(total, cnt)
    return total

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if M > N:
        max_cnt = hamsu(A, B)
    else:
        max_cnt = hamsu(B, A)
    print(f"#{tc} {max_cnt}")