def zero(op = ""):
    return operation(op[0], 0, op[1]) if op != "" else 0
def one(op = ""):
    return operation(op[0], 1, op[1]) if op != "" else 1
def two(op = ""):
    return operation(op[0], 2, op[1]) if op != "" else 2
def three(op = ""):
    return operation(op[0], 3, op[1]) if op != "" else 3
def four(op = ""): 
    return operation(op[0], 4, op[1]) if op != "" else 4
def five(op = ""):
    return operation(op[0], 5, op[1]) if op != "" else 5
def six(op = ""):
    return operation(op[0], 6, op[1]) if op != "" else 6
def seven(op = ""):
    return operation(op[0], 7, op[1]) if op != "" else 7
def eight(op = ""):
    return operation(op[0], 8, op[1]) if op != "" else 8
def nine(op = ""):
    return operation(op[0], 9, op[1]) if op != "" else 9

def plus(op):
    return ["+", op]
def minus(op):
    return ["-", op]
def times(op):
    return ["*", op]
def divided_by(op):
    return ["/", op]

def operation(symbol, val1, val2):    
    if symbol == "+":
        return val1 + val2
    elif symbol == "-":
        return val1 - val2
    elif symbol == "*":
        return val1 * val2
    elif symbol == "/":
        return int(val1 / val2)


# print(seven(times(five())))
# print(four(plus(nine())))
# print(eight(minus(three())))
# print(six(divided_by(two())))
print(two(divided_by(three())))