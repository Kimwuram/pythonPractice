def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        a = int(t[i:i+len(p)])
        if a <= int(p):
            answer += 1
    return answer

print(solution("10203", "15"))