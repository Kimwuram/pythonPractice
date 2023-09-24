def solution(k, score):
    answer = []
    temp = []
    for i in range(len(score)):
        if i < k:
            temp.append(score[i])
            answer.append(min(temp))
        else:
            if score[i] >= min(temp):
                temp[temp.index(min(temp))] = score[i]
                answer.append(min(temp))
            else:
                answer.append(min(temp))
    return answer


print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))