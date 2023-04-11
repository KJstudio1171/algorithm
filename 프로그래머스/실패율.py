def solution(N, stages):
    answer = []
    failRatio = [0.0] * N
    challenger = len(stages)
    stages.sort()
    index = 0
    numIndex = 0
    for i in stages:
        if index == i - 1:
            numIndex += 1
        else:
            if i == N + 1:
                break
            failRatio[index] = numIndex / challenger
            challenger -= numIndex
            index = i - 1
            numIndex = 1
    failRatio[index] = numIndex / challenger
    for i in sorted(enumerate(failRatio), key = lambda x : x[1], reverse = True):
        answer.append(i[0] + 1)
    return answer