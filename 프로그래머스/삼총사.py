import itertools
def solution(number):
    answer = 0
    test = itertools.combinations(number, 3)
    for i in test:
        if sum(i) == 0:
            answer += 1
    return answer