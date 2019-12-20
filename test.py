def wave(strg):

    for x in range(0, len(strg)):
        print( strg[:x] + strg[x].upper() + strg[x+1:])


wave("codewars")