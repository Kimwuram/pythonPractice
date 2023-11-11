def solution(priorities, location):
    end = []
    target = location
    
    while True:
        if target == 0:
            if priorities[0] >= max(priorities):
                return len(end) + 1
            else:
                target = len(priorities)
        if priorities[0] >= max(priorities):
            end.append(priorities.pop(0))
            target -= 1
        else:
            priorities.append(priorities.pop(0))
            target -= 1
            
print(solution([1, 1, 9, 1, 1, 1], 0))