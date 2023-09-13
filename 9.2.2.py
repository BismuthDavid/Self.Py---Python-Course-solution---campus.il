def copy_file_content(source, destination):
    """
    this func will receive a file path to copy from and a file path to write to.
    :param source: file pate to read from it the info.
    :type source: str.
    :param destination: file path to write into the info.
    :type destination: str.
    :return: copy all the info from source to destination.
    :rtype: noun - the func will only copy from one file to the other.
    """
    info = ""
    with open(source, "r") as input_file:
        for line in input_file:
            info += line
    with open(destination, "w") as output_file:
        output_file = info


