def solution(cards1, cards2, goal):
    pos1 = 0
    pos2 = 0
    val = []
    for i in range(len(goal)):
        if pos1 < len(cards1):
            if goal[i] == cards1[pos1]:
                pos1 += 1
                val.append(goal[i])
                continue
        if pos2 < len(cards2):
            if goal[i] == cards2[pos2]:
                pos2 += 1
                val.append(goal[i])
                continue
    if val == goal:
        return "Yes"
    else:
        return "No"

print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))