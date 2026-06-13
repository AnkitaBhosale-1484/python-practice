"""2. What is the difference between:
a = 10
b = 10
and
a = [10]
b = [10]
Explain using id().
"""

a=10
b=10

print("value of a",(a))
print(id(a))
print("value of b",(b))
print(id(b))


a=[10]
b=[10]

print("value of a",(a))
print(id(a))
print("value of b",(b))
print(id(b))

""" output...
value of a 10
140736932464024
value of b 10
140736932464024
value of a [10]
1923037378112
value of b [10]
1923037261760 """
