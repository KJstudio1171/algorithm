def solution(t, p):
    answer = 0
    num_p = int(p)
    len_p = len(p)
    len_t = len(t)
    for i in range(len_t - len_p + 1):
        if int(t[i:i + len_p]) <= num_p:
            answer += 1
    return answer