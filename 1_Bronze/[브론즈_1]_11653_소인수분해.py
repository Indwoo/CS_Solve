N = int(input())
if N == 1:
    exit()
    
i = 2

while N >= 2:
    if N % i == 0:
        print(i)
        N = N / i
    else:
        i += 1
    