def are_lists_equal(list1, list2):
    """
    this func will check and return true only is the list contain the same value (no matter the order) and false if it
    isn't
    :param list1, kist2: list of obj.
    :type list1, list2: list
    :return: true if the same, false if it isn't
    :rtype: bool
    """
    if sorted(list1) == sorted(list2):
        return True
    else:
        return False
