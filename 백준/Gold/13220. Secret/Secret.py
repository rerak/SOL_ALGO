def is_same_password(a, b):

    if len(a) != len(b):
        return "NO"

    if ' '.join(map(str, b)) in ' '.join(map(str, a * 2)):
        return "YES"

    return "NO"

n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

print(is_same_password(arr, brr))