def split_obj(my_str):
    """
    this func will receive a string of obj. to buy and will split it into list
    :param my_str: string of obj. with "," sign between one and other.
    :type my_str: str
    :return: the func will not return a value, only convert the values to list.
    :rtype: list
    """
    my_list = my_str.split(",")
    return my_list


def check_if_appears(my_list):
    """
    this func will receive a list and take an input of an obj. then will verify if it appears on the list.
    :param my_list: list of of obj.
    :type my_list: list 
    :return: true if the input obj. appears and false if it doesnt
    :rtype: bool
    """
    obj_to_check = input("please enter a name of the obj. to check:\n")
    if obj_to_check in my_list:
        return True
    else:
        return False


def how_many_times_appears(my_list):
    """
    this func will receive an input of an obj. and the list, then it will count how many times it appears and return the
    value.
    :param my_list: list of obj.
    :type my_list: list
    :return: how many times the input obj. appears.
    :rtype: int
    """
    obj_to_check = input("please enter a name of the obj. to check:\n")
    num_of_times = my_list.count(obj_to_check)
    return num_of_times


def delete_the_input(my_list):
    """
    this func will receive an input of an obj. and the list, then it will delete the input value from the list.
    :param my_list: list of obj.
    :type my_list: list.
    :return: list without the input obj.
    :rtype: list
    """
    obj_to_delete = input("please enter a name of the obj. to delete:\n")
    my_list.remove(obj_to_delete)
    return my_list


def add_the_input(my_list):
    """
    this func will receive an input of an obj. and the list, then it will add the input value to the list.
    :param my_list: list of obj.
    :type my_list: list.
    :return: list with the input obj.
    :rtype: list
    """
    obj_to_add = input("please enter a name of the obj. to add:\n")
    my_list.append(obj_to_add)
    return my_list


def to_short_obj(my_list):
    """
    this func will print all the obj. that are too short (item name < len 3).
    :param my_list: list of obj.
    :type my_list: list
    :return: noun, only print operation
    :rtype: none
    """
    for obj in my_list:
        if len(obj) < 3 or not obj.isalpha():
            print(obj)
    return


string_of_obj = str(input("please enter a list of obj. to buy with comma sign to separate them:\n"))
operator_chosen = 0
list_of_obj = list(split_obj(string_of_obj))

while operator_chosen != 9:

    operator_chosen = int(input("please enter a single digit to chose the operation you would like to preform:\n"))

    if operator_chosen == 1:        # printing the list.
        print(list_of_obj)

    elif operator_chosen == 2:      # printing how many obj. are in the list.
        print(len(list_of_obj))

    elif operator_chosen == 3:      # print true or false if the input obj. is in the list.
        print(check_if_appears(list_of_obj))

    elif operator_chosen == 4:      # print how many times the input obj. appears on the list.
        print(how_many_times_appears(list_of_obj))

    elif operator_chosen == 5:      # delete the input obj. from the list.
        list_of_obj = delete_the_input(list_of_obj)

    elif operator_chosen == 6:      # add the input obj. to the list.
        list_of_obj = add_the_input(list_of_obj)

    elif operator_chosen == 7:      # print all the obj. that there name is < 3 char's.
        to_short_obj(list_of_obj)

    elif operator_chosen == 8:      # remove duplicate values from the list
        list_of_obj = list(dict.fromkeys(list_of_obj))

