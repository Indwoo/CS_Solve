import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
check_list = [1]*N

for i in range(1,N):
    for j in range(i):
        if arr[i] > arr[j]:
            check_list[i] = max(check_list[i], check_list[j]+1)
            

print(max(check_list))