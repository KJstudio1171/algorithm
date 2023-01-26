def solution(sides):
    case1 = min(sides)
    case2 = sum(sides) - max(sides) - 1
    return case1 + case2