def solution(my_string):
    answer = ''
    for i in my_string:
        if ord(i) <= ord("z") and ord(i) >= ord("a"):
            answer += i.upper()
        else:
            answer += i.lower()
    return answer