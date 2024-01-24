king = 0
n = list(range(10))
king_index = 0
for i in range(9):
    n[i] = int(input())
for i in range(9):
    if king <= n[i]:
        king = n[i]
        king_index = n.index(king)+1
print(king)
print(king_index)
