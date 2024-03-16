import sys
from itertools import combinations

N, K = map(int, sys.stdin.readline().split())
print(len(list(combinations(range(N), K))))