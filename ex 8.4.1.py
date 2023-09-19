pic1 = """
    x-------x"""
pic2 = """
    x-------x
    |
    |
    |
    |
    |"""
pic3 = """
    x-------x
    |       |
    |       0
    |
    |
    |
"""
pic4 = """
    x-------x
    |       |
    |       0
    |       |
    |
    |"""
pic5 = """
    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |
"""
pic6 = """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      /
    |
"""
pic7 = """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \ 
    |"""


dict_of_hangman = {1: pic1, 2: pic2, 3: pic3, 4: pic4, 5: pic5, 6: pic6, 7: pic7}


def print_hangman(num_of_tries):
    """
    this func will print a string of chars that represent the HANGMAN as a factor of num of times the user guessed wrong the
    letter.
    :param num_of_tries: num of times he failed to guess the next letter.
    :type num_of_tries: int
    :return: none, just printing string of chars that represent the HANGMAN
    """
    print(dict_of_hangman[num_of_tries])
