def wave(strg):
    return [( strg[:x] + strg[x].upper() + strg[x+1:]) for x in range(0, len(strg)) if strg[x] != " "]


print(wave("codewars"))
print(wave("two words"))
print(wave(""))