def solution(string,markers):

    newString = ""
    flag = False
    for x in string:
        if flag:
            if x == "\n":
                newString = newString.strip(" ")
                flag = False
                newString += "\n"
        else:
            if x in markers:
                flag = True
            else:
                newString += x

    return newString.strip(" ")
    #return newString.encode('unicode_escape').decode("utf-8").strip(" ")

# print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
# # "apples, pears\ngrapes\nbananas"
# print(solution("a #b\nc\nd $e f g", ["#", "$"]))
# # "a\nc\nd"

######################## BEST SOLUTION ########################################
# def solution(string,markers):
#     parts = string.split('\n')
#     for s in markers:
#         parts = [v.split(s)[0].rstrip() for v in parts]
#     return '\n'.join(parts)