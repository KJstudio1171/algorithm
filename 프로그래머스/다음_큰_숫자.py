def solution(n):
    i = 1
    while(bin(n)[2:].count('1') != bin(n + i)[2:].count('1')):
        i += 1
    return n + i