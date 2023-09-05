def seven_boom(end_number):
    """
    this func will return a list of every num between 0 to end number while changing every num that has the 7 digit in
    it or is a multiplication of 7 by the str "BOOM".
    :param end_number: number that is the end of the range to print.
    :type end_number: int
    :return: list of digits and strings
    :rtype: list
    """
    new_list = []
    for x in range(0, end_number + 1):
        if x % 7 == 0 or x % 10 == 7:
            new_list.append("BOOM")
        else:
            new_list.append(x)
    return new_list