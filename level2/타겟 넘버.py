def solution(numbers, target):
    def findsum(idx, numsum):
        nonlocal answer
        if idx == len(numbers):
            if numsum == target:
                answer += 1
            return
        findsum(idx+1, numsum + numbers[idx])
        findsum(idx+1, numsum - numbers[idx])
    answer = 0
    findsum(0, 0)
    return answer


print(solution([4, 1, 2, 1], 4))