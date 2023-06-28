def solution(myString, pat):
    l = []
    for i in myString:
        if i == 'A':
            l.append('B')
        else:
            l.append('A')
    return int(pat in ''.join(l))