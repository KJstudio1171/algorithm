def solution(n, left, right):
    answer = []
    i_left = left // n
    j_left = left % n
    i_right = right // n
    j_right = right % n
    
    for i in range(i_left, i_right + 1):
        for _ in range(i + 1):
            answer.append(i + 1)
        for j in range(i + 2, n + 1):
            answer.append(j)
    return answer[j_left : j_left + right - left + 1]