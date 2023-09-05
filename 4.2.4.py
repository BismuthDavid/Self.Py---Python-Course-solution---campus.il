import calendar
date_to_check = input("Enter a date in a dd/mm/yyyy format:\n")
year, month, day = int(date_to_check[-4:]), int(date_to_check[3:5]), int(date_to_check[0:2])
num_of_the_day = calendar.weekday(year, month, day)
weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekday_names[num_of_the_day])