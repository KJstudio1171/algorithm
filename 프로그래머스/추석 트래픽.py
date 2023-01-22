from collections import deque

def timeTofloat(string):
    time = string.split(':')
    val = float(time[0])*3600 + float(time[1])*60 + float(time[2])
    return val

def solution(lines):
    answer = 1
    list_start = []
    deque_end = deque()
    list_answer = []
    for i in lines:
        start,end = (round(timeTofloat(i.split(' ')[1]) - float(i.split(' ')[2].replace('s','')) + 0.001, 3), timeTofloat(i.split(' ')[1]))
        list_start.append((start,end))
        deque_end.append((start,end))
    list_start.sort()
    deque_start = deque(list_start)
    while deque_start:
        if not list_answer:
            list_answer.append(deque_start.popleft())
        while deque_start and list_answer and deque_start[0][0] < list_answer[0][0] + 1:
            list_answer.append(deque_start.popleft())
        answer = max(len(list_answer),answer)
        while deque_start and deque_start[0][0] < deque_end[0][1] + 1:
            list_answer.append(deque_start.popleft())
        answer = max(len(list_answer),answer)
        list_answer.remove(deque_end.popleft())
    return answer

print(solution(	["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))