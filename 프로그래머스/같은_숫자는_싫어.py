def solution(arr):
    ret = []
    for i in arr:
        if not ret:
            ret.append(i)
        elif ret[-1] != i:
            ret.append(i)
    return ret