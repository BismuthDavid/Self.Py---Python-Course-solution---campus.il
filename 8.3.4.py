from collections import defaultdict


def inverse_dict(my_dict):
    """
     The function returns a new dictionary with a "reverse" mapping:
    each key in the passed dictionary is a value in the returned dictionary
    and each value in the passed dictionary is a key in the returned dictionary.
    :param my_dict: dict of keys and values.
    :type my_dict: dict.
    :return: dict of keys and values (possible lists as values if the value of the new key appears as a value
     more than once
    :rtype:dict
    """
    inverted_dict = defaultdict(list)
    for key, value in my_dict.items():
        inverted_dict[value].append(key)
    for key, value in inverted_dict.items():
        value.sort()
    return inverted_dict
