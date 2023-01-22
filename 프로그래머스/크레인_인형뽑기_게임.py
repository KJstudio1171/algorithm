def solution(board, moves):
    answer = 0
    stack = []
    moves = list(map(lambda x: x - 1, moves))
    for i in moves:
        for j in board:
            if j[i] != 0:
                stack.append(j[i])
                j[i] = 0
                if len(stack) >= 2 and stack[-2] == stack[-1]:
                    del stack[-2] #pop을 썼으면 더 좋았을 듯하다.
                    del stack[-1]
                    answer += 2
                break
    return answer