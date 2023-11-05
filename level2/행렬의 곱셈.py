def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        temp = []
        for i2 in range(len(arr2[0])):
            idx = 0
            t = 0
            for j in range(len(arr1[0])):
                if idx <= len(arr2):
                    t += arr1[i][j] * arr2[idx][i2]
                    idx += 1
                else:
                    break
            temp.append(t)
        answer.append(temp)
    return answer

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))