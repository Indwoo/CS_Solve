import sys

N, M = map(int, sys.stdin.readline().split())
pocket_dict = {}

for i in range(1, N+1):
    j = sys.stdin.readline().rstrip()
    pocket_dict[i] = j
    pocket_dict[j] = i

for i in range(M):
    result = sys.stdin.readline().rstrip()
    if result.isdigit():
        print(pocket_dict[int(result)])
    else:
        print(pocket_dict[result])