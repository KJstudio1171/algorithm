t = int(input())
for test_num in range(1, t + 1):
    sellPrice = 0
    profit = 0
    n = int(input())
    price = list(map(int, input().split()))
    for j in reversed(price):
        if j > sellPrice:
            sellPrice = j
        else:
            profit += sellPrice - j
    print("#" + str(test_num), profit)
