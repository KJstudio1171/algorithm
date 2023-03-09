def solution(quiz):
    answer = []
    for i in quiz:
        l = i.split(" = ")
        if int(l[1]) == eval(l[0]) :
            answer.append("O")
        else :
            answer.append("X")
    return answer