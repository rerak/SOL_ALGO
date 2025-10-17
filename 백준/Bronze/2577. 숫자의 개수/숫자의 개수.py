a = int(input())
b = int(input())
c = int(input())

result = a * b * c

x = str(result)

val = [0] * 10
for i in x:

    for j in range(0, 10):
        if int(i) == j:
            val[j] += 1

for x in val:
    print(x)