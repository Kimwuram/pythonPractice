def solution(food):
    answer = ''
    for i in range(1, len(food)):
        for j in range(food[i] // 2) :
            answer += str(i)
    temp = ''.join(sorted(answer, reverse=True))
    answer = answer + '0' + temp
    
    return answer

print(solution([1,3,4,6]))