N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_result = float('-inf')
min_result = float('inf')

def dfs(nums, operators, index, total):
    global max_result, min_result
    
    if index == len(nums):
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return
    
    if operators[0] > 0:
        operators[0] -= 1
        dfs(nums, operators, index+1, total + nums[index])
        operators[0] += 1
    if operators[1] > 0:
        operators[1] -= 1
        dfs(nums, operators, index+1, total - nums[index])
        operators[1] += 1
    if operators[2] > 0:
        operators[2] -= 1
        dfs(nums, operators, index+1, total * nums[index])
        operators[2] += 1
    if operators[3] > 0:
        operators[3] -= 1
        if total >= 0:
            dfs(nums, operators, index+1, total // nums[index])
        else:
            dfs(nums, operators, index+1, -(-total // nums[index]))
        operators[3] += 1

dfs(nums, operators, 1, nums[0])

print(max_result)
print(min_result)
