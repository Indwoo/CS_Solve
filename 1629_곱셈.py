import sys

A, B, C = map(int, sys.stdin.readline().split())

C_mod = []

res = A ** B % C
for i in range(1,C):
    if A**i%C in C_mod:
        break
    else:
        C_mod.append(A**i%C)
    print(C_mod[i%len(C_mod)])
print(C_mod)
