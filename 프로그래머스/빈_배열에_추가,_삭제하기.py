def solution(arr, flag):
    answer = []
    for i,v in enumerate(flag):
        if v == True:
            for j in range(arr[i] * 2):
                answer.append(aarr[i])
        else:
            answer = answer[0:-arr[i]]
    return answer