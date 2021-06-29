#!/usr/bin/python3

secret_word = "mike"
guess_word = ""
guess_count = 0
guess_limit = 3

while guess_word != secret_word:
    if guess_count < guess_limit:
        guess_word = input("guess word: ")
        guess_count +=1
    else:
        print("you are out of chances")
        break
    