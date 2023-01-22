def solution(record):
    answer = []
    nickName = {}
    for i in record:
        string = i.split()
        if string[0] == 'Enter' or string[0] == 'Change':
                nickName[string[1]] = string[2]
    for i in record:
        string = i.split()
        if string[0] == 'Enter':
            answer.append(nickName[string[1]] + '님이 들어왔습니다.')
        elif string[0] == 'Leave':
            answer.append(nickName[string[1]] + '님이 나갔습니다.')
    return answer