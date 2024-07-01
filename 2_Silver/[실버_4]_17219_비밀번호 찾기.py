import sys
pas_list = {}

N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    key, value = map(str, sys.stdin.readline().split())
    pas_list[key] = value

for _ in range(M):
    password = sys.stdin.readline().rstrip()
    print(pas_list[password])