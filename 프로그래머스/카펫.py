def solution(brown, yellow):
    for i in range(1, brown + yellow + 1):
        if (brown + yellow) % i:
            continue
        j = (brown + yellow) // i
        if 2 * i + 2 * (j - 2) == brown and (i - 2) * (j - 2) == yellow:
            return [j, i]
    return 0