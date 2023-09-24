def solution(wallpaper):
    answer = []
    s1 = 0
    s2 = 0
    e1 = 0
    e2 = 0
    temp = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                temp.append([i, j])
    s1 = temp[0][0]
    s2 = temp[0][1]
    e1 = temp[0][0]
    e2 = temp[0][1]
    for i in temp:
        if i[0] < s1:
            s1 = i[0]
        if i[1] < s2:
            s2 = i[1]
        if i[0] > e1:
            e1 = i[0]
        if i[1] > e2:
            e2 = i[1]
            
    answer = [s1, s2, e1 + 1, e2 + 1]
    return answer
    
print(solution([".#...", "..#..", "...#."]))