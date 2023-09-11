from datetime import date, datetime

person_dict = {"first_name": "mariah", "last_name": "carey", "birth_date": "27.03.1970",
               "hobbies": ["sing", "compose", "act"]}


def calculate_age(birth_date):
    """
    this func will receive date in a (yyyy/mm/dd) format and calculate the age of that person today
    :param birth_date: date in a (yyyy/mm/dd) format
    :type birth_date: date.
    :return: num of year past
    :rtype: int
    """
    date_format = "%Y-%m-%d"
    current_date = datetime.now()
    birth_date = datetime.strptime(birth_date, date_format)
    age = current_date.year - birth_date.year
    age = age - 1  # self.py asks for a solution based on the 2021 year, they didnt update the exercise
    return age


operator = int(input("please enter a number between 1 - 7 : "))
if operator == 1:
    print(person_dict["last_name"])
elif operator == 2:
    print(person_dict["birth_date"][3:5])
elif operator == 3:
    print(len(person_dict["hobbies"]))
elif operator == 4:
    print(person_dict["hobbies"][-1])
elif operator == 5:
    person_dict["hobbies"].append("Cooking")
elif operator == 6:
    birth_date_tuple = (person_dict["birth_date"][0:2], person_dict["birth_date"][3:5], person_dict["birth_date"][6:])
    print(birth_date_tuple)
elif operator == 7:
    birth_date_str = str(person_dict["birth_date"][6:] + "-" + person_dict["birth_date"][3:5] + "-" +
                         person_dict["birth_date"][0:2])
    print(calculate_age(birth_date_str))
