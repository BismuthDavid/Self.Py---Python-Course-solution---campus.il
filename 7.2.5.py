def sequence_del(my_str):
    """
    this func will receive and fix string that contain the same char more than once in a row, the duplicate chars will
    be deleted.
    :param my_str: string of char's
    :type my_str: str
    :return: fixed str without duplicated char's
    :rtype: str
    """
    if len(my_str) <= 1:
        return my_str
    else:
        list_to_convert = [my_str[0]]
        idx = 0
        for x in my_str[1:]:
            if x != my_str[idx]:
                list_to_convert.append(x)
            idx += 1
        my_str = "".join(list_to_convert)
        return my_str
