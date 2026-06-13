"""Predict the output:
x = input("Enter number: ")
print(type(x))
Explain the reason."""


x = input("Enter the number: ")
print(type(x))


"""outpuut..
Enter the number: 10
<class 'str'>

"""

#The input() function always returns the value entered by the user as a string (str).
#  Even if the user enters a number such as 10, Python treats it as the string "10" because keyboard input is read as text by default.