import time

# ask the user for a word
word = input("Please enter a word: ")

while word != "chupacabra":
    word = input("Please enter another word: ")
    if word == "cupacabra":
        break

print("You've successfully left the loop.")