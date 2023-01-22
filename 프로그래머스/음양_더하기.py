def solution(absolutes, signs):
    return sum([i[0] for i in zip(absolutes, signs) if i[1]]) - sum([i[0] for i in zip(absolutes, signs) if not i[1]])