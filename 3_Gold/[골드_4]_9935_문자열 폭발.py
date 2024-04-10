N = input()
bomb = list(input())
stack = []

for i in N:
    stack.append(i)
    if len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')
    