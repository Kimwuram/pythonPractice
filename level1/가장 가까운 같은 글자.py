def solution(s):
    answer = []
    temp = []
    for i in range(len(s)):
        if len(temp) == 0:
            answer.append(-1)
            temp.append([s[i],i])
        else:
            a = 0
            for j in temp:
                if s[i] in j:
                    answer.append(i - j[1])
                    j[1] = i
                    a = 1
            if a == 0:
                answer.append(-1)
                temp.append([s[i],i])
    return answer

print(solution("banana"))