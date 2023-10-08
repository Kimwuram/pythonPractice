def solution(elements):
    templist = []
    nums = 1
    orglen = len(elements)
    elements += elements
    #while nums <= orglen:
    for i in range(orglen):
        tempnum = 0
        templist.append(elements[i])
        #for j in range(nums):
        for j in range(i + 1, i + orglen):
            #idx = i + j
            # if idx > len(elements) - 1:
            #     idx = j + i - len(elements)
            tempnum = sum(elements[i:j + 1])
            #tempnum += elements[idx]
            templist.append(tempnum)
     #   nums += 1
    return len(set(templist))

print(solution([7,9,1,1,4]))