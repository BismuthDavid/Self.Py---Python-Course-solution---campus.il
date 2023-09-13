def my_mp3_playlist(file_path):
    """
    this func will receive a file path that contain info about songs at this format ["song name":"singer":"song length"]
    the func will read the info, and will return a tuple with the info at this format ["the longest song", "num of songs
    that the file contain", "the singer that appears max time on the list"].
    :param file_path: string of file path.
    :type file_path: str.
    :return: tuple of info at the chosen format.
    :rtype: tuple.
    """
    with open(file_path, 'r') as input_file:
        song_data = input_file.readlines()
    length_of = len(song_data)

    song_length, singer_count = {}, {}

    for line in song_data:
        line_list = line.split(";")
        song_length[line_list[0]] = line_list[2]

        if line_list[1] in singer_count.keys():
            singer_count[line_list[1]] += 1
        else:
            singer_count[line_list[1]] = 1

    return max(song_length, key=song_length.get), length_of, max(singer_count, key=singer_count.get)
