import sys

N, K = map(int,sys.stdin.readline().split())
idx = 0
array = list(range(1,N+1))
result = []

while len(array) != 0: 
    idx += (K-1)
    idx = idx % len(array)
    result.append(array.pop(idx))

print("<", end ='')
for i in range(len(result)):
    if i == len(result)-1:
        print(f'{result[i]}', end = '')
        break
    print(f'{result[i]}, ', end = '')

print(">", end = '')