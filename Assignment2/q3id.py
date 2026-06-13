"""What does the id() function return?
Is the value returned by id() same for two variables holding the same value?"""

a=11
print(id(a))

x=11
y=11

print(id(x))
print(id(y))

print(id(x)==id(y))

a=11
b=11   

print(id(a))
print(id(b))

print(id(a)==id(b)) #depending on data type


""" output...
140736717440440
140736717440440
140736717440440
True
140736717440440
140736717440440
True

"""