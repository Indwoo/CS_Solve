N = int(input())

for i in range(N):
    
    k = int(input())
    n = int(input())
    
    floor = [i for i in range(1, n+1)]
    
    for j in range(k):
        for n_room in range(1, n):
            floor[n_room] += floor[n_room-1]
            
    print(floor[-1])