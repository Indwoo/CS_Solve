import sys

N = int(sys.stdin.readline())
stairs = []
max_list = []
cnt = 0

for i in range(N):
    stairs.append(int(sys.stdin.readline()))

stairs = list(reversed(stairs))
stairs.append(0)
max_list.append(stairs[0])
i = 0
while (i <= len(stairs)):
    if stairs[i+1] > stairs[i+2]:
        max_list.append(stairs[i+1])
        i = stairs.index(stairs[i+1])
        print(max_list)
    else:
        max_list.append(stairs[i+2])
        i = stairs.index(stairs[i+2])
        print(max_list)
