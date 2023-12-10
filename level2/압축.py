def solution(msg):
    answer = []
    index = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U', 'V', 'W','X','Y','Z']
    while True:
        idx = 0
        temp = ""
        for i in range(1000):
            if len(temp) == 0:
                temp = msg[idx]
                idx += 1
            else:
                temp += msg[idx]
                if temp in index:
                    idx += 1
                else:
                    index.append(temp)
                    answer.append(index.index(temp[:len(temp) - 1]) + 1)
                    msg = msg[len(temp) - 1:]
                    break
            if idx == len(msg):
                if temp in index:
                    answer.append(index.index(temp) + 1)
                else:
                    answer.append(index.index(temp[:len(temp) - 1]) + 1)
                return answer

print(solution("ABABABABABABABAB"))