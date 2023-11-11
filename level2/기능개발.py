def solution(progresses, speeds):
    answer = []
    needs = []
    for i in range(len(progresses)):
        rest = 100 - progresses[i]
        need = rest // speeds[i]
        if rest % speeds[i] != 0:
            need += 1
        needs.append(need)
    
    res = 0
    stan = 0
    for i in range(len(needs)):
        if stan == 0:
            stan = needs[i]
            res += 1
            continue
        if needs[i] <= stan:
            res += 1        
        else:
            answer.append(res)
            res = 1
            stan = needs[i]
    answer.append(res)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))