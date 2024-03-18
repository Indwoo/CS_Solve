import sys

N = int(sys.stdin.readline())

for _ in range(N):
    stack_list = []
    num_list = input()
    for i in num_list:
        if i == '(':
            stack_list.append(i)
        elif i == ')':
            if stack_list:
                stack_list.pop()
            else:
                print('NO')
                break
    else:
        if not stack_list:
            print('YES')
        else:
            print('NO')