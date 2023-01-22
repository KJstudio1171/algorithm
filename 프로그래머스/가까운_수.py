def solution(array, n):
    answer = 1000
    min = 1000
    for i in sorted(array):
        if abs(i - n) < min:
            answer = i
            min = abs(i - n) 
    return answer