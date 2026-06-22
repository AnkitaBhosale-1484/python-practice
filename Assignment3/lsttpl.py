lst=[10,20,30]
tpl=(10,20,30)

lst[0]=100
print(lst)
tpl[0]=100


"""output
C:\Users\bhosa\OneDrive\Desktop\python\Assignment3>python lsttpl.py
[100, 20, 30]

    tpl[0]=100
    ~~~^^^
TypeError: 'tuple' object does not support item assignment

List (lst) is mutable, so its elements can be changed after creation.
Tuple (tpl) is immutable, so its elements cannot be changed after creation.
"""

