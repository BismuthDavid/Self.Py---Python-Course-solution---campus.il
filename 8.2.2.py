def sort_prices(list_of_tuples):
    """
    this func will receive a list of tuples and sort them from the highest to lowest price.
    :param list_of_tuples: list of tuples. [('item', 'price'), ('item', 'price'), ('item', 'price')]
    :type list_of_tuples: list.
    :return: list of sorted tuples.
    :rtype: list.
    """
    sorted_list = sorted(list_of_tuples, key=lambda x: x[1], reverse=True)
    return sorted_list
