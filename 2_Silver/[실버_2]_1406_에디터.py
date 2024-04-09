import sys
left_str_list = list(map(str,sys.stdin.readline().strip()))
right_str_list = []

N = int(input())

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if left_str_list:
            right_str_list.append(left_str_list.pop())
            
    elif command[0] == 'D':
        if right_str_list:
            left_str_list.append(right_str_list.pop())
            
    elif command[0] == 'B':
        if left_str_list:
            left_str_list.pop()
    else:
        left_str_list.append(command[1])

        
left_str_list.extend(reversed(right_str_list))
print(''.join(left_str_list))
