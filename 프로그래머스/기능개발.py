def solution(progresses, speeds):
    complete_list = []
    max_date = 0
    for i in zip(progresses,speeds):
        if (100 - i[0]) % i[1] == 0 :
            complete_list.append((100 - i[0]) // i[1])
        else :
            complete_list.append((100 - i[0]) // i[1] + 1)
    answer = []
    for i in complete_list:
        if i > max_date:
            max_date = i
            answer.append(1)
        else:
            answer[-1] += 1
    return answer