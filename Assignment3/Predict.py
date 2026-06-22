def fun():
    x=10
    print(x)
fun()
print(x)


""" output
10
error
Traceback (most recent call last):
File "C:\Users\bhosa\OneDrive\Desktop\python\Assignment3\predict.py", line 5, in <module>
    print(x)
          ^
NameError: name 'x' is not defined

reason-
When fun() is called, the variable x is created inside the function.
print(x) inside the function prints 10.
After the function finishes execution, the local variable x is destroyed.
The statement print(x) outside the function tries to access x, but x exists only inside fun().
A variable created inside a function is called a local variable. It can be accessed only within that function.
"""