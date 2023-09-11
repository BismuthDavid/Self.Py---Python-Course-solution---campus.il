def sort_anagrams(list_of_strings):
    """
    The function receive as a parameter a list of strings, so each string is one word (without spaces).
    The function returns a list of the same strings that were transferred, but in the following way:
    the list is divided into lists so that each "internal" list consists of words that are anagrams of each other
    (anagram: a word consisting of letters of another word, i.e. the same letters but in a different order).
    the list to return (strings and lists) are arranged according to the order in which the strings appear in the
    original list.
    :param list_of_strings: list of strings.
    :type list_of_strings: list.
    :return: list of list of strings.
    :rtype: list
    """
    dict_list_of_anagrams = {}
    for word in list_of_strings:
        patern = "".join(sorted(word))

        if patern in dict_list_of_anagrams:
            dict_list_of_anagrams[patern].append(word)
        else:
            dict_list_of_anagrams[patern] = [word]

    return list(sorted(dict_list_of_anagrams.values()))



