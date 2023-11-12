from itertools import *
def solution(k, dungeons):
    d2 = []
    case = []
    answers = []
    for i in dungeons:
        if i[0] <= k:
            d2.append(i)
    case = list(permutations(d2, len(d2)))
    
    for i in range(len(case)):
        answer = 0
        k2 = k
        b = case[i]
        for j in case[i]:
            a = j[0]
            if k2 >= j[0]:
                k2 -= j[1]
                answer += 1
        answers.append(answer) 

    return max(answers)

print(solution(80, [[80,20],[50,40],[30,10]]))