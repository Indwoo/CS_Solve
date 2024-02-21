while (1):
    cnt = 0
    N = input()
    if(N=='0'):
        break
    num_list = list(map(int, str(N)))
    for i in range(len(num_list)//2):
        if (num_list[i] == num_list[len(num_list)-1-i]):
            cnt += 1
        else:
            break
    if cnt == len(num_list)//2:
        print("yes")
    else:
        print("no")