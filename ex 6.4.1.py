def check_valid_input(letter_guessed, old_letters_guessed):
    """
    the func will receive a guessed letter and will check if it's on the already guessed letter list and if it's
    standing in the criteria (only one char, from alpha-beta)
    :param letter_guessed: the new guessed letter
    :type letter_guessed: str
    :param old_letters_guessed: string with all the already guessed letters
    :type old_letters_guessed: list
    :return: false if the newest guessed letter doesn't match the criteria or if its already been guessed.
             true if it matches the criteria, and it's the first time to be guessed.
    :rtype: bool
    """

    if len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed:
        return True
    else:
        return False
