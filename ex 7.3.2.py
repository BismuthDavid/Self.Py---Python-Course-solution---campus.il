def check_win(secret_word, old_letters_guessed):
    """
    this func checks whether the player was able to guess the secret word and thus won the game
    :param secret_word: The string represents the secret word that the player has to guess.
    :type secret_word: str.
    :param old_letters_guessed: the list contains the letters the player has guessed so far.
    :type old_letters_guessed: list.
    :return:returns true if all the letters that make up the secret word are included in the list of letters that the
    user guessed. Otherwise, the function returns false.
    :rtype: bool
    """
    bool_to_return = True
    for char in secret_word:
        if char not in old_letters_guessed:
            bool_to_return = False
    return bool_to_return
            