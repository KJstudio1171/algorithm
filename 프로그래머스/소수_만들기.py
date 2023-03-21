from itertools import combinations

def isdecimal(num):
    if num == 1 or num == 2 or num == 3:
        return True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    c = [sum(i) for i in combinations(nums, 3)]
    answer = len([i for i in c if isdecimal(i)])
    return answer