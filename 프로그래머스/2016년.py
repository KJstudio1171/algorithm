def solution(a, b):
    num = 0
    date = [31,29, 31, 30, 31,30,31,31,30,31,30,31]
    for i in range(a - 1):
        num += date[i]
    num += b
    num %= 7
    return ["THU","FRI","SAT","SUN", "MON","TUE","WED",][num]
print(solution(1,1))