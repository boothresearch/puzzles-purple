def find_anagrams(word, candidates):
    letters = set(word)
    print(letters)
    print(type(letters))
    for letter in letters:
        for candidate in candidates:
            if letter in candidate:
                print(candidate)
    return(candidates[0])


print(find_anagrams("listen", ["enlists" "google" "inlets" "banana"]))