def my_mp4_playlist(file_path, new_song):
    """
    this func will receive a file path to a file that already contain info at this format:["song name":"singer":
    "song length"] and a new name for the third song (if there isn't a third song, the func will write blank rows till
    the third row and there it will write the name of the song.
    :param file_path: string for the file path.
    :param new_song: string for the new name of the third song.
    :type file_path, new_song: str.
    :return: the func will print the final output, and save the info to the original file.
    :rtype: none
    """
    with open(file_path, 'r') as input_file:
        data = input_file.read().splitlines()
    if len(data) >= 3:
        line = data[2].split(";")
        line[0] = new_song
        str_line = ";".join(line)
        data[2] = str_line
    elif len(data) == 2:
        data.append(new_song + ";")
    elif len(data) == 1:
        data.append(" ")
        data.append(new_song + ";")
    with open(file_path, 'w') as output_file:
        data_to_write = "\n".join(data)
        output_file.write(data_to_write)
    print(data_to_write)
