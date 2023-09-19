def choose_word(file_path, index):
    """
    this func will receive a file path to a file that contain words to chose from, and an index that represent the index
    of a word in the file.
    the indexed word will be the word that the player will need to guess.
    if the index is greater than the quantity of the words in the file, the func will continue to count from the start
    of the file.
    :param file_path: string of a file path.
    :type file_path: str.
    :param index: a number that represent the index of the word that the player will need to guess.
    :type index: int.
    :return: a tuple that contain to parameter's, first: the num of the words in the file (without duplicates),
             second: the chosen word that the player will need to guess.
    :rtype: tuple
    """
    with open(file_path, 'r') as input_file:
        words = input_file.read()
    words = words.split(" ")

    import collections
    counter = collections.Counter(words)
    unique_words = len(counter)

    if len(words) == 1:
        chosen_word = words[0]
    elif index <= len(words):
        chosen_word = words[index - 1]
    else:
        multiply = (index // len(words)) + 1
        words = words * multiply
        chosen_word = words[index - 1]
    value_to_return = (unique_words, chosen_word)
    return value_to_return

