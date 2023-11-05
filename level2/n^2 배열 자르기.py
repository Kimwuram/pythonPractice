def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        if i // n >= i%n:
            answer.append(i//n + 1)
        else:
            answer.append(i%n + 1)
    return answer

    # for i in range(1, right):
    #     for j in range(i):
    #         answer.append(i)
    #     for k in range(i, n):
    #         answer.append(k + 1)
    # return answer[left:right+1]

print(solution(4, 7, 14))