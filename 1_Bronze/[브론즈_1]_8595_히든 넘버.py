N = int(input())
hidden = input()
hidden_list = list(map(str, hidden))
int_list = []
answer = 0
x=0
is_int = False

for i in hidden_list:
    if i.isdigit() and is_int == False:
        is_int = True
        int_list.append(i)
    elif i.isdigit() and is_int == True:
        int_list.append(i)
    elif not(i.isdigit()) and len(int_list) != 0:
        is_int = False
        x = int(''.join(int_list))
        answer += x
        int_list=[]
    else:
        is_int = False
        int_list=[]
        
if len(int_list) != 0:
    x = int(''.join(int_list))
    answer += x
    print(answer)
else:
    print(answer)
        