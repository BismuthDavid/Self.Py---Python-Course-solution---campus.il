def format_list(my_list):
    """
    this func will return a list of the obj. from the even idx, with the last obj. with "and" before it
    :param my_list: list of obj.
    :type my_list: list
    :return: str of the obj.
    :rtype: str
    """
    my_list_str = my_list[0:-1:2]
    my_list_str = ", ".join(my_list_str) + ", and " + my_list[-1]
    return my_list_str
