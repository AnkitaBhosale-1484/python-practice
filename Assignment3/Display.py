from sys import getsizeof
value=eval(input("enter the the value"))

print(value)
print("Data Type:",type(value))
print("Memory Address:",id(value))

print("size in bytes:",getsizeof(value))


"""output
enter the the value12
12
Data Type: <class 'int'>
Memory Address: 140729021547992
size in bytes: 28

enter the the value"ankita"
ankita
Data Type: <class 'str'>
Memory Address: 2180738602480
size in bytes: 47

"""