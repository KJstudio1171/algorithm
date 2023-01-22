def solution(s):
    answer = 0
    wordDict = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,
    'six':6,'seven':7,'eight':8,'nine':9}
    word = ''
    for i in s:
        if ord(i) >= ord('0') and ord(i) <= ord('9'):
            if word != '':
                answer = answer * 10 + wordDict[word]
                word = ''
            answer = answer * 10 + int(i)
        else:
            word = word + i
            if word in wordDict:
                answer = answer * 10 + wordDict[word]
                word = ''
    if word != '':
        answer = answer * 10 + wordDict[word]
    return answer