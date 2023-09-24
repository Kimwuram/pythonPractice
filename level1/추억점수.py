def solution(name, yearning, photo):
    answer = []
    for i in photo:
        temp = 0
        for j in i:
            if j in name:
                temp += yearning[name.index(j)]
        answer.append(temp)
    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))