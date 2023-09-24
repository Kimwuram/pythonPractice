def solution(babbling):
    answer = 0
    available = [ "aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for j in available:
            idx = 0
            cnt = 0
            while True:
                if j in i:
                    if cnt == 0:
                        idx = i.index(j)
                        if idx == 0:
                            i = i[:idx] + i[idx + len(j):]
                        else:
                            i = i[:idx] +"-"+ i[idx + len(j):]
                    else:
                        if idx == i.index(j):
                            i = "x"
                    cnt += 1
                else:
                    break
                # if j in i:
                #     if i.index(j) == idx:
                #         i  = 'x'
                #         break
                #     else:
                #         idx = i.index(j)
                #         i = i[:idx] + i[idx + len(j):]
            # else:
            #     break

        if i.count('-') == len(i):
            answer += 1
        elif len(i) == 0:
            answer += 1
    
    # for i in babbling:
    #     temp = ""
    #     for j in i:
    #         temp += j
    #         if temp in available:

    return answer
    
    
print(solution(	["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))