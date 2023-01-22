def solution(my_string):
    answer = 0
    l = list(my_string)
    for i,j in enumerate(l):
        if j.isalpha():
            l[i] = "_"
    for i in "".join(l).split("_"):
        if i:
            answer += int(i)
    return answer