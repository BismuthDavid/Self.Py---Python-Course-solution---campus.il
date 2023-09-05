def distance(num1, num2, num3):
    """
    this func will receive 3 num & return true if 2 condition are true:
    1. one of the nums is close in an abs value to the first num.
    2. the other num is close >= 2 from the first num
    :param num1, num2, num3: numbers
    :type num1, num2, num3: int
    :return: true if the 2 condition are true, false if it isn't
    :rtype: bool
    """
    case1 = abs(num1 - num2) <= 1 or abs(num3 - num1) <= 1
    case2 = abs(num3 - num2) >= 2 and abs(num3 - num1) >= 2 or abs(num2 - num1) >= 2 and abs(num2 - num3) >= 2
    return case2 and case1



