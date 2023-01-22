def solution(s):
    answer = []
    for i in s.lower().split(" "):
        answer.append([k.upper() if j % 2 == 0 else k for j,k in enumerate(i)])
    return " ".join(["".join(i) for i in answer])