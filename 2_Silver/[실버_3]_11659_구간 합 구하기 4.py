import sys

N, M = map(int, sys.stdin.readline().split())
sum_list = list(map(int, sys.stdin.readline().split()))
pre_sum = [0]

range_sum = 0
for i in sum_list:
    range_sum += i
    pre_sum.append(range_sum)
    
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(pre_sum[j] - pre_sum[i-1])