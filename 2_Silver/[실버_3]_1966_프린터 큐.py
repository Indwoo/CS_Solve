from collections import deque

N = int(input())

for i in range(N):
    M, K = map(int, input().split())
    print_list = deque(list(map(int, input().split())))
    cnt = 0
    
    while print_list:
        max_value = max(print_list)
        front = print_list.popleft()
        K -= 1
        if front == max_value:
            cnt += 1
            if K < 0:
                print(cnt)
                break
        else:
            print_list.append(front)
            if K < 0:
                K = len(print_list) - 1
            