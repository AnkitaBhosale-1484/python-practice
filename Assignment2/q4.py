"""What is the purpose of getsizeof()?
Why is memory size different for different data types?"""


from sys import getsizeof

a=10
print(getsizeof(a))


""" output...
28
"""

y=3.14
print(getsizeof(y))

lst=[12,23,23]
print(getsizeof(lst))

tuple=(11,22,34)
print(getsizeof(tuple))

"""
output..
28
24
88
72

"""

