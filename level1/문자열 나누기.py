def solution(s):
    answer = 0
    idx = 0
    while idx < len(s):
        a = s[idx]
        e = 1
        d = 0
        if idx == len(s) - 1:
            return answer + 1

        for i in range(idx + 1, len(s)):
            if s[i] == a:
                e += 1
            else:
                d += 1
            if e == d:
                idx = i + 1
                answer += 1
                break
            idx = i
        
    return answer
    
print(solution("aaabbaccccabba"))