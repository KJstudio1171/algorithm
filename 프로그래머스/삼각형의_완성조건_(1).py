def solution(sides):
    sides.sort()
    return 1 + int(sides[0] + sides[1] <= sides[2])