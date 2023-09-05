str_temp_to_convert = input("Insert the temperature you would like to convert:\n")
temperature = float(str_temp_to_convert[0:-1])
temperature_sign = str_temp_to_convert[-1]
temperature_sign = temperature_sign.upper()

if temperature_sign == "F":
    temperature = ((temperature * 5) - 160) / 9
    temperature_sign = "C"
else:
    temperature = (((temperature * 9) + 160) / 5)
    temperature_sign = "F"
print(str(temperature) + temperature_sign)
