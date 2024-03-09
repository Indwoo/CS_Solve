from collections import deque
import sys

N = int(sys.stdin.readline())
n_queue = deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    
    if command[0] == 'pop':
        if len(n_queue) == 0:
            print('-1')
        else:
            print(n_queue.popleft())
            
    elif command[0] == 'size':
        print(len(n_queue))
        
    elif command[0] == 'empty':
        if len(n_queue) == 0:
            print('1')
        else:
            print('0')
            
    elif command[0] == 'front':
        if len(n_queue) == 0:
            print('-1')
        else:
            print(n_queue[0])
            
    elif command[0] == 'back':
        if len(n_queue) == 0:
            print('-1')
        else:
            print(n_queue[-1])
            
    elif command[0] == 'push':
        n_queue.append(int(command[1]))