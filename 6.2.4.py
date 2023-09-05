def extend_list_x(list_x, list_y):
    """
    this func will create a new list based on the 2 given list
    :param list_x, lisy_y: list of obj.
    :type list_x, list_y: list
    :return: new extended list based on the 2 originals
    :rtype: list
    """
    new_extended_list = list_y
    for x in list_x:
        new_extended_list.append(x)
    return new_extended_list

