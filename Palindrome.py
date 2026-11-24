word = "racecar"
reversed_word = ""

for letter in word:
    reversed_word = letter + reversed_word

if word == reversed_word:
    print("Palindrome jhor")
else:
    print("no Palindrome")
