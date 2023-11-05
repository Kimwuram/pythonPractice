def solution(want, number, discount):
    answer = 0
    startidx = 0
    copynum = []
    if len(discount) < 10:
        return 0
    for i in range(len(discount) - 9):
        copynum = number[:]
        if discount[i] in want:
            startidx = i
            for j in range(i, i + 10):
                if discount[j] in want:
                    copynum[want.index(discount[j])] -= 1
                    if copynum[want.index(discount[j])] < 0:
                        break
                else:
                    break
            if sum(copynum) == 0:
                if len(set(copynum)) == 1:
                    answer += 1
                else:
                    continue
            else:
                continue
        else:
            continue
        
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], 
               [3, 2, 2, 2, 1], 
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))