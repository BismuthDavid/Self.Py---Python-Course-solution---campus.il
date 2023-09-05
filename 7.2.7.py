def arrow(my_char, max_length):
    """
    this func will receive a char and build an arrow shape that with the char.
    the widest row in the arrow shape will be at the size given by "max length".
    :param my_char: single char
    :type my_char: str
    :param max_length: size of the widest point of the arrow.
    :type max_length: int
    :return: a str shaped as an arrow
    :rtype: str
    """
    arrow_sign = ""
    if max_length <= 1:
        return my_char * max_length
    else:
        for x in range(1, max_length):
            arrow_sign += my_char * x + "\n"
        for x in range(max_length, 1, -1):
            arrow_sign += my_char * x + "\n"
        arrow_sign += my_char
    return arrow_sign
