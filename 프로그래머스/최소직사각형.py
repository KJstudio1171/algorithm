def solution(sizes):
    w, h = 0, 0
    for i in sizes:
        w, h = max(w, max(i)), max(h, min(i))
    return w * h