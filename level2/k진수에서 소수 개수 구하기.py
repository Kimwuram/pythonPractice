def solution(n, k):
    answer = 0
    strnum = ""
    answers = []
    while n:
        strnum = strnum + str(n % k)
        n = n // k
    strnum = strnum[::-1]

    while len(strnum) > 0:
        temp = ''
        idx = strnum.find("0")
        if idx == 0:
            strnum = strnum[1:]
        elif idx > 0:
            temp = strnum[:idx]
            answers.append(temp)
            strnum = strnum[idx:]

        else:
            if len(strnum) != 0:
                answers.append(strnum)
                break
    for i in answers:
        ps = 0
        for j in range(2, int(int(i) ** 0.5) + 1):
            if int(i) % j == 0:
                ps += 1
        if ps == 0:
            if i != "1":
                answer += 1

    return answer

print(solution(883438, 3))
