word = "Wordings"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for things in word:
    if ("A" <= things <= "Z") or ("a" <= things <= "z"):
        if things in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
