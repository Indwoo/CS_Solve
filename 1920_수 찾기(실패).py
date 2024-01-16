import sys

def is_in(N : list, X):
    if X == N[len(N)//2]:
        print("1")
    elif X > N[len(N)//2]:
        is_in(N[(len(M)/2)+1:len(M)], X)
    elif X > N[len(N)//2]:
        is_in(N[0:(len(M)/2)-1], X)
    else:
        print("0")
        

N = int(sys.stdin.readline())
A = list(map(int, input().split()))
M = int(sys.stdin.readline())
X = list(map(int, input().split()))
for i in X:
    is_in(M, X)