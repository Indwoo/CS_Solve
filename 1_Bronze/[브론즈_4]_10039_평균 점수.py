N = []
for _ in range(5):
  X = int(input())
  if X>40:
    N.append(X)
  else:
    N.append(40)
print(sum(N)//5)