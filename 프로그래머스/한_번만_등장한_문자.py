def solution(s):
    answer = ''
    ascii = [0] * 256
    for i in s:
        ascii[ord(i)] += 1
    for i,j in enumerate(ascii):
        if j == 1:
            answer += chr(i)
    return answer