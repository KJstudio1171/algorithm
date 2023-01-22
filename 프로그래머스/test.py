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
        if score(find_arr(n - info[index] - 1,  make_arr(arr, info, index), info, index + 1), info) > 0:
            print(score(find_arr(n - info[index] - 1,  make_arr(arr, info, index), info, index + 1), info))
        if score(find_arr(n,  make_arr(arr, info, 100), info, index + 1), info) > 0 :
            print(score(find_arr(n,  make_arr(arr, info, 100), info, index + 1), info))
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

solution(5, [2,1,1,1,0,0,0,0,0,0,0])