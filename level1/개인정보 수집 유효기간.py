def solution(today, terms, privacies):
    answer = []
    ltoday = today.split(".")
    td = 28 * 12 * int(ltoday[0]) + int(ltoday[1]) * 28 + int(ltoday[2])
    for i in range(len(privacies)):
        for j in terms:
            ps = privacies[i].split(" ")
            ts = j.split(" ")
            if ps[1] == ts[0]:
                pss = ps[0].split( ".")
                ed = 28 * 12 * int(pss[0]) + (int(pss[1]) + int(ts[1])) * 28 + int(pss[2])
                if td >= ed:
                    answer.append(i + 1)
                break
                
    return answer
    
print(solution("2020.01.01", ["A 1"], ["2019.12.01 A"]))