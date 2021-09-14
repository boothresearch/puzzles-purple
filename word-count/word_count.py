def count_words(sentence):
    #remove the space thing
    s = s.replace("\n"," ").replace("\t"," ")

    #handle apostrophe
    s = s.replace("'s","ag96")

    #handle punctuation
    s_new = s.translate(str.maketrans('', '', string.punctuation)).lower()

    #word list
    s_list = (s_new.split(' '))

    #count the words
    count = dict()
    for i in s_list:
        i=i.replace("ag96","'s")
        if i in count.keys():
            count[i]=count[i]+1
        else:
            count[i]=1

    return count
