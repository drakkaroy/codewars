def solution(s):
    return [s[x]+"_" if x == len(s)-1 and len(s) % 2 != 0 else s[x] + s[x+1] for x in range(0, len(s), 2)]



print(solution("asdfads"))