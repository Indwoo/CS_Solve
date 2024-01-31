import sys
sys = sys.stdin
cnt = 0

N,K = map(int, sys.readline().split())
arr=[[0] * (K+1) for _ in range(N+1)]
cost=[[0,0]]

for i in range(N):
    cost.append(list(map(int,sys.readline().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = cost[i][0]
        value = cost[i][1]
        
        if j < weight:
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-weight]+value)
        
print(arr[-1][-1])