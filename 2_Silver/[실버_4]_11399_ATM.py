import sys
N = int(sys.stdin.readline())
ATM = list(map(int, sys.stdin.readline().split()))
ATM = sorted(ATM)
cnt = 0
total = 0
for i in ATM:
    cnt += i
    total += cnt
print(total)