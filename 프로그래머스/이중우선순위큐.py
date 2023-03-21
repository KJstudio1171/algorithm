def solution(operations):
    queue = []
    for i in operations:
        inst = i.split(" ")
        if inst[0] == 'I':
            queue.append(int(inst[1]))
        elif inst[0] == 'D':
            if not queue:
                continue
            if inst[1] == '1':
                queue.remove(max(queue))
            else:
                queue.remove(min(queue))
    if not queue:
        answer = [0,0]
    else:
        answer = [max(queue), min(queue)]
    return answer