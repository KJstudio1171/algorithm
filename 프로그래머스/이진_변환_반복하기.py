def solution(s):
    answer = 0
    n = 0
    while (s != "1"):
        answer += s.count("0")
        s = bin(len(s.replace('0', '')))[2:]
        n += 1
    return [n, answer]