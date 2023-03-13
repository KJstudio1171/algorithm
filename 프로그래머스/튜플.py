from collections import defaultdict
def solution(s):
    answer = []
    d = defaultdict(int)
    for i in s.replace("{","").replace("}","").split(','):
        d[i] += 1
    for i in reversed(sorted(d.items(), key = lambda x : x[1])):
        answer.append(int(i[0]))
    return answer