import sys

my_queue = []

N = int(sys.stdin.readline())
count = 0

for i in range(N):
    
    cmnd = sys.stdin.readline().split()
    
    if(cmnd[0]) == 'push':
        my_queue.append(cmnd[1])
        
    elif(cmnd[0]) == 'pop':
        if len(my_queue)-count == 0:
            print("-1")
        else:
            print(my_queue[count])
            count+=1
        
    elif(cmnd[0]) == 'size':
        print(len(my_queue)-count)
    
    elif(cmnd[0]) == 'empty':
        if(len(my_queue)-count == 0):
            print("1")
        else:
            print("0")
            
    elif(cmnd[0]) == 'front':
        if len(my_queue)-count == 0:
            print("-1")
        else:
            print(my_queue[count])
        
    else:
        if len(my_queue)-count == 0:
            print("-1")
        else:
            print(my_queue[-1])
        