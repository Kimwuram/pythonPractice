def solution(s):
    answer = []
    s = s.replace("{", "")
    ls = []
    ltemp = s.split("}")
    for i in ltemp:
        if len(i) == 0:
            continue
        if i[0] == ",":
            i = i[1:]
        temp = i.split(",")
        ls.append(temp)
                
    ls.sort(key=len)

    for i in ls:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer

print(solution("{{20,111},{111}}"))