import sys
seven_knights = list(int(sys.stdin.readline()) for i in range (9))
red_one = 0
red_two = 0

for i in range(9):
    for j in range(i+1,9,1):
        if((sum(seven_knights) - seven_knights[i] - seven_knights[j])==100):
            red_one = seven_knights[i]
            red_two = seven_knights[j]
            break

seven_knights.remove(red_one)
seven_knights.remove(red_two)

for i in sorted(seven_knights):
    print(i)