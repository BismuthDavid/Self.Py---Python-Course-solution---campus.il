def are_files_equal(file1, file2):
    """
    the func will receive 2 file path and checks if they are equal.
    :param file1, file2: file path
    :type file1, file2: string files
    :return: true if equal, false if different
    :rtype: bool
    """
    first_file, second_file = "", ""
    with open(file1, "r") as input_file:
        for line in input_file:
            first_file += line
    with open(file2, "r") as input_file:
        for line in input_file:
            second_file += line
    if first_file == second_file:
        return True
    else:
        return False
