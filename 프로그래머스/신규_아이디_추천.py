def solution(new_id):
    answer_able = '0123456789abcdefghijklmnopqrstuvwxyz-_.'
    answer = new_id.lower()
    for i in new_id:
        if i not in answer_able:
            answer = answer.replace(i, '')
    answer = '.'.join([i for i in answer.split('.') if i != ''])
    if answer == '':
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[0:15].strip('.')
    if len(answer) <= 2:
        while len(answer) != 3:
            answer = answer + answer[-1]
    return answer
