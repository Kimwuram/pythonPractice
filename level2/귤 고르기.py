def solution(k, tangerine):
    answer = 0
    tempdic = {}
    templist = []
    for i in tangerine:
        if str(i) not in tempdic:
            tempdic[str(i)] = 1
        else:
            tempdic[str(i)] += 1
    
    templist = sorted(list(tempdic.values()), reverse=True)
    if templist[0] >= k:
        return 1
    t = 0
    for i in templist:
        if t < k:
            answer += 1
            t += i 
        if t >= k:
            break
            
    return answer

print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))