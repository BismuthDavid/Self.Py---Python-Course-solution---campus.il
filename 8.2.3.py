def mult_tuple(tuple1, tuple2):
    """
    The function receive as parameters two structures of tuple.
    The function returns a tuple containing all the pairs that can be created from the obj. of the tuples passed
     as arguments.
    :param tuple1, tuple2: tuple of obj.
    :type tuple1, tuple2: tuple
    :return: tuple containing all the pairs that can be created
    :rtype:tuple
    """
    tuple_of_all_combination = [(a, b) for a in tuple1 for b in tuple2]
    tuple_of_all_combination += [(a, b) for a in tuple2 for b in tuple1]
    tuple_of_all_combination = tuple(tuple_of_all_combination)
    return tuple_of_all_combination
