def is_valid_input(letter_guessed):
    """
    the func will return false for: 1. str with more than one char.  2. if the str contain a non alpha-bet char.
    and will return true if the str contain only a single char from the abc.
    :param letter_guessed: string (expected a single char)
    :type letter_guessed: str
    :return: true if the condition are matched, false if it isn't
    :rtype: bool
    """
    if letter_guessed.isalpha() and len(letter_guessed) == 1:
        return True
    else:
        return False