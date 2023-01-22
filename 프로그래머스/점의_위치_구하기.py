def solution(dot):
    if dot[1] > 0 and dot[0] > 0:
        return 1
    elif dot[1] > 0 and dot[0] < 0:
        return 2
    elif dot[1] < 0 and dot[0] < 0:
        return 3
    else:
        return 4