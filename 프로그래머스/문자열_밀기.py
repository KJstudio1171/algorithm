def shift(A):
    return A[-1] + A[0:-1]

def solution(A, B):
    if A == B:
        return 0
    for i,j in enumerate(range(len(B) - 1)):
        A = shift(A)
        if A == B:
            return i + 1
    return -1