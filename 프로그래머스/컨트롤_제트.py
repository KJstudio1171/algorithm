def solution(s):
    num = []
    answer = 0
    s = s.split()
    for i in s:
        if i == 'Z':
            if num:
                answer -= num.pop()
        else:
            answer += int(i)
            num.append(int(i))
        
    return answer