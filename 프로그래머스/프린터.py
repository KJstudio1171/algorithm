def solution(priorities, location):
    answer = 0
    num = priorities[location]
    stack = list(enumerate(priorities))
    while stack:
        if stack[0][1] == max(stack, key = lambda x : x[1])[1]:
            if stack[0][0] == location and stack[0][1] == num:
                return answer + 1
            else:
                stack.pop(0)
                answer += 1
        else:
            stack = stack[1:] + stack[0:1]
    return answer