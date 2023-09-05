def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    the func will receive a guessed letter and will check if it's on the already guessed letter list and if it's
    standing in the criteria (only one char, from alpha-beta)
    :param letter_guessed: the new guessed letter
    :type letter_guessed: str
    :param old_letters_guessed: string with all the already guessed letters
    :type old_letters_guessed: list
    :return: "X" and the old guessed letters with the sign "->" between, and false as a sign that the guessed letter
    hadn't been adjusted to the list - if the newest guessed letter doesn't match the criteria or if its already been
    guessed.
    and adjust the letter to the already guessed letters and true as a sign that it had been adjusted if it matches
    the criteria, and it's the first time to be guessed.
    :rtype: str + bool
    """

    if len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed:
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        list_to_print = "X\n{0}"
        print(list_to_print.format(" -> ".join(sorted(old_letters_guessed))))
        return False
