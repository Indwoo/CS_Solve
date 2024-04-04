import sys

N = int(sys.stdin.readline())
stk_list = []   # 10 3 6 8 7 5 2 1
is_stack = []   #
answer = []
rsp = 0

for i in range(N):
    stk_list.append(int(sys.stdin.readline().rstrip()))

for i in range(1, N+1):

    if i <= stk_list[rsp]:
        is_stack.append(i)
        answer.append("+")
    
    while len(is_stack) != 0 and is_stack[-1] == stk_list[rsp] and rsp != N:
        is_stack.pop()
        rsp+=1
        answer.append("-")

if len(answer) == N*2:
    for i in answer:
        print(i , end="\n")
else:
    print("NO")