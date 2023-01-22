# def make_list(arr, i):
#     temp = arr[:]
#     temp[i] = 1
#     return temp

# def find_arr(arr, n, info):
#     if n == 0:
#         return arr
#     if n == 1:
#         for i,j in enumerate(arr):
#             if j == 0:
#                 arr[i] = 1
#                 return arr
#         arr[-1] += 1
#         return arr
#     for i,j in enumerate(arr):
#         if j == 1:
#             continue
#         elif j == 0:
#             arr[i] = 1
#             return find_arr(arr, n - 1, info)
#         else:
#             if -j > n - 1:
#                 continue
#             temp = score(find_arr(make_list(arr, i), n + j - 1, info), info), i , j
#             for k,e in enumerate(arr):
#                 if k <= i:
#                     continue
#                 if -e > n - 1 or e == 1:
#                     continue
#                 else:
#                     if score(find_arr(make_list(arr, k), n + e - 1, info), info) >= temp[0]:
#                              temp = score(find_arr(make_list(arr, k), n + e - 1, info), info), k, e
#             return find_arr(make_list(arr, temp[1]), n + temp[2] - 1, info)
#     arr[-1] += n
#     return arr

# def score(arr, info):
#     num = 0
#     for i, j in enumerate(arr):
#         if j < 0 :
#             num -= (10 - i)
#             if -1 * info[i] != j:
#                 num += (10 ** (-1 * (11 - i))) * (info[i] + j)
#         elif j > 0 :
#             num += (10 - i)
#             num += (10 ** (-1 * (11 - i))) * j
#     return num
        

# def solution(n, info):
#     minus_list = list(map(lambda x : x * -1, info))
#     finded_list = find_arr(minus_list, n, info)
#     if 1 > score(finded_list, info):
#         return [-1]
#     ret = []
#     for i, j in enumerate(finded_list):
#         if info[i] == 0:
#             ret.append(j)
#             continue
#         if info[i] == j and j < 0:
#             ret.append(0)
#             continue
#         else:
#             ret.append(info[i] + j)
#     return ret

def score(arr, info):
    num = 0
    for i,j in enumerate(arr):
        if j > 0:
            num += 10 ** (-1 * (11 - i))
        if info[i] == j and info[i] == 0:
            continue
        if info[i] >= j:
            num -= (10 - i)
        else:
            num += (10 - i)
    return num

def make_arr(arr, info, index):
    temp = arr[:]
    if index == 100:
        return temp
    temp[index] = info[index] + 1
    return temp

def find_arr(n, arr, info, index):
    if index == 10:
        arr[-1] += n
        return arr
    if n == 0:
        return arr
    if n > info[index]:
        if score(find_arr(n - info[index] - 1,  make_arr(arr, info, index), info, index + 1), info) > score(find_arr(n,  make_arr(arr, info, 100), info, index + 1), info):
            return find_arr(n - info[index] - 1,  make_arr(arr, info, index), info, index + 1)
        else:
            return find_arr(n,  arr, info, index + 1)
    return find_arr(n,  arr, info, index + 1)
    
    

def solution(n, info):
    arr = [0] * 11
    answer = find_arr(n, arr, info, 0)
    if score(answer, info) < 1:
        return [-1]
    print(answer)
    return answer