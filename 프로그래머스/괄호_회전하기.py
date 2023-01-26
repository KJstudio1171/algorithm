def checker(s):
    stack = ['stack']
    for i in s:
        if i == '(':
            stack.append('(')
        elif i == '{':
            stack.append('{')
        elif i == '[':
            stack.append('[')
        elif i == ')':
            if stack[-1] != '(':
                return False
            stack.pop()
        elif i == '}':
            if stack[-1] != '{':
                return False
            stack.pop()
        elif i == ']':
            if stack[-1] != '[':
                return False
            stack.pop()
    if len(stack) == 1:
        return True
    else:
        return False
        

def solution(s):
    answer = 0
    for i,j in enumerate(s):
        if checker(s[i:]+s[:i]):
            answer += 1
    return answer