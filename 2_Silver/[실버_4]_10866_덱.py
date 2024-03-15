import sys
from collections import deque

my_deque = deque()

N = int(sys.stdin.readline())

for i in range(N):
    
    cmnd = sys.stdin.readline().split()
    
    if(cmnd[0]) == 'push_front':
        my_deque.appendleft(cmnd[1])
        
    elif(cmnd[0]) == 'push_back':
        my_deque.append(cmnd[1])
        
    elif(cmnd[0]) == 'pop_front':
        if len(my_deque) == 0:
            print("-1")
        else:
            pop_item = my_deque[0]
            del(my_deque[0])
            print(pop_item)
            
    elif(cmnd[0]) == 'pop_back':
        if len(my_deque) == 0:
            print("-1")
        else:
            pop_item = my_deque[-1]
            del(my_deque[-1])
            print(pop_item)
        
    elif(cmnd[0]) == 'size':
        print(len(my_deque))
    
    elif(cmnd[0]) == 'empty':
        if(len(my_deque) == 0):
            print("1")
        else:
            print("0")
            
    elif(cmnd[0]) == 'front':
        if(len(my_deque) == 0):
            print("-1")
        else:
            print(my_deque[0])
    else:
        if(len(my_deque) == 0):
            print("-1")
        else:
            print(my_deque[-1])
        