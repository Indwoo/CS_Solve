import sys
import math

N = int(sys.stdin.readline())
if(N ==0):
    print(0)
    exit()
    
jsoc = math.floor((N*0.15)+0.5)
sum_list = []

for i in range(N):
    sum_list.append(int(sys.stdin.readline()))
    
sum_list.sort()
sum_lst = sum(sum_list)
count = 0
for i in range(jsoc):
    sum_lst -= sum_list[i]
    sum_lst -= sum_list[-(i+1)]
    count += 2
print(math.floor((sum_lst / (len(sum_list)-count))+0.5))