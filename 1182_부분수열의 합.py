import sys
from itertools import combinations

N, S = map(int, input().split())

total = 0

bubun = list(map(int, sys.stdin.readline().split()))

for i in reversed(range(N+1)):
    if i==0: break
    is_S = list(combinations(bubun, i))
    for s in is_S:
        if sum(s) == S:
            total += 1

print(total)