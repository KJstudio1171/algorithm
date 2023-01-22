def solution(s):
    return "{0} {1}".format(min(map(int, s.split(" "))), max(map(int, s.split(" "))))