def send_message(message):

    key_path = {
        "1": [".", ",", "?", "!"],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
        "*": ["'", "-", "+", "="],
        "0": [" "],
        "#": ["#"]
    }
    string = ""
    upper_flag = False
    latest_key = ""
    latest_message = ""
    while len(message) > 0:
        for key in key_path:
            if message[0].lower() in key_path[key] or message[0] == key:

                if latest_key == key and (not latest_message.isdigit() and latest_message != "*") and ((latest_message.isupper() and message[0].isupper()) or (latest_message.islower() and message[0].islower()) or not message[0].isalpha()):
                    string += " "

                if message[0].isdigit() or message[0] == "*" or message[0] == "#":
                    string += (message[0]+"-")
                else:
                    if message[0].isupper() and not upper_flag:
                        string += "#" + str(key)*(key_path[key].index(message[0].lower()) + 1)
                        upper_flag = True
                    elif message[0].isupper() and upper_flag or message[0].islower() and not upper_flag:
                        string += str(key)*(key_path[key].index(message[0].lower()) + 1)
                    elif message[0].islower() and upper_flag:
                        string += "#" + str(key)*(key_path[key].index(message[0].lower()) + 1)
                        upper_flag = False
                    else:
                        string += str(key)*(key_path[key].index(message[0].lower()) + 1)
                latest_key = key
                latest_message = message[0]
                break
        message = message[1:]
    return string

send_message("rafa*-here")

# send_message("     ")
# send_message("hey") # 4433999
# send_message("one two three") # 666 6633089666084477733 33
# send_message("Hello World!") # #44#33555 5556660#9#66677755531111
# send_message('Def Con 1!') # #3#33 3330#222#666 6601-1111
# send_message("A-z") # #2**#9999
# send_message("1984") # 1-9-8-4-
# send_message("Big thanks for checking out my kata") # #22#444 4084426655777703336667770222443322255444664066688 806999055282
# send_message("b2b")
# send_message('How could anyone type with this thing?!')# #44#666902226668855530266999666 663308999733094448440844 44477770844 444664111 1111
# send_message("mom, I'll be home by 9, I promise!!!")# 6 666 6110#444*#555 55502233044666 63302299909-110#4440#7 777666 64447777331111 1111 1111