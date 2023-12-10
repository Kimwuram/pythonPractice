def makedec(num, n):
    if num == 0:
        return "0"
    result = ""
    while num:
        res = str(num%n)
        if res == "10":
            res = "A"
        elif res == "11":
            res = "B"
        elif res == "12":
            res = "C"
        elif res == "13":
            res = "D"
        elif res == "14":
            res = "E"
        elif res == "15":
            res = "F"

        result += res
        num = num // n

    return result[::-1]
def solution(n, t, m, p):
    answer = ''
    num = 0
    strnum = ""
    while len(strnum) <= t * m:
        strnum += makedec(num, n)
        num += 1
    strnum = strnum[p - 1:]
    
    while len(answer) < t:
        answer += strnum[0]
        strnum = strnum[m:]
    return answer

print(solution(16,16,2,1))

