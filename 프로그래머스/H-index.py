def solution(citations):
    answer = 0
    for i,j in enumerate(sorted(citations)):
        if len(citations) - i >= j:
            answer = max(answer, j)
    return answer