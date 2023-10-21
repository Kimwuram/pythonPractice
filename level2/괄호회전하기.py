def solution(s):
    answer = 0
    spin = ""
    for i in range(len(s)):
        spin =  s[i:] + s[:i]
        while (True):
            if "()" in spin:
                idx = spin.index("()")
                spin = spin[:idx] + spin[idx+2:]
            elif "[]" in spin:
                idx = spin.index("[]")
                spin = spin[:idx] + spin[idx+2:]
            elif "{}" in spin:
                idx = spin.index("{}")
                spin = spin[:idx] + spin[idx+2:]
            else:
                break
        if len(spin) == 0:
            answer += 1
    return answer

print(solution("}}}"))