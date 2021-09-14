def abbreviate(words):
    acronym = ''
    for i in words.replace('-',' ').split():
        acronym = acronym + i.replace('_', '')[0].upper()
    return acronym
