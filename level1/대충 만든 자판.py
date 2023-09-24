def solution(keymap, targets):
    answer = []
    for i in targets:
        res = 0
        for j in i:
            temp = []
            for k in keymap:
                if j in k:
                    temp.append(k.index(j) + 1)
            if len(temp) == 0:
                res = -1
                break
            else:
                res += min(temp)
        answer.append(res)
    return answer
    
print(solution( ["BC"], ["AC", "BC"]))