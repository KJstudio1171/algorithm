def solution(lottos, win_nums):
    answer = [0,0]
    for i in lottos:
        if i == 0:
            answer[0] += 1
            continue
        for j in win_nums:
            if i == j:
                answer[0] += 1
                answer[1] += 1
    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))