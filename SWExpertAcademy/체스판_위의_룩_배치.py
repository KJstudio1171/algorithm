t = int(input())
for i in range(1, t + 1):
    correct = 1
    rook = [0] * 8
    rook_position = []
    for _ in range(8):
        rook_position.append(input())
    for one_line in rook_position:
        if one_line.count("O") != 1:
            print("#" + str(i), "no")
            correct = 0
            break
        rook[one_line.index("O")] += 1
        if rook[one_line.index("O")] != 1:
            print("#" + str(i), "no")
            correct = 0
            break
    if correct:
        print("#" + str(i), "yes")
