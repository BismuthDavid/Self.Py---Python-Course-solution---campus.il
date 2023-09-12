def sort(str_file_path):
    """
    this func will sort the words in the file from a -> z while removing duplicat word
    :param str_file_path: file path to read from it.
    :type str_file_path: str
    :return: print sorted list of word.
    :rtype: noun - just printing order.
    """
    list_to_sort = list()
    with open(str_file_path) as input_file:
        for line in input_file:
            line = line.split()
            for word in line:
                if word not in list_to_sort:
                    list_to_sort.append(word)
        list_to_sort.sort()
    print(list_to_sort)


def rev(str_file_path):
    """
    this func will print every char in a line from the file in a reversed order.
    :param str_file_path: string of file path
    :type str_file_path: str
    :return: printing every line in a reversed order.
    :rtype: noun - just a printing order.
    """
    with open(str_file_path) as input_file:
        for line in input_file:
            print(line[-2::-1])


def last(str_file_path):
    """
    this func will request one more variable as a num of line from the end to print
    :param str_file_path: string of file path
    :type str_file_path: str
    :return: printing N lines from the end of the file (N = num as an input from user)
    :rtype: noun - just printing order.
    """
    i = 0
    line_num = int(input("Enter a number: "))
    with open(str_file_path) as input_file:
        for line in input_file:
            if i < line_num:
                i += 1
            else:
                print(line)


def main():
    """
    this func will ask for file path and which command to do with it
    """
    file_path = input("please enter a file path to read:\n")
    operator = input("please chose the op. you would like to do [ sort  |  rev  |  last  ]:\n")
    if operator == "sort":
        sort(file_path)
    elif operator == "rev":
        rev(file_path)
    elif operator == "last":
        last(file_path)


if __name__ == "__main__":
    main()
