def number_of_num(num1, num2):
    if num1 < 10 :
        if num1 == num2:
            return 1
        else:
            return 0
    if num1 % 10 == num2 :
        return 1 + number_of_num(num1 // 10, num2)
    else:
        return 0 + number_of_num(num1 //10, num2)

def solution(i, j, k):
    answer = 0
    for l in range(i, j + 1):
        answer += number_of_num(l, k)
    return answer