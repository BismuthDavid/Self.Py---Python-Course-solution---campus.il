guessed_letter = input("Guess a letter:\n")
if guessed_letter.isalpha() and len(guessed_letter) > 1:
    print("E1")
elif not guessed_letter.isalpha() and len(guessed_letter) == 1:
    print("E2")
elif not guessed_letter.isalpha() and len(guessed_letter) > 1:
    print("E3")
else:
    print(guessed_letter.lower())

