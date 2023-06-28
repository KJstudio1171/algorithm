def solution(str_list, ex):
    return "".join([i if not ex in i else '' for i in str_list])