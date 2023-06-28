def solution(my_string, is_prefix):
    for i,p in enumerate(is_prefix):
        if i < len(my_string) and my_string[i] == p :
            continue
        else:
            return 0
    return 1