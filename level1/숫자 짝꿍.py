def solution(X, Y):
    answer = ''
    # for i in range(len(X)):
    #     if X[i] in Y:
    #         if len(answer) == 0:
    #             answer += X[i]
    #         else:
    #             if answer[-1] >= X[i]:
    #                 answer = answer + X[i]
    #             else:
    #                 answer = X[i] + answer
    #         idx = Y.index(X[i])
    #         Y = Y[:idx]  + Y[idx + 1:]
    # if len(answer) == 0:
    #     return "-1"
    # if answer.count("0") == len(answer):
    #     answer = "0"
    dic = {}

    # for i in range(len(X)):
    #     if X[i] in Y:
    #         if X.count(X[i]) > Y.count(X[i]):
    #             dic[X[i]] = Y.count(X[i])
    #         else:
    #             dic[X[i]] = X.count(X[i])
    # if len(dic) == 0:
    #     return "-1"
    #
    # for i in dic.keys():
    #     for j in range(int(dic[i])):
    #         answer +=i
    # if answer.count("0") == len(answer):
    #     return "0"
    # return ''.join(sorted(answer, reverse=True))
    val = 0
    for i in range(10):
        if X.count(str(i)) > Y.count(str(i)):
            dic[str(i)] = Y.count(str(i))
        else:
            dic[str(i)] = X.count(str(i))
        if dic[str(i)] != 0:
            val = 1
    if val == 0:
        return "-1"
    for i in range(10):
        for j in range(int(dic[str(i)])):
            answer +=str(i)
    if answer.count("0") == len(answer):
        return "0"
    return ''.join(sorted(answer, reverse=True))
    
    
print(solution("100", "123450"))