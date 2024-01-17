import sys
import heapq as hq

n = int(input())
my_heap=[]
for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        hq.heappush(my_heap, (-x, x))
    else:
        if len(my_heap) >= 1:
            print(hq.heappop(my_heap)[1])
        else:
            print(0)