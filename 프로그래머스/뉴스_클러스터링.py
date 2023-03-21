def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    set1 = []
    set2 = []
    inter = 0
    len1 = 0
    len2 = 0
    for i,j in enumerate(str1):
        if i < len(str1) - 1 and str1[i].isalpha() and str1[i+1].isalpha():
            set1.append(str1[i]+str1[i+1])
    
    for i,j in enumerate(str2):
        if i < len(str2) - 1 and str2[i].isalpha() and str2[i+1].isalpha():
            set2.append(str2[i]+str2[i+1])
    len1 = len(set1)
    len2 = len(set2)
    for i in set1:
        if i in set2:
            set2.remove(i)
            inter += 1
    if len1 + len2 - inter == 0:
        return 65536

    answer = int(inter / (len1 + len2 - inter) * 65536)
    return answer