def rotate(text, key):
    chars = "abcdefghijklmnopqrstuvwxyz"
    newchars = chars[key:] + chars[:key]
    trans = str.maketrans(chars + chars.upper(), newchars + newchars.upper())
    return text.translate(trans)
