def is_greater(my_list, n):
    """
    this func will receive a list with nums, and a num as a criteria.
    the func will return only the nums in the list that are greater than the criteria.
    :param my_list: list of nums
    :type my_list: list
    :param n: a num as a criteria to check
    :type n: int
    :return: list of nums that are greater than num
    :rtype: list
    """
    new_list = []
    for x in my_list:
        if x > n:
            new_list.append(x)
    return new_list
