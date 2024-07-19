import sys
import math

input = sys.stdin.readline

N = int(input())

shirt = list(map(int, input().split()))
T, P = map(int, input().split())

shirt_count = 0

for size in shirt:
    if size > 0:
        shirt_count += math.ceil(size / T)

print(shirt_count)
print(N // P, N % P)