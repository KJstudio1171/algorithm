def solution(dots):
    answer = 0
    dots.sort()
    row = dots[3][0] - dots[0][0]
    dots.sort(key = lambda x : x[1])
    col = dots[3][1] - dots[0][1]
    return row * col