def goodVsEvil(good, evil):
    good_worth = [1,2,3,3,4,10]
    evil_worth = [1,2,2,2,3,5,10]
    gwr = sum([int(good.split()[x]) * good_worth[x] for x in range(0, len(good.split()))])
    ewr = sum([int(evil.split()[x]) * evil_worth[x] for x in range(0, len(evil.split()))])
    if gwr > ewr:
        return "Battle Result: Good triumphs over Evil"
    elif gwr < ewr:
        return "Battle Result: Evil eradicates all trace of Good"
    elif gwr == ewr:
        return "Battle Result: No victor on this battle field"





print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
print(goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0'))
print(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'))