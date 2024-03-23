import sys

N = int(sys.stdin.readline())
coordination = []

for i in range(N):
    coordination.append(list(map(int,sys.stdin.readline().split())))
    
coordination = sorted(coordination,key = lambda x:(x[1],x[0]))

for i in range(N):
    print(coordination[i][0],coordination[i][1])