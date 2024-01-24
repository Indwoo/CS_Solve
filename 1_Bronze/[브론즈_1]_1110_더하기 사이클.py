N = int(input())
real = N
cnt = 0

while True:
    
    ten = real // 10
    one = real % 10
    
    next_one = (ten + one)%10
    
    real = (one * 10) + next_one
    
    cnt += 1
    if (real == N):
        break
    
print(cnt)
