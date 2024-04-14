import sys

N = int(sys.stdin.readline())
got_cards = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
unkwon_cards = list(map(int, sys.stdin.readline().split()))

card_dict = {}

for i in range(len(got_cards)):
    card_dict[got_cards[i]] = i

for i in range(M):
    if unkwon_cards[i] in card_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')