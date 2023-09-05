full_string = input("Please enter a string:\n")
lenght_of_str = int(len(full_string))
first_half = (lenght_of_str // 2)
lower_case = full_string[0:first_half]
upper_case = full_string[first_half:]
print(lower_case.lower() + upper_case.upper())
