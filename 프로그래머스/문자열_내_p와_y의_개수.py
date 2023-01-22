def solution(s):
    (a, b) = (0, 0)
    for i in s.upper():
        if i in ['P', 'Y']:
            a += 1
        if i in ['p', 'P']:
            b += 1
    return a == b