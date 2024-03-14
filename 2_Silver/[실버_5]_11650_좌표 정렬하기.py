import sys

N = int(sys.stdin.readline())
num_list=[]

for i in range(N):
    [a, b] = map(int, sys.stdin.readline().split())
    num_list.append([a, b])
    
num_list.sort()

for i in num_list:
    print(i[0], i[1])