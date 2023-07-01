def solution(my_string, s, e):
    answer = ''
    answer += my_string[0:s]
    answer += "".join(reversed(list(my_string[s:e+1])))
    if e + 1 < len(my_string):
        answer += my_string[e+1:]
    return answer