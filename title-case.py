
def title_case(title, minor_words=''):
    mwl = [minor_words.split()[x].lower() for x in range(0, len(minor_words.split()))]
    tl = [title.split()[x].lower() for x in range(0, len(title.split()))]
    result = ' '.join([tl[x] if tl[x] in mwl and x != 0 else tl[x].title() for x in range(0, len(tl))])

    return result
    
print(title_case(''))
print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
print(title_case('the quick brown fox'))

