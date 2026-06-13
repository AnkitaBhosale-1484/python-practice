"""predict the output
a=10
b=10
print(id(a)==id(b))
explain why this happens"""


a=10
b=10

print(id(a)==id(b)) #both variables refer to the same memory location as they are immutable

"""
output
True
"""