import sys

N = int(sys.stdin.readline().strip())

for _ in range(N):
    clothes = {}
    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        name, type = sys.stdin.readline().strip().split()
        if type in clothes:
            clothes[type].append(name)
        else:
            clothes[type] = [name]

    cnt = 1
    
    for i in clothes:
        cnt *= (len(clothes[i]) + 1)
	
    print(cnt-1)