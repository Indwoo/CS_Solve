N = [i for i in range(1,31)]

for _ in range(28):
    submit = int(input())
    N.remove(submit)

print(min(N))
print(max(N))