import sys

my_stack = []

N = int(sys.stdin.readline())

for i in range(N):
    
    cmnd = sys.stdin.readline().split()
    
    if(cmnd[0]) == 'push':
        my_stack.append(cmnd[1])
        
    elif(cmnd[0]) == 'pop':
        if len(my_stack) == 0:
            print("-1")
        else:
            pop_item = my_stack[len(my_stack)-1]
            del(my_stack[len(my_stack)-1])
            print(pop_item)
        
    elif(cmnd[0]) == 'size':
        print(len(my_stack))
    
    elif(cmnd[0]) == 'empty':
        if(len(my_stack) == 0):
            print("1")
        else:
            print("0")
            
    else:
        if(len(my_stack) == 0):
            print("-1")
        else:
            print(my_stack[len(my_stack)-1])
        