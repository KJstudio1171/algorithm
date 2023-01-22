def solution(cacheSize, cities):
    answer = 0
    cache = []
    for i in cities:
        if i.lower() in cache:
            answer += 1
            cache.remove(i.lower())
        else:
            answer += 5
            if cacheSize and len(cache) == cacheSize:
                cache.pop(0)
        if cacheSize:
            cache.append(i.lower())
    return answer