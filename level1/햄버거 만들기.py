def solution(ingredient):
    answer = 0
    i = 0
    makesense = 0
    while i < len(ingredient) -3:

        if len(ingredient) < 4:
            return answer
        
        if ingredient[i:i+4] == [1,2,3,1]:
            makesense = 1
            answer += 1
            del(ingredient[i:i+4])
            i -= 3
        else:
            i += 1
            continue

    return answer
#print(solution(	[1, 3, 2, 1, 2, 1, 3, 1, 2]))
