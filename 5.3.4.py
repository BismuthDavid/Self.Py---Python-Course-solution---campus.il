def last_early(my_str):
    """
    this func will check if the last char of a string appears in the string more than once
    :param my_str: string of chars
    :type my_str: str
    :return: true if it appears or false if it doesn't
    :rtype: bool
    """
    last_char = my_str[-1].lower()
    my_str = my_str[0:-1].lower()
    if last_char in my_str:
        return True
    else:
        return False
