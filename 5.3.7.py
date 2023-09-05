def chocolate_maker(small, big, x):
    """
    The function receives the number of small cubes (small = len(1)), the number of large cubes (big = len(5))
    and the desired line length (x). The function returns true if it is possible to create a line of length x
    using the number of chocolate cubes it received, all or some.
    :param small, big ,x: number
    :type small, big, x: int
    :return: true if we can create or false if not
    :rtype: bool
    """
    big_block = 5
    if x < (small + big * big_block):
        return True
    elif big == 0 and small < x:
        return False
    elif small > x % big * big_block:
        return True
    else:
        return False
