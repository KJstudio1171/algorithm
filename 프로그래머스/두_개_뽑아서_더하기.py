def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        j = i + 1
        while(j < len(numbers)):
            answer.add(numbers[i] + numbers[j])
            j += 1
    return sorted(list(answer))