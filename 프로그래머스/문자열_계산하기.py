def solution(my_string):
    op = 1
    answer = 0
    for i in my_string.split():
        if i.isnumeric():
            if op:
                answer += int(i)
            else:
                answer -= int(i)
        else:
            if i == '+':
                op = 1
            else:
                op = 0    
    return answer