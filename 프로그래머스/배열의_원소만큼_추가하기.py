def solution(arr):
    answer = []
    for i in arr:
        answer = answer + [i] * i
    return answer