def solution(a, b, n):
    answer = 0
    while n >= a:
        if n % a == 0:
            n = b * (n//a)
            answer += n
        else:
            answer += b * (n//a)
            n = b * (n//a) + n % a
    return answer

print(solution(3,2,20))