import sys

def fib(n):
    memo = [1,1]
    for i in range(2,n):
        memo.append(0)
        
    return fib_action(memo, n-1)

def fib_action(memo, n):
    if memo[n] > 0: #수행한 적 있으면 바로 return
        return memo[n]

    memo[n] = fib_action(memo, n-1) + fib_action(memo, n-2)
    return memo[n]

N = int(sys.stdin.readline())
print(fib(N))