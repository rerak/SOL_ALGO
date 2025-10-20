while True:
    check_list = list(map(int,input().split()))
    if check_list[0] == 0:
        break
    check_list.sort()
    if check_list[2]**2 == (check_list[0]**2)+(check_list[1]**2):
        print("right")
    else:
        print("wrong")