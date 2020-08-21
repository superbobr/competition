def vowels_count(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    i = 0
    for letter in word:
        if letter in vowels:
            i += 1
    return i


print(vowels_count('Pseudopseudohypoparathyroidism'))