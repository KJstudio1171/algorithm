def solution(arr, queries):
    dp = [0] * 1000001
    for i in queries:
        for j in range(i[0], i[1] + 1):
            dp[j] += 1
    for i in range(0, len(arr)):
        arr[i] += dp[i]
    answer = arr
    return answer