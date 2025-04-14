T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    x, y = a, b
    while a%b != 0:
        a,b = b, a%break
  print(x*y//b)