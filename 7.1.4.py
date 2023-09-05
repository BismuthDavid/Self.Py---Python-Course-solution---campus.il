def squared_numbers(start, stop):
    """
    this func will receive 2 nums and will return every num in the range between them as a squared value.
    :param start: first number of the range
    :param stop:last number of the range
    :type start, stop: int
    :return: list of squared value of every int in the range
    :rtype: list
    """
    squared_value_list = []
    for x in range(start, stop + 1):
        squared_value_list.append(x ** 2)
    return squared_value_list
