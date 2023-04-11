def dfs(numbers,target):
    if sum(numbers) < abs(target):
        return 0
    if len(numbers) == 1:
        if abs(target) == abs(numbers[0]):
            return 1
        return 0
    return dfs(numbers[1:], target - numbers[0]) + dfs(numbers[1:], target + numbers[0])

def solution(numbers, target):
    answer = dfs(numbers, target)
    return answer