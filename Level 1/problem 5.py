#defining the function palindrome
def palindrome_check(string):
    #returning with the reversed string
    return string == string[::-1]
#input the palindrome checking word
word = input("Enter the word:")
#assigning a variable with function
result = palindrome_check(word)
#printing the result
print(result)