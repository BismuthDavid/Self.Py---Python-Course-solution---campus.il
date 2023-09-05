in_string = input("please enter a word:\n")
reverse_string = in_string[-1::-1]
if in_string.lower().replace(" ", "") == reverse_string.lower().replace(" ", ""):
    print("OK")
else:
    print("NOT")
