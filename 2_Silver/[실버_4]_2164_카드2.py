from collections import deque

N = int(input())
card_list = deque(range(1, N+1))
index = 0

while len(card_list) > 1:
    if index % 2 == 0:
        card_list.popleft()
    else:
        card_list.append(card_list.popleft())
    index += 1

print(card_list[0])

# import queue

# N = int(input())
# card_list = []
# for i in range(1,N+1):
#     card_list.append(i)
# while(len(card_list)>1):
#     card_list.pop(0)
#     card_list.append(card_list.pop(0))
    
# print(card_list.pop())
