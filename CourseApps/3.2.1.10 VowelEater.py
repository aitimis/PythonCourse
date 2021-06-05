word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input('Enter a word: ')
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    if letter == "E":
        continue
    if letter == "I":
        continue
    if letter == "O":
        continue
    if letter == "U":
        continue
    else:
        word_without_vowels += letter

# Print the word assigned to word_without_vowels.
print(word_without_vowels)