def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return 5 * len(cities)
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        if cities[i] in cache:
            answer += 1
        else:
            answer += 5
        if len(cache) < cacheSize:
            if cities[i] not in cache:
                cache.append(cities[i])
            else:
                cache.append(cache.pop(cache.index(cities[i])))
        else:
            if cities[i] not in cache:
                cache = cache[1:]
                cache.append(cities[i])
            else:
                cache.append(cache.pop(cache.index(cities[i])))
    return answer

print(solution(2,["a", "a", "a", "b", "b", "b", "c", "c", "c"]))