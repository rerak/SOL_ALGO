N = int(input())
arr = input()

x = 0
y = 0
for i in arr:
    if i == "A":
        x += 1
    else:
        y += 1

if x > y:
    print("A")
elif x < y:
    print("B")
else:
    print("Tie")