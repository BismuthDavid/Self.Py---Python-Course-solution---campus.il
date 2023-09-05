def longest(my_list):
    """
    this func will return the longest string in the list
    :param my_list: list of strings
    :type my_list: list
    :return: longest string in the list
    :rtype: str
    """
    return max(my_list, key = len)
