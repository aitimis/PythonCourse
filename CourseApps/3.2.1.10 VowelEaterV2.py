wordWithoutVowels = ""
userWord = input("Please Enter a word: ")

# make a copy of userWord
output = userWord

# replace vowels
vowels = 'aAeEiIoOuU'
for letter in vowels:
    output = output.replace(letter, '') # replace letter with empty string

print(output)