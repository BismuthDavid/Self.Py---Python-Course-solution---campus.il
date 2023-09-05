def numbers_letters_count(my_str):
    """
    this func will receive a str that contain digit's and char's, the func will return a list [sum of digit in string,
    sum of char including non alpha-beta char's]
    :param my_str: string of char's & digit's]
    :type my_str: str
    :return:  list in this format [sum of digit in string, sum of char including non alpha-beta char's]
    :rtype: list
    """
    i = 0
    for x in my_str:
        if x.isdigit():
            i += 1
    num_of_chars = len(my_str) - i
    new_list = [i, num_of_chars]
    return new_list
