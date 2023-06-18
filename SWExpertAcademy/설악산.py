tc = int(input())
for test_num in range(1, tc + 1):
    result = 0
    high = 0
    n = int(input())
    data = list(map(int, input().split()))
    if n == 1:
        print(f"#{test_num} 1")
        continue
    for i, j in enumerate(data):
        if i == 0 and j < data[i + 1]:
            result += 1
            continue
        if i == len(data) - 1:
            if j <= data[i - 1]:
                result += 1
                break
            else:
                break
        if j <= data[i - 1] and j < data[i + 1]:
            result += 1
    print(f"#{test_num} {result}")
