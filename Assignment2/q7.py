"""Why does the input() function always return a string?
How can you convert it to another data type?"""

age=input("enter the age")
print("age")
print(type(age))


age=int(input("enter the age"))
print(type(age))

salary=float(input("enter the salary"))
print(type(salary))

value=bool(input("enter the value"))
print(type(value))


"""output
enter the age2
age
<class 'str'>
enter the age32
<class 'int'>
enter the salary23.2
<class 'float'>
enter the value0
<class 'bool'>
"""


