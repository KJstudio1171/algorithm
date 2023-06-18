import math


def solution(num_list):
    answer = int(math.prod(num_list) < sum(num_list) ** 2)
    return answer
