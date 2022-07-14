def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

solution = lambda n, arr1, arr2: ([''.join(map(lambda x: '#' if x=='1' else ' ', "{0:b}".format(row).zfill(n))) for row in (a|b for a, b in zip(arr1, arr2))])

def solution(n, arr1, arr2):
    answer = []
    for index in range(0,n):
        answer.append(str(bin(arr1[index] | arr2[index] | pow(2,n))).replace("0b1","").replace("1","#").replace("0"," "))
        pass

    return answer