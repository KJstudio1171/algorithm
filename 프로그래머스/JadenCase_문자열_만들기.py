def solution(s):
    s = [i for i in s.lower().split(" ")]
    ret = []
    for i in s:
        if i:
            ret.append(i.replace(i[0], i[0].upper(), 1))
        else:
            ret.append("")
    return " ".join(ret)

print(solution("a   b"))