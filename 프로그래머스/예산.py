def solution(d, budget):
    for i,j in enumerate(sorted(d)):
        budget -= j
        if budget < 0:
            return i
    return len(d)