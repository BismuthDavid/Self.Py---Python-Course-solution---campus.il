def who_is_missing(file_name):
    """
    this func will receive a file path that contain nums from 1 -> N, not sorted, divided by commas.
    one of the nums between the smallest (1) to the greater (N) will be missing.
    the func will sort them out, return the missing num and write it to a new file named "found.txt".
    :param file_name: file path to a file filled with nums.
    :type file_name: str.
    :return: the missing num and create a file with the missing num.
    :rtype: int + file.
    """
    with open(file_name, 'r') as input_file:
        list_of_nums =  [int(num) for num in input_file.read().split(",")]

    if len(list_of_nums) == 1:
        missing_num = list_of_nums[0] - 1
    else:
        list_of_nums.sort()
        for i in range(len(list_of_nums) - 1):
            if list_of_nums[i + 1] - list_of_nums[i] > 1:
                missing_num = list_of_nums[i] + 1
                break

    with open('found.txt', 'w') as new_file:
        new_file.write(str(missing_num))

    return missing_num

