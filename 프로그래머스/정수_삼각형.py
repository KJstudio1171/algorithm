def solution(triangle):
    for i,j in enumerate(triangle):
        if i<1:
            continue
        for index, num in enumerate(j):
            if index == 0:
                j[index] += triangle[i - 1][0]
            elif index == len(j) - 1:
                j[index] += triangle[i - 1][-1]
            else:
                j[index] += max(triangle[i - 1][index - 1], triangle[i - 1][index])
            
    return max(triangle[-1])