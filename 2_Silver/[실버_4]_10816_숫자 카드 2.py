import sys
from collections import Counter

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

card_cnt = Counter(card)
for i in target:
    print(card_cnt[i], end = ' ')