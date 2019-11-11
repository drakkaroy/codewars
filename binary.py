def code(strng):
    binary_result = ""
    for n in (strng):
        binary = str(bin(int(n))[2:])
        k_times_0 = str(len(binary) - 1)
        k = ('0' * int(k_times_0)) + "1"
        binary_result = binary_result + (k + binary)
    return binary_result

def decode(strng):
    decimal = ""
    while len(strng) > 0:
        k_binary = (strng.index("1") + 1) * 2
        decimal += str(int(strng[strng.index("1") + 1:k_binary],2))
        strng = strng[k_binary:]
    return decimal

decode("0011010011010011011010101111110011000011000011000011100011100011100011100011100011100001100100011001000110011100011001001111001111001111001111001111001111")