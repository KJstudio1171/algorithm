def f(n1, n2):
    if n1 % n2 == 0 :
        return n2
    else :
        return f(n2, n1 % n2)

def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    answer.append(numer // f(max(numer, denom), min(numer, denom)))
    answer.append(denom // f(max(numer, denom), min(numer, denom)))
    return answer