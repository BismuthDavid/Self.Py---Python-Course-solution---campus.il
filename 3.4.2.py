full_string = input("please enter a string:\n")
first_letter = full_string[0:1]
string_without_first = full_string[1::1]
full_string = first_letter + string_without_first.replace(first_letter, "e")
print(full_string)
    
