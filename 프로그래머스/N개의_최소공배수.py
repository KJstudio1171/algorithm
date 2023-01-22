def GCD(num1, num2):
    while(num1 % num2):
        num1, num2 = num2, num1 % num2
    return num2

def solution(arr):
    answer = 1
    for i in range(len(arr)):
        j = i + 1
        while (j < len(arr)):
            temp = GCD(arr[i], arr[j])
            if temp != 1:
                arr[j] = arr[j] // temp
            j = j + 1
    for i in arr:
        answer *= i
    return answer