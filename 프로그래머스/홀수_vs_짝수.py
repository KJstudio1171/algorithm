def solution(num_list):
    a = sum([v if i % 2 else 0 for i,v in enumerate(num_list)])
    b = sum([v if not i % 2 else 0 for i,v in enumerate(num_list)])
    return a if a > b else b