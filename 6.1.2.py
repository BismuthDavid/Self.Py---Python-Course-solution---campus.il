def shift_left(my_list):
    """
    this func will receive a list and take the first obj. (i=0) and put him last insted.
    :param my_list: list of obj.
    :type my_list: list
    :return: list reordered with the first obj. as a last obj.
    :rtype: list
    """
    if len(my_list) > 1:
        first_idx = my_list.pop(0)
        my_list.append(first_idx)
    return my_list
