def solution(s):
    i = 1
    answer = len(s)
    while i <= len(s) // 2:
        tmp = len(s)
        j = 0
        count = 1
        while(j < len(s) - 2 * i + 1):
            if s[j:j+i] == s[j+i:j+2*i]:
                count += 1
            else:
                if count != 1:
                    tmp = tmp - i * count + i + len(str(count))
                count = 1
            j += i
        if count != 1:
            tmp = tmp - i * count + i + len(str(count))
        i += 1
        answer = min(answer,tmp)
    return answer