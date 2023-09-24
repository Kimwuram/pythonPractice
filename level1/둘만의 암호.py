def solution(s, skip, index):
    answer = ''
    al = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(skip)):
        a1 = al[:al.index(skip[i])]
        a2 = al[al.index(skip[i]) + 1:]
        al = a1 + a2
    for i in range(len(s)):
        newidx = index
        start = al.index(s[i])
        while start + newidx >= len(al):
            newidx = newidx - len(al)
        answer += al[al.index(s[i]) + newidx]
    return answer

print(solution("aukks","wbqd", 5))