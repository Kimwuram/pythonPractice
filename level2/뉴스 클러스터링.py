def solution(str1, str2):
    answer = 0
    a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    lstr1 = []
    lstr2 = []
    n = []
    u = []
    
    for i in range(len(str1) - 1):
        if str1[i + 1] not in a:
            continue
        if str1[i] not in a:
            continue            
        temp = str1[i] + str1[i+1]
        lstr1.append(temp.lower())
        
    for i in range(len(str2) - 1):
        if str2[i + 1] not in a:
            continue
        if str2[i] not in a:
            continue
        temp = str2[i] + str2[i+1]
        lstr2.append(temp.lower())
    
    while len(lstr1):
        if lstr1[0] in lstr2:
            lstr2.pop(lstr2.index(lstr1[0]))
            n.append(lstr1.pop(0))
        else:
            u.append(lstr1.pop(0))

    u = u + n + lstr2
    if n == u:
        return 65536
    answer = int((len(n) / len(u)) * 65536)
    return answer

print(solution("E=M*C^2", "e=m*c^2"))