def reversing_string(value):
    reversed_string =""
    for char in value:
        reversed_string = char + reversed_string
    return reversed_string

value = str(input("Enter only string:"))
print(reversing_string(value))