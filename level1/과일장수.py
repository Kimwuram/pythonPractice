# def solution(k, m, score):
#     answer = 0
#     box = []
#     temp = []
#     for i in range(len(score)):
#         temp.append(score.pop(score.index(max(score))))
#         if len(temp) == m:
#             box.append(temp)
#             temp = []
#     for i in box:
#         if len(i) == m:
#             answer += m * min(i)
#     return answer

def solution(k, m, score):
    answer = 0
    temp = []
    score.sort(reverse = True)
    idx = 0
    for i in range(len(score)):
        if idx + m <= len(score):
            temp = score[idx:idx+m]
            answer += m * min(temp)
            idx += m
        else:
            break
    return answer

print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))