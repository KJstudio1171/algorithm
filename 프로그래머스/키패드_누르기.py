def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def solution(numbers, hand):
    answer = ''
    coordinate = {0 : (1, 0), 1: (0, 3), 2: (1, 3), 3: (2, 3),
    4: (0, 2), 5: (1, 2), 6: (2, 2), 7: (0, 1), 8:(1, 1), 9:(2, 1)}
    left = (0, 0)
    right = (2, 0)
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
        elif i in [3, 6, 9]:
            answer += "R"
        else:
            if distance(left, coordinate[i]) < distance(right, coordinate[i]):
                answer += "L"
            elif distance(left, coordinate[i]) > distance(right, coordinate[i]):
                answer += "R"
            else:
                answer += hand[0].upper()
        if answer[-1] == "R":
            right = coordinate[i]
        else:
            left = coordinate[i]
    return answer