N = int(input())
X = 0
cnt = 0
stop = 0

for i in range(1000000000):
    stop += i
    cnt = stop*6+1  
    if N <= cnt:
        print(i+1)
        break
