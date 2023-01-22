def solution(my_string, n):
    l = []
    for i in my_string:
        for j in range(n):
            l.append(i)
    return "".join(l)