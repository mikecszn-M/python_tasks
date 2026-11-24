text = input("Enter a sentence:")
word = ""

for letter in text:
    if letter == " ":
        print(word)
        word = ""
    else:
        word += letter

print(word)
