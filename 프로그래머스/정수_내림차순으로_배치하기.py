def solution(n):
    return int("".join(i for i in list(map(str, list(reversed(sorted(list(map(int, str(n))))))))))