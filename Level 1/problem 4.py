#defining the addition function
def add(a,b):
    return a + b
#defining the substraction function
def minus(a,b):
    return a - b 
#defining the multiply function
def mul(a,b):
    return a * b 
#defining the division function
def div(a,b):
    return a/b 
#defining the modulus function
def mod(a,b):
    return a%b 
#assigning the variables
a = float(input("Enter the first value :"))
b = float(input(" Enter the second value :"))
#input for the operator
o = input("Enter the operation (+,-,%,*,/):")
#conditions for checking the operation
if o == '+':
    print(add(a,b))
elif o == '-':
    print(minus(a,b))
elif o == '*':
    print(mul(a,b))
elif o == "/":
    print(div(a,b))
elif o == "%":
    print(mod(a,b))
else:
    print("Enter valid operation.")