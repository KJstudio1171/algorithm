def solution(board, k):
    answer = 0
    for num in range(k + 1):
        for i in range(num + 1):
            if len(board) > i and len(board[0]) > num - i:
                answer += board[i][num - i]
    return answer