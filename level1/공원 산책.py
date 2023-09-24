def solution(park, routes):
    answer = []
    x = 0
    y = 0
    s = []
    obs = []
    f = 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                s.append(i)
                s.append(j)
            if park[i][j] == "X":
                obs.append([i, j])
                
    for i in routes:
        if i[0] == "N":
            if s[0] - int(i[-1]) < 0:
                continue
            else:
                for j in obs:
                    if j[0] < s[0] and j[0] >= s[0] - int(i[-1]) and j[1] == s[1]:
                        f = 1
                if f == 1:
                    f = 0
                    continue
                s[0] = s[0] - int(i[-1])
        elif i[0] == "S":
            if s[0] + int(i[-1]) >= len(park[1]):
                continue
            else:
                for j in obs:
                    if j[0] > s[0] and j[0] <= s[0] + int(i[-1]) and j[1] == s[1]:
                        f = 1
                if f == 1:
                    f = 0
                    continue
                s[0] = s[0] + int(i[-1])
        elif i[0] == "W":
            if s[1] - int(i[-1]) <0:
                continue
            else:
                for j in obs:
                    if j[1] < s[1] and j[1] >= s[1] - int(i[-1]) and j[0] == s[0]:
                        f = 1
                if f == 1:
                    f = 0
                    continue
                s[1] = s[1] - int(i[-1])
        else:
            if s[1] + int(i[-1]) >= len(park[0]):
                continue
            else:
                for j in obs:
                    if j[1] > s[1] and j[1] <= s[1] + int(i[-1]) and j[0] == s[0]:
                        f = 1
                if f == 1:
                    f = 0
                    continue
                s[1] = s[1] + int(i[-1])

    return s
    
print(solution(	["OSO", "OOO", "OXO", "OOO"], ["E 2","S 3","W 1"]))
