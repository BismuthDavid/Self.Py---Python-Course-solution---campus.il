def show_hidden_word(secret_word, old_letters_guessed):
    """
    The function returns a string consisting of letters and underscores. The string shows the letters from the
    old_letters_guessed list that are in the secret_word string in their appropriate position, and the other letters
    in the string (which the player has not yet guessed) as underlines.
    :param secret_word: string containing the word need's to guess.
    :type secret_word: str.
    :param old_letters_guessed: list of already guessed letter.
    :type old_letters_guessed: list
    :return: string with correct guessed letters at there idx and underlines at the places the player didn't gues.
    :rtype: str
    """
    string_to_print = ""
    for char in secret_word:
        if char not in old_letters_guessed:
            string_to_print += "_ "
        else:
            string_to_print += char + " "
    return string_to_print[:-1]
