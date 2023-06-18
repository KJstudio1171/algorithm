def install_rest_stops(N, y):
    dp = [0] * N
    dp[0] = 1  # 첫 번째 좌표에는 항상 휴게소를 설치할 수 있음

    for i in range(1, N):
        dp[i] = dp[i-1]  # 이전 좌표에서 설치 가능한 휴게소 개수를 그대로 가져옴
        max_height = 0

        for j in range(i-1, -1, -1):
            if y[j] > max_height and dp[i] < dp[j] + 1:
                # i번째 좌표보다 낮으면서 j번째 좌표에서 설치 가능한 휴게소 개수 + 1이 더 크면 업데이트
                dp[i] = dp[j] + 1
                max_height = y[j]

    return dp[-1]  # 마지막 좌표까지 계산한 휴게소 개수 반환


# 테스트 케이스 수 입력
TC = int(input())

for _ in range(TC):
    # 정수 N 입력
    N = int(input())
    # 정수 y_i들 입력
    y = list(map(int, input().split()))

    result = install_rest_stops(N, y)
    print(result)
