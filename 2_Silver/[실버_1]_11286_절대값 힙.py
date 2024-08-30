import sys
import heapq as hq

N = int(input())
my_heap=[]
for i in range(N):
    x = int(sys.stdin.readline())
    if x:
        hq.heappush(my_heap, (abs(x), x))
    else:
        if len(my_heap) >= 1:
            print(hq.heappop(my_heap)[1])
        else:
            print(0)