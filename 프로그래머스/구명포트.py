def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people)
    while(i < j):
        if people[i] + people[j - 1] <= limit:
            i+=1
        answer += 1
        j-=1
           
    return answer