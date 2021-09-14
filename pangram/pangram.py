import string

def is_pangram(sentence):
    test_list = list(string.ascii_lowercase)
    score = 0

    for i in test_list:
        if i in sentence.lower():
            score = score + 1
        else:
            score = 0
    
    if score == 26:
        return True
    else:
        return False

