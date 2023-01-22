def solution(s, n):
    answer = ""
    lower = 'abcdefghijklmnopqrstuvwxyz'
    for i in s:
        if i >= 'a' and i <= 'z':
            answer += lower[(ord(i) - ord('a') + n) % 26]
        elif i >= 'A' and i <= 'Z':
            answer += lower.upper()[(ord(i) - ord('A') + n) % 26]
        else:
            answer += i