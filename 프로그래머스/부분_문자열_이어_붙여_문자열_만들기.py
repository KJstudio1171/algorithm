def solution(my_strings, parts):
    answer = ''
    for i,v in enumerate(my_strings):
        tmp = parts[i]
        answer += v[tmp[0]:tmp[1] + 1]
    return answer