def find_anagrams(word, candidates):
    for letter in word:
        candidate[0].search(letter)
    return(candidates[0])


print(find_anagrams("listen", ["enlists" "google" "inlets" "banana"]))