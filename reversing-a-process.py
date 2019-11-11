
def code(string, number):
    alphabet = ''.join(chr(x) for x in range(ord('a'), ord('z') + 1))
    string_result = ""
    for letter in string:
        index = alphabet.index(letter)
        string_result += alphabet[index * number % len(alphabet)]
        print(index * number % len(alphabet))
    print(str(number) + string_result)
        

def decode(string):
    alphabet = ''.join(chr(x) for x in range(ord('a'), ord('z') + 1))
    number = ''.join(x for x in string if x.isdigit())
    new_string = string[len(number):]
    decode_string = ""
    while len(new_string) > 0:
        for letter in alphabet:
            print("----------------------------")
            print(str(alphabet.index(new_string[0])) +" == "+ str(alphabet.index(letter) * int(number) % len(alphabet)))
            print("----------------------------")            
            if alphabet.index(new_string[0]) == alphabet.index(letter) * int(number) % len(alphabet):
                print('entre')
                decode_string += alphabet[alphabet.index(letter)]
                new_string = new_string[1:]
                break            
    
    return decode_string

#decode("6015ekx")
# code("mer", 6015)

# 761328 qockcouoqmoayqwmkkic

#code("abcdefghijk", 5057)
code("qockcouoqmoayqwmkkic", 761328)
#print(decode("5057efghijk"))


# Closed, in progress .....
