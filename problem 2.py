#defining the function converted_temperature() with temperature as value, temperature unit as unit
def converted_temperature(value,unit):
    #if unit is in degree celsius as C
    if unit == "C":
        #converts it into farenheit
        return (value - 32)*5/9, "F"
    #if unit is in farenheit as F
    elif unit == "F":
        #converts it into degree celsius
        return (value *9/5)+32, "C"
    else:
        return None,None

#taking input temperature as value from user
temperature = float(input("Enter the Temperature:"))
#taking input temperature unit as unit from user
unit = input("Enter ( celsius as C or farenheit as F):").upper()

#assigning the converted value and unit
converted_value,converted_unit = converted_temperature(temperature,unit)

if converted_temperature is None:
    print("Invalid, please")
else:
    print(f"converted temperature:{converted_value:.2f}{converted_unit}")
