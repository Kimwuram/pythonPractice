def solution(n, a, b):
    answer = 0
    if a > b:
        c = a
        a = b
        b = c
    temp = 0
    for i in range(1, n // 2 + 1):
        if a % 2 == 0 and a != 1:
            temp = 1
        else:
            temp = 0
        if temp == 1:
            if a == b:
                return i
            a = a // 2
            if b % 2 == 0:
                b = b // 2
            else:
                b = b // 2 + 1
        else:
            if b == a or b == a + 1:
                return i
            a = a // 2 + 1
            if a == 0:
                a = 1
            if b % 2 == 0:
                b = b // 2
            else:
                b = b // 2 + 1
    return answer

print(solution(8, 4, 7))