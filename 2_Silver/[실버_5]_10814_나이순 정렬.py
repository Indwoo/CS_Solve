import sys

N = int(sys.stdin.readline())
num_list=[]
for i in range(N):
    num_list.append(list(sys.stdin.readline().split()))

num_list = sorted(num_list, key=lambda x: int(x[0]))

for i in range(N):
    print(num_list[i][0], num_list[i][1])