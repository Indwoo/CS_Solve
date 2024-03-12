import sys
from collections import Counter

N = int(sys.stdin.readline())
num_list=[]

for i in range(N):
    x = int(sys.stdin.readline())
    num_list.append(x)

num_list=sorted(num_list)

print(round(sum(num_list) / N))

print(num_list[N//2])

cnt_list = Counter(num_list).most_common()
if len(cnt_list) > 1 and cnt_list[0][1] == cnt_list[1][1]:
    print(cnt_list[1][0])
else:
    print(cnt_list[0][0])

print(max(num_list) - min(num_list))

