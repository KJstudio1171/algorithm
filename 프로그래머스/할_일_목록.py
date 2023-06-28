def solution(todo_list, finished):
    l = []
    for i,v in enumerate(todo_list):
        if finished[i] == False:
            l.append(v)
    return l