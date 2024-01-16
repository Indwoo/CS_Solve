import sys

N, M = list(map(int, input().split()))

tree = list(map(int, input().split()))

max_tree = max(tree)
cutted_tree = 0


while(M>max_tree):
    

for i in range(max_tree):
    for j in tree:
        cutted_tree += j - max_tree
        if(cutted_tree < 0):
            cutted_tree = 0
            continue
    
print(cutted_tree)
