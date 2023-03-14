def solution(elements):
    l = elements + elements
    s = set()
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            s.add(sum(l[j : j + i]))
    answer = len(s)
    return answer