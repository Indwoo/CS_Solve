test_list = ['B','A','C']
result_list = []

for i in test_list:
    temp = i.replace("B", "BD")
    result_list.append(temp)
    
print(result_list)