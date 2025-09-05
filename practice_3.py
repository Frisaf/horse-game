# letters = ["n", "t", "i"]
# letters.reverse()
# print(letters)

letters = ["n", "t", "i"]
word = ""

for letter in letters:
    word += letter

letters_reversed = []
word_reversed = ""

for i in range(len(letters)):
    letters_reversed.insert(0, letters[i])

for letter in letters_reversed:
    word_reversed += letter

print(letters)
print(word.upper())
print(letters_reversed)
print(word_reversed.upper())