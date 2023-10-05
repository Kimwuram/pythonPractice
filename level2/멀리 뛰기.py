def getPac(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def solution(n):
    answer = 1
    cnt = 0
    while ((cnt + 1) * 2) <= n:
        cnt += 1
        a1 = cnt + (n - 2 * cnt)
        a2 = (n - 2 * cnt)
        a = getPac(cnt + (n - 2 * cnt))
        b = getPac((n - 2 * cnt))
        c = getPac(cnt)
        
        answer += a // (b * c)
            
    return int(answer) % 1234567

print(solution(2000))