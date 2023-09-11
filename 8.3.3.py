def count_chars(my_str):
    """
    this func will receive a string as a parameter, and return a dict that every char is a key, and the value will be
    how many times the char appears on the string.
    :param my_str: string of chars.
    :type my_str: str
    :return: dict with chars as a key and num of appearance as a value
    :rtype: dict
    """
    new_dict = {}
    my_str = my_str.replace(" ", "")
    for char in my_str:
        counter = my_str.count(char)
        new_dict[char] = counter
    return new_dict

