def fix_age(age):
    """
    if the parameter equal to a num matching this conditions: 13 < age < 19 and != 15,16, the func will
    replace it with 0 as a value
    :param age: age
    :type age: int
    :return: the original or the fixed age
    :rtype: int
    """
    age_range =(13, 14, 17, 18, 19)
    if age in age_range:
        return int(0)
    else:
        return age


def filter_teens(a = 13, b = 13, c = 13):
    """
    this func will receive 3 nums (ages) and will return their sum.
    if one of the num is > 13 and < 19 while != 15,16 - the value will be updated to 0
    :param a, b, c: age of the child
    :type a, b, c: int
    :return: sum of the correct ages
    :rtype: int
    """
    sum_of_ages = fix_age(a) + fix_age(b) + fix_age(c)
    return sum_of_ages


